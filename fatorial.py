n=1
while n>=0:
    n = int(input("Digite o numero inteiro positivo que deseja fatorar: "))
    fatorial=1
    while n>1:
        fatorial=fatorial*n
        n=n-1
    print(fatorial)
