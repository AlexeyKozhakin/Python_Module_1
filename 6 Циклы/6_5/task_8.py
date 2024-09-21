from math import log10
N = 100
x0 = 22
xn = 24
dx = (xn-x0)/N
x_min = 0
df_min = 1e10
for n in range(1,N):
    x = x0 + n*dx
    f_left = x**(2*log10(x)**2)
    f_right = 10*x**3
    df = abs(f_left-f_right)
    if df<df_min:
        df_min = df
        x_min = x

print(x_min)