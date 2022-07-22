import numpy as np

def aicc(ss, constant):
    if not constant:
        return N * np.log(ss/N) + 2 * (p+q+1) * N / (N - p - q - 2)
    else:
        return N * np.log(ss/N) + 2 * (p+q+2) * N / (N - p - q - 3)


N = 4989
ss = 6.40558
constant = True
p, d, q = 2, 1, 2
print(ss, constant, aicc(ss, constant))
