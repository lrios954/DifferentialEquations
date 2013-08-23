import pylab
import numpy
import sys

# Definimos el potencial para un pozo de paredes finitas

def V(x):

    if x < 1.0:

        return 0.0
    
    if x >= 1.0:

        return 0.0


# Aqui tomaremos que psi = y1 y que  psi' = y2, luego definimos las derivadas de y1 y y2

def y1_prime(x,y1,y2,B,V,E):

    return y2

def y2_prime(x,y1,y2,B,V,E):

    return B*(V-E)*y1

# Definimos el intervalo [a,b] donde queremos resolver nuestra ecuacion diferencial y definimos el paso h que vamos a tomar

a = 0.0
b = 3.0
h = 0.0001

# Calculamos cuantos puntos vamos a tener (n_points) y luego creamos una lista de las coordenadas en x saltando en h de la siguiente manera:
#
# x =[a,a+h,a+2h,a+3h,...,b]

n_points = int((b-a)/h)
x = [a+i*h for i in range(n_points+1)]

# Definimos valor es para la energia y el parametro B

B = 134.95
E= [float(sys.argv[2])]
# Resolvemos numericamente aproximando la derivada por la secante
for j in range(len(E)):
    print j
# Creamos listas para y1 y y2
    y1 = []
    y2 = []
    
# Establecemos nuestras condiciones iniciales
    if sys.argv[1] == 'par':
        y1.append(1.0)
        y2.append(0.0)

    if sys.argv[1] == 'impar':
        y1.append(0.0)
        y2.append(1.0)

    for i in range(1,n_points+1):

        a1 = y1_prime(x[i-1],y1[i-1],y2[i-1],B,V(x[i-1]),E[j])
        a2 = y2_prime(x[i-1],y1[i-1],y2[i-1],B,V(x[i-1]),E[j])

        y1.append(h*a1+y1[i-1])
        y2.append(h*a2+y2[i-1])
        
        
# Graficamos y guardamos
    if (1):
        norm = numpy.trapz([k**2.0 for k in y1])
        if sys.argv[1] == 'par':
            psi = [y/norm for y in y1] + [y/norm for y in y1]
            ex = [-i for i in x] + x
        if sys.argv[1] == 'impar':
            psi = [-y/norm for y in y1] + [y/norm for y in y1]
            ex = [-i for i in x] + x            
        pylab.plot( ex, psi, '.k')
        pylab.xlim([-3.0,3.0])
        pylab.xlabel('$x$')
        pylab.ylabel('$\psi$')
        pylab.title('Energy = '+str(E[j])+' eV')
        pylab.savefig(sys.argv[1]+'_'+str(E[j])+'.png')
#       pylab.show()
    pylab.close()
