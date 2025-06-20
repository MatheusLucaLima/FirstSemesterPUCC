"""
    This is the original version of Report Card,
    It was created by a group of 3 students from PUC-Campinas,
    It is written in portuguese.
"""



lista_alunos = []

total_alunos = int(input("Digite a quantidade total de alunos a serem cadastrados: "))

aux = 0
alunos_superior5 = 0
maior_MF = -1
menor_MF = 11



while aux < total_alunos:

    aluno = []
    lista_T = []
    lista_P = []
    lista_M = []

    print(f"-------------Aluno{aux+1}-------------")

    nome = input("Digite o nome do aluno: ")

    T1 = -1
    while T1>10 or T1<0:
        T1 = float(input(f"Digite a nota da primeira prova teórica de {nome}: "))

    T2 = -1
    while T2>10 or T2<0:
        T2 = float(input(f"Digite a nota da segunda prova teórica de {nome}: "))

    P1 = -1
    while P1>10 or P1<0:
        P1 = float(input(f"Digite a nota do primeiro projeto  de {nome}: "))

    P2 = -1
    while P2>10 or P2<0:  
        P2 = float(input(f"Digite a nota do segundo projeto de {nome}: "))
    

    MP = (P1+P2)/2    

    MT = T1 *0.4 + T2*0.6  

    MF = 0.3*MP + 0.7*MT
    
    if MP <= 5 or MT <= 5:
        if MP < MT :
            MF = MP
        else:
            MF = MT
    if MF > 5:
        alunos_superior5 += 1
     

    aluno.append(nome)
    lista_T.append(T1)
    lista_T.append(T2)
    aluno.append(lista_T)

    lista_P.append(P1)
    lista_P.append(P2)
    aluno.append(lista_P)

    lista_M.append(MP)
    lista_M.append(MT)
    aluno.append(lista_M)
    aluno.append(MF)
    
    aux+=1
    lista_alunos.append(aluno)

aluno_maior = 0
aluno_menor = 0
i=0
while i < total_alunos: 
    if maior_MF < lista_alunos[i][4]:
            maior_MF = lista_alunos[i][4]
            aluno_maior = str(lista_alunos[i][0])
    if menor_MF > lista_alunos[i][4]:
            menor_MF = lista_alunos[i][4]
            aluno_menor = str(lista_alunos[i][0])
    i+=1

print("-------------Finalizado cadastro dos alunos-------------")

loop = 100
while loop != 0:
    print("\n\n-------------OPÇÕES DO SISTEMA-------------")
    print("0- Para sair")
    print("1- Boletim com o nome de cada aluno, sua Média Teórica(MT), Média Prática (MP) e Média Final (MF)")
    print("2- Digitar o nome do aluno e imprima todas as informações sobre ele")
    print("3- O nome do aluno com maior Média Final (MF)")
    print("4- O nome do aluno com menor Média Final (MF)")
    print("5- Percentual dos alunos com Média Final (MF) superior a 5.0")

    loop = int(input("Digite o número desejado: "))
    if loop < 0 or loop > 5:
        while loop < 0 or loop > 5:
            print("\n\n-------------OPÇÕES DO SISTEMA-------------")
            print("0- Para sair")
            print("1- Boletim com o nome de cada aluno, sua Média Teórica(MT), Média Prática (MP) e Média Final (MF)")
            print("2- Digitar o nome do aluno e imprima todas as informações sobre ele")
            print("3- O nome do aluno com maior Média Final (MF)")
            print("4- O nome do aluno com menor Média Final (MF)")
            print("5- Percentual dos alunos com Média Final (MF) superior a 5.0")
            print("Opção inválida")
            loop = int(input("Digite o número desejado: "))
    
    if loop == 1:
        print("\n-------------OPÇÃO 1-------------")
        i = 0
        while i < total_alunos:
            print(f"-------------Aluno {i+1}-------------")
            print(f"Nome: {lista_alunos[i][0]}")  
            print(f"Média teórica: {lista_alunos[i][3][0]:.2f}")  
            print(f"Média prática: {lista_alunos[i][3][1]:.2f}") 
            print(f"Média final: {lista_alunos[i][4]:.2f}")  
            print("\n")      
            i+=1
    elif loop == 2:
        print("\n-------------OPÇÃO 2-------------")
        auxnome = input("Digite o nome do aluno para saber todas as suas informações: ")
        i = 0
        aluno_encontrado = False
        while i < total_alunos:
            if auxnome == lista_alunos[i][0]:
                print(f"Nome do aluno : {lista_alunos[i][0]}")
                print(f"Nota T1 : {lista_alunos[i][1][0]}")
                print(f"Nota T2 : {lista_alunos[i][1][1]}")
                print(f"Nota P1 : {lista_alunos[i][2][0]}")
                print(f"Nota P2 : {lista_alunos[i][2][1]}")
                print(f"Média Trabalho : {lista_alunos[i][3][0]:.2f}")
                print(f"Média Projeto : {lista_alunos[i][3][1]:.2f}")
                print(f"Média Final : {lista_alunos[i][4]:.2f}")
            if auxnome == lista_alunos[i][0]:
                aluno_encontrado = True
            i+=1
        if aluno_encontrado == False:
            print("Aluno não encontrado")
            
            
    elif loop == 3:
        print("\n-------------OPÇÃO 3-------------")
        print(f"O nome do aluno com a maior média final é: {aluno_maior}")
    elif loop == 4:
        print("\n-------------OPÇÃO 4-------------")
        print(f"O nome do aluno com a menor média final é: {aluno_menor}")
    elif loop == 5:
        print("\n-------------OPÇÃO 5-------------")
        alunos_superior5 = alunos_superior5*100/total_alunos 
        print(f"O percentual de alunos com média superior a 5,0 é: {alunos_superior5:.0f}%")
