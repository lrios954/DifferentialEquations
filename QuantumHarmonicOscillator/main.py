import pylab
import numpy

# Definimos constantes

hbar = 6.582119 * (10.0**(-16.0))
mass = 510998.9
omega = 2.5 * (10.0 ** 15.0)
B = 0.0734986
a0 = 5.2917721092 * (10.0**(-11.0))

# Definimos el potencial para un oscilador armonico

def V(x):

#    return (0.5)* mass * (omega**2.0) * (a0 ** 2.0) * (x**2)
    
     return 0.5 * 0.09951 * x**2
# Aqui tomaremos que psi = y1 y que  psi' = y2, luego definimos las derivadas de y1 y y2

def y1_prime(y2):

    return y2

def y2_prime(x,y1,E):

    return B*(V(x)-E)*y1

# Definimos el intervalo [a,b] donde queremos resolver nuestra ecuacion diferencial y definimos el paso h que vamos a tomar

a = 0.0
b = 15.0
h = 0.0001

# Calculamos cuantos puntos vamos a tener (n_points) y luego creamos una lista de las coordenadas en x saltando en h de la siguiente manera:
#
# x =[a,a+h,a+2h,a+3h,...,b]

n_points = int((b-a)/h)
x = [a+i*h for i in range(n_points+1)]

# Definimos valor es para la energia y el parametro B

E = [hbar*omega*(float(n)+0.5) for n in range(10)]
#E = [1.646*(float(n)+0.5) for n in range(5)]

# Resolvemos numericamente aproximando la derivada por la secante
for j in range(len(E)):

# Creamos listas para y1 y y2
    y1 = []
    y2 = []
    
# Establecemos nuestras condiciones iniciales
    y1.append(1+(-1)**(j))
    y2.append(1+(-1)**(j+1))
    
    for i in range(1,n_points+1):

        a1 = y1_prime(y2[i-1])
        a2 = y2_prime(x[i-1],y1[i-1],E[j])

        y1.append(h*a1+y1[i-1])
        y2.append(h*a2+y2[i-1])

# Graficamos y guardamos
    norm = numpy.trapz([y**2.0 for y in y1],x)
    if(j%2==0):
        psi = [y1[len(y1)-i-1]/norm for i in range(len(y1))] + [y/norm for y in y1]
        ex = [-x[len(x)-i-1] for i in range(len(x))] + x
    else:
        psi = [-y1[len(y1)-i-1]/norm for i in range(len(y1))] + [y/norm for y in y1]
        ex = [-x[len(x)-i-1] for i in range(len(x))] + x      
    
    pylab.plot(ex , psi, 'k')
    pylab.xlim([-b,b])
    pylab.ylim([-0.2,0.2])
    pylab.xlabel('$x$')
    pylab.ylabel('$\psi$')
    pylab.title('n = '+str(j+1)+'   Energy = '+str(E[j])+' eV')
    pylab.savefig(str(j+1)+'.png')
    pylab.close()
