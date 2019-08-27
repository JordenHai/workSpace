import numpy
m = 1.82781*10**8
X_P = 3.3*10**6
d = 16.5
C_b = 0.8580
B = 45.0
L = 280.0
S = 19556.1
p = 1.02473*10**3
v = 1.05372*10**(-6)
m_x = 4.799*10**7

print(m_x)
def func(y):
    R = y * L / v
    t = numpy.log10(R)
    C_f = 0.075 / ((t - 2)**2)
    C_t = C_f + 0.9*10**(-3) +4*10**(-4)
    X_H = -2*S*C_t/L/L/d/d/p
    return (X_H+X_P)/(m+m_x)

for i in range(100):
    value = func(i)
    print(value)
