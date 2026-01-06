def contaRegressivaRecursao(x):
    if x <= 0:
        return
    print(x) 
    contaRegressivaRecursao(x - 1)

contaRegressivaRecursao(10)