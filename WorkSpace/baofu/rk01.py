import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'

fig = plt.figure(figsize=(12, 8), dpi=100)

N = 100000
h = 0.1
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

X, Y = [0], [0]

def f(x,y):
    R = y * L / v
    t = np.log10(R)
    C_f = 0.075 / ((t - 2)**2)
    C_t = C_f + 0.9*10**(-3) +4*10**(-4)
    X_H = -1/2*p*y*y*S*C_t
    return (X_H+X_P)/(m+m_x)
#
# def f(x, y):
#     return -x * y ** 2
y_n = 2
for i in range(N):
    x_n = i * h
    k_1 = f(x_n, y_n)
    k_2 = f(x_n + 0.5 * h, y_n + 0.5 * h * h * k_1)
    k_3 = f(x_n + 0.5 * h, y_n + 0.5 * h * k_2)
    k_4 = f(x_n + h, y_n + h * k_3)
    y_n += 1 / 6 * h * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
    X.append(x_n + h)
    Y.append(y_n)

plt.plot(X, Y, 'r:')
print(Y)
f = open('log.txt','w')
for i in Y:
    if(i == float('inf')):
        break
    else:
        f.write(str(i))
        f.write(str(','))
        f.flush()
        print(i)
plt.show()

