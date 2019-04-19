def oculos(o1, o2, c1, c2):
    print('valores maximo: de 0 até 15 para Esferico')
    print('valores maximo: de 0 até 5 para Cilindrico')
    if (o1 >= 3 and o1 <= 12 and o2 >= 3 and o2 <= 12 and c1==0 and c2 == 0):
        print('\nPrime')
    elif (o1 >= 3 and o1 <= 10 and o2 >= 3 and o2 <= 10 and c1 <= 2 and c2 <= 2):
        print('\nPrime')
    elif(o1 >= 0 and o1 <= 15 and o2 >= 0 and o2 <= 15 and c1 <= 5 and c2 <= 5):
        print('\nVision')   
    elif(o1 >= 16 or o2 >= 16  or c1 >= 6 or c2 >= 6):
        print('\nNossas lentes nao suportam o seu grau')

print("===========================================")
oculos(5, 6, 0, 3)
