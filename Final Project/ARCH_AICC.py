def aicc(N, logLik, q):
    return -2 * logLik + 2 * (q + 1) * N / (N - q - 2)


N = 4989
logLik = 9799.593
q = 2
print(aicc(N, logLik, q))
