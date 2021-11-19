Valores = { 2: 0.3010, 
            4: 0.6020, 
            6: None, 
            8: 0.9030, 
            10: 1.0000, 
            12: 1.0792, 
            14: None, 
            16: 1.2041, 
            18: 1.2552, 
            20: None, 
            22: 1.3424} # Dicionario de valores (X) e (F(x))

def Lagrange(n):
    x = n
    x0 = n-4 
    x1 = n-2
    x2 = n+2

    L0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2)) #algoritmo de lagrange em python
    L1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    L2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))

    L0 = round(L0, 4) #arredondo os valores para aparecer apenas as 4 primeiras casas apos a virgula
    L1 = round(L1, 4)
    L2 = round(L2, 4) 

    f0 = Valores[x0] # Busca o F(x) do X nescessario
    f1 = Valores[x1]
    f2 = Valores[x2]

    pn0 = round(f0 * L0,4)
    pn1 = round(f1 * L1,4)
    pn2 = round(f2 * L2,4)

    SPn = pn0 + pn1 + pn2  # O polinomio é o somatorio de F(x) * Lagrange (x)
    SPn = round(SPn, 4)
    return SPn

print(Lagrange(6))
print(Lagrange(14)) 
print(Lagrange(20))