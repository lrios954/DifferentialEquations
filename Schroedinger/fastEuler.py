import pylab
import numpy

# Definimos el potencial para un pozo de paredes finitas

def V(x):

    if x < 1.0:

        return 0.0
    
    if x >= 1.0:

        return 1.0


# Aqui tomaremos que psi = y1 y que  psi' = y2, luego definimos las derivadas de y1 y y2

def y1_prime(x,y1,y2,B,V,E):

    return y2

def y2_prime(x,y1,y2,B,V,E):

    return B*(V-E)*y1

# Definimos el intervalo [a,b] donde queremos resolver nuestra ecuacion diferencial y definimos el paso h que vamos a tomar

a = 0.0
b = 2.0
h = 0.01

# Calculamos cuantos puntos vamos a tener (n_points) y luego creamos una lista de las coordenadas en x saltando en h de la siguiente manera:
#
# x =[a,a+h,a+2h,a+3h,...,b]

n_points = int((b-a)/h)
x = [a+i*h for i in range(n_points+1)]

# Definimos valor es para la energia y el parametro B

B = 134.95
E = numpy.arange(0.0 , 1.0, 0.0000001)
got = 0
# Resolvemos numericamente aproximando la derivada por la secante
for j in range(len(E)):
    print str(j) + ' of '+str(len(E))+'. '+str(got)+' solutions founded'  
# Creamos listas para y1 y y2
    y1 = []
    y2 = []
    
# Establecemos nuestras condiciones iniciales
    y1.append(0.0)
    y2.append(1.0)
    
    for i in range(1,n_points+1):

        a1 = y1_prime(x[i-1],y1[i-1],y2[i-1],B,V(x[i-1]),E[j])
        a2 = y2_prime(x[i-1],y1[i-1],y2[i-1],B,V(x[i-1]),E[j])

        y1.append(h*a1+y1[i-1])
        y2.append(h*a2+y2[i-1])

# Graficamos y guardamos
    if (numpy.abs(y1[n_points]) < 0.1):
        got = got + 1
        pylab.plot(x , y1, 'k')
        pylab.xlim([a,b])
        pylab.xlabel('$x$')
        pylab.ylabel('$\psi$')
        pylab.title('Energy = '+str(E[j])+' eV')
        pylab.savefig(str(j)+'.png')
#       pylab.show()
    pylab.close()
