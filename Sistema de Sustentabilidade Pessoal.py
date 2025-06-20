"""
    Final version of the greatest project from the first semester.
    Dveloped by a group of 6 students.
    Written in Portuguese, I have another version available in English with some changes
    and developed only by myself.
    This code has a documantation written in portuguese.
"""


import numpy as np
import mysql.connector
import os
Menu=True

#Change it to work properly
conexao = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database=""
)
cursor = conexao.cursor()

cursor.execute("""
create table if not exists Alunos(
    id_Pesoa int primary key auto_increment,
    data date,
    nome_ varchar(100) unique,
    Cons_agua int,Cons_energia int,
    residuos int,
    reciclado int,
    transporte varchar(50)
)   
""")
cursor.execute("""
create table if not exists Clas(
    id_Clas int primary key auto_increment,
    id_aluno int,
    nome varchar(50),
    C_Cons_Agua varchar(50),
    C_energia varchar(50),
    C_reciclado varchar(50),
    c_transporte varchar(50),
    CONSTRAINT fk_id_aluno FOREIGN KEY (id_aluno) REFERENCES Alunos(id_Pesoa),
    CONSTRAINT fk_nome_aluno FOREIGN KEY (nome) REFERENCES Alunos(nome_)
)
""")
# Matriz 2x2 escolhida
key = np.array([[9, 3],[2, 1]])

def texto_para_numeros(texto): # Função 1 de transformar letra para numero.
    """
        no if se encontrar a letra z ele transforma em 0.
        no else [ord(letra)] retorna o codigo unicode da letra, subitrai por 97.
        Para que assim a=1,b=2,c=3,...y=0, transformando o texto em numero.
    """
    letra_transformado_numero = []
    for letra in texto:
        if letra=='z':
            letra_transformado_numero.append(0)
        else:
            letra_transformado_numero.append((ord(letra)+1) - ord('a'))
    return letra_transformado_numero

def numeros_para_texto(letra_transformado_numero): # Função 2 de trasnformar numero para letra.
    """
        no if se encontrar o numero 0 ele transforma em z.
        no else (ord('a')-1) retorna o codigo unicode da letra, somando por 96.
        Para que assim a=97,b=98,c=99,...y=0, transformando os numeros em texto.
    """
    numero_transformado_em_letra = ''
    for numero in letra_transformado_numero:
        if numero == 0:
            numero_transformado_em_letra += 'z'
        else:
            numero_transformado_em_letra += chr(numero+ (ord('a')-1))
    return numero_transformado_em_letra


def transformar_em_blocos(texto, tamanho_bloco): # Função 3 de transformar os numeros (letra convertidos para numeros) em matriz
    """
    Converter o texto em numeros utilizando a função 1
    Coloca 0 (ou a letra z) se o numero de letra (que foram convertidos em numero) for impar 
    Separa em blocos de tamanho 2
    """
    matriz_2x1 = []
    numeros = texto_para_numeros(texto)
    if len(numeros) % 2 != 0:
        numeros.append(0)
    for i in range(0, len(numeros), 2):
        matriz_2x1.append(numeros[i:i+2])
    return matriz_2x1


def criptografar(texto, key): # Função 4 utilizar todas as funções anteriores para criptografar o texto de imput (utilizamos a cifra de hill para isso)
    """
    Converte os numeros em blocos, utilizando a função 3
    transforma os blocos de numeros 1x2 em 2x1 para ser possivel a multiplicação com a chave 2x2
    multiplica pela matriz 2x2 chave e aplica o modulo de 26 para encontrar seu respectivo numero
    adiciona os numeros resultantes do modulo de 26 ao dicionario "Resultado" ja transformados em matriz 1x2
    Converte os numeros criptografados de matriz 1x2 em letras utilizando a função 2

    """
    blocos = transformar_em_blocos(texto, 2)  
    resultado = []
    for i in blocos:
        vetor_descriptografado = np.array(i).reshape(-1,1)
        vetor_transformado = key.dot(vetor_descriptografado) % 26
        resultado.extend(vetor_transformado.flatten())
    return numeros_para_texto(resultado)
#------------------------------------------------------------------------------------------------------------------
inversos_mod26 = { # Biblioteca com os inversos dos numeros em modulo 26
    1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23,
    19: 11, 21: 5, 23: 17, 25: 25
}
def matriz_inversa_mod26(matriz):
    """
    Função para descobrir o inverso da matriz chave (necessaria para encontrar o texto descriptografado)
    utilizando a regra do [d, -b];[-c, a] pelo mod de 26
    """
    a, b = matriz[0, 0], matriz[0, 1]
    c, d = matriz[1, 0], matriz[1, 1]
    det = (a * d - b * c) % 26
    det_inv = inversos_mod26.get(det)
    adj = np.array([[d, -b], [-c, a]]) % 26
    inversa = (det_inv * adj) % 26
    return inversa
def descriptografar(texto_criptografado, chave):
    """
    Função da descriptografia
    Calcula a matriz inversa da chave
    Transforma em blocos
    Multiplica pela matriz inversa encontrado na parte acima e aplica o modulo 26
    Coloca tudo em uma lista
    Utiliza a função de converter os numeros encontrados em letras
    """
    chave_inv = matriz_inversa_mod26(chave)
    blocos = transformar_em_blocos(texto_criptografado, 2)
    resultado = []
    for i in blocos:
        vetor = np.array(i).reshape(-1,1)
        vetor_descriptografado = chave_inv.dot(vetor) % 26
        resultado.extend(vetor_descriptografado.flatten())
    return numeros_para_texto(resultado)

while Menu==True:
    os.system("cls")
    print(f"\n\n\t\t\t  => Sistema de Sustentabilidade!!! <=")
    print(f"\n\n\t\t1-Adicionar dados")
    print(f"\n\t\t2-Ler Tabela Geral Dados")
    print(f"\n\t\t3-Ler Tabela com a Classificação dos Dados dos Usuários")
    print(f"\n\t\t4-Atualizar Dados de Usuário Existente")
    print(f"\n\t\t5-Apagar Dados de Usuário Existente")
    print(f"\n\t\t6-Ler Tabela com Média Geral e Suas Classificações")
    print(f"\n\t\t7-Sair do Sistema de Sustentabilidade")
    resposta_menu=int(input(f"\n\n\t\t\tDigite a opção escolhida: "))
    if resposta_menu==1:
        agua=""
        energia=""
        rec=""
        sustentavel=0
        n_sustentavel=0
        os.system("cls")
        print(f"\n\n\t\t\t  => Sistema De Sustentabilidade!!! <=")
        dia=input(f"\n\n\t\tDigite a data atual no modelo (ANO/MÊS/DIA): ")
        nome=input(f"\n\t\tDigite o nome: ")
        cons_agua=float(input(f"\n\t\tDigite o consumo de água: "))
        cons_energia=float(input(f"\n\t\tDigite o consumo de energia: "))
        residuos=float(input(f"\n\t\tDigite os resíduos: "))
        reciclado=float(input(f"\n\t\tDigite o reciclado: "))
        print(f"\t\t\n\nS = Sim e N = Não")
        publico=input(f"\n\t\tTransporte Público (ônibus, metrô, trem) => ")
        bike=input(f"\n\t\tBicicleta => ")
        caminhada=input(f"\n\t\tCaminhada => ")
        carro=input(f"\n\t\tCarro (Combustíveis Fósseis) => ")
        carro_e=input(f"\n\t\tCarro Elétrico => ")
        carona=input(f"\n\t\tCarona Compartilhada (Fósseis) => ")
        if publico=="S":
            sustentavel+=1
        if bike=="S":
            sustentavel+=1
        if caminhada=="S":
            sustentavel+=1
        if carro_e=="S":
            sustentavel+=1
        if carro=="S":
            n_sustentavel+=1
        if carona=="S":
            n_sustentavel+=1
        if sustentavel!=0 and n_sustentavel==0:
            transporte="alta"
        else:
            if n_sustentavel!=0 and sustentavel==0:
                transporte="baixa"
            else:
                transporte="moderada"
        criptografado = criptografar(transporte, key)
            
        cursor.execute("""

        insert into Alunos(
            data,
            nome_,
            Cons_agua,
            Cons_energia,
            residuos,
            reciclado,
            transporte
        )values(%s,%s, %s, %s, %s, %s, %s) 
        """, (dia,nome, cons_agua, cons_energia, residuos, reciclado, criptografado))
        conexao.commit()
        if cons_agua<150:
            agua="alta"
        else:
            if 150<=cons_agua<=200:
                agua="moderada"
            else:
                agua="baixa"
        if cons_energia<5:
            energia="alta"
        else:
            if 5<=cons_energia<=10:
                energia="moderada"
            else:
                energia="baixa"
        if reciclado>50:
            rec="alta"
        else:
            if 20<=reciclado<=50:
                rec="moderada"
            else:
                rec="baixa"
        criptografado_agua=criptografar(agua, key)
        criptografado_energia=criptografar(energia, key)
        criptografado_rec=criptografar(rec, key)
        criptografado_transporte=criptografar(transporte, key)
        cursor.execute("""SELECT id_Pesoa FROM Alunos WHERE nome_ = %s""", (nome,))
        id_aluno=cursor.fetchone()[0]
        cursor.execute("""
            insert into Clas(
                id_aluno,
                nome,
                C_Cons_Agua,
                C_energia,
                C_reciclado,
                c_transporte
            )values(%s,%s,%s, %s, %s,%s) 
                """, (id_aluno, nome, criptografado_agua, criptografado_energia, criptografado_rec, criptografado_transporte))
        conexao.commit()
    else:
        if resposta_menu==2:
            os.system("cls")
            print(f"\n\n\n\t\t\t  => Sistema de Sustentabilidade!!! <=")
            cursor.execute("""select * from Alunos""")
            Alunos=cursor.fetchall()
            for i in Alunos:
                x=descriptografar(i[7], key)
                print(f"\n\t| Id: {i[0]} | Data: {i[1]} | Nome: {i[2]} | Consumo de Água: {i[3]} | Consumo de Energia: {i[4]} | Qnt. Residuos: {i[5]} | % Reclicado: {i[6]}% | Clas. Trans.: {x} |")
            input(f"\n\n                            <<<   TECLE ALGO   >>> ")
        else:
            if resposta_menu==3:
                os.system("cls")
                print(f"\n\n\t\t\t  => Sistema de Sustentabilidade!!! <=")
                cursor.execute("""SELECT * FROM Clas""")
                Clasificados=cursor.fetchall()
                for i in (Clasificados):
                    agua=descriptografar(i[3], key)
                    energia=descriptografar(i[4], key)
                    rec=descriptografar(i[5], key)
                    trans=descriptografar(i[6], key)
                    print(f"\n\t| Id: {i[0]} | Id Pessoa: {i[1]} | Nome: {i[2]} | Clas. Cons. Água: {agua} | Clas. Cons. Energia: {energia} | Clas. % Res. Reciclados: {rec} | Clas. Trans.: {trans} |")
                input(f"\n\n                            <<<   TECLE ALGO   >>> ")
            else:
                if resposta_menu==4:
                    sustentavel=0
                    n_sustentavel=0
                    agua=""
                    energia=""
                    rec=""
                    os.system("cls")
                    print(f"\n\n\t\t\t  => Sistema de Sustentabilidade!!! <=")
                    pesq_nome=input(f"\n\n\t\tDigite o Nome do Usuário que Deseja Alterar os Dados: ")
                    os.system("cls")
                    print(f"\n\n\t\t\t  => Sistema de Sustentabilidade!!! <=")
                    cursor.execute("""select * from Alunos where nome_=%s""",(pesq_nome,))
                    aluno = cursor.fetchone()
                    dia=input(f"\n\n\t\tDigite a data atual: ")
                    nome=input(f"\n\t\tDigite o nome: ")
                    cons_agua=float(input(f"\n\t\tDigite o consumo de água: "))
                    cons_energia=float(input(f"\n\t\tDigite o consumo de energia: "))
                    residuos=float(input(f"\n\t\tDigite os resíduos: "))
                    reciclado=float(input(f"\n\t\tDigite o reciclado: "))
                    print(f"\t\t\n\nS = Sim e N = Não")
                    publico=input(f"\n\tTransporte Público (ônibus, metrô, trem) => ")
                    bike=input(f"\tBicicleta => ")
                    caminhada=input(f"\tCaminhada => ")
                    carro=input(f"\tCarro (Combustível fósseis) => ")
                    carro_e=input(f"\tCarro Elétrico => ")
                    carona=input(f"\tCarona Compartilhada (Fósseis) => ")
                    if publico=="S":
                        sustentavel+=1
                    if bike=="S":
                        sustentavel+=1
                    if caminhada=="S":
                        sustentavel+=1
                    if carro_e=="S":
                        sustentavel+=1
                    if carro=="S":
                        n_sustentavel+=1
                    if carona=="S":
                        n_sustentavel+=1
                    if sustentavel!=0 and n_sustentavel==0:
                        transporte="alta"
                    else:
                        if n_sustentavel!=0 and sustentavel==0:
                            transporte="baixa"
                        else:
                            transporte="moderada"
                    if cons_agua<150:
                        agua="alta"
                    else:
                        if 150<=cons_agua<=200:
                            agua="moderada"
                        else:
                            agua="baixa"
                    if cons_energia<5:
                        energia="alta"
                    else:
                        if 5<=cons_energia<=10:
                            energia="moderada"
                        else:
                            energia="baixa"
                    if reciclado>50:
                        rec="alta"
                    else:
                        if 20<=reciclado<=50:
                            rec="moderada"
                        else:
                            rec="baixa"
                    criptografado_agua=criptografar(agua, key)
                    criptografado_energia=criptografar(energia, key)
                    criptografado_rec=criptografar(rec, key)
                    criptografado_transporte=criptografar(transporte, key)
                    cursor.execute("DELETE FROM Clas WHERE nome = %s", (pesq_nome,))
                    cursor.execute("""
                        UPDATE Alunos SET
                            data=%s,
                            nome_=%s,
                            Cons_agua=%s,
                            Cons_energia=%s,
                            residuos=%s,
                            reciclado=%s,
                            transporte=%s
                        WHERE nome_=%s
                    """, (dia,nome, cons_agua, cons_energia, residuos, reciclado, criptografado_transporte, pesq_nome))
                    cursor.execute("""SELECT id_Pesoa FROM Alunos WHERE nome_ = %s""", (nome,))
                    id_aluno=cursor.fetchone()[0]
                    cursor.execute("""
                        insert into Clas(
                            id_aluno,
                            nome,
                            C_Cons_Agua,
                            C_energia,
                            C_reciclado,
                            c_transporte
                        )values(%s,%s,%s,%s, %s,%s) 
                            """, (id_aluno, nome, criptografado_agua, criptografado_energia, criptografado_rec, criptografado_transporte))
                    conexao.commit()
                else:
                    if resposta_menu==5:
                        os.system("cls")
                        print(f"\n\n\t\t\t  => Sistema De Sustentabilidade!!! <=")
                        pesq_nome=input(f"\n\n\t\tDigite o Nome do Usuário que Desejar Apagar do Banco de Dados: ")
                        cursor.execute("""DELETE FROM Clas WHERE nome = %s""", (pesq_nome,))
                        cursor.execute("""delete from Alunos where nome_=%s""",(pesq_nome,))
                        conexao.commit()
                    else:
                        if resposta_menu==6:
                            t_clasificacao=0
                            t_clasificacao_ruim=0
                            t_clas=""
                            cursor.execute("""SELECT avg(Cons_agua) from Alunos""")
                            media_agua=cursor.fetchone()[0]
                            if media_agua<150:
                                c_media_agua="Alta Sus."
                            else:
                                if 150<=media_agua<=200:
                                    c_media_agua="Mod. Sus."
                                else:
                                    c_media_agua="Baixa Sus."
                            cursor.execute("""SELECT avg(reciclado) from Alunos""")
                            media_rec=cursor.fetchone()[0]
                            if media_rec>50:
                                c_media_rec="Alta Sus."
                            else:
                                if 20<=media_rec<=50:
                                    c_media_rec="Mod. Sus."
                                else:
                                    c_media_rec="Baixa Sus."
                            cursor.execute("""SELECT avg(Cons_energia) from Alunos""")
                            media_energia=cursor.fetchone()[0]
                            if media_energia<5:
                                c_media_energia="Alta Sus."
                            else:
                                if 5<=media_energia<=10:
                                    c_media_energia="Mod. Sus."
                                else:
                                    c_media_energia="Baixa Sus."
                            cursor.execute("""select transporte FROM Alunos""")
                            tipo=cursor.fetchall()
                            for i in tipo:
                                transporte=descriptografar(i[0], key)

                                if transporte=='alta':
                                    t_clasificacao+=1
                                else:
                                    if transporte=='baixa':
                                        t_clasificacao_ruim+=1
                                    else:
                                        t_clasificacao+=1
                                        t_clasificacao_ruim+=1
                            if t_clasificacao!=0 and t_clasificacao_ruim==0:
                                t_clas="Alta Sus."
                            else:
                                if t_clasificacao!=0 and t_clasificacao_ruim!=0:
                                    t_clas="Mod Sus."
                                else:
                                    if t_clasificacao==0 and t_clasificacao_ruim!=0:
                                        t_clas="Baixa Sus."
                            os.system("cls")
                            print(f"\n\n\t\t\t  => Sistema de Sustentabilidade!!! <=")
                            print(f"\n\n\t\tA Média Geral de Consumo de Água Foi: {media_agua} e Sua Classificação Foi de => {c_media_agua}")
                            print(f"\n\n\t\tA Média Geral de Consumo de Energia Foi: {media_energia} e Sua Classificação Foi de => {c_media_energia}")
                            print(f"\n\n\t\tA Média Geral da % de Lixo Reciclado Foi: {media_rec}% e Sua Classificação Foi de => {c_media_rec}")
                            print(f"\n\n\t\tA Média Geral do Tipo de Transporte Classificado Foi: {t_clas}")
                            input(f"\n\n                            <<<   TECLE ALGO   >>> ")
                        else:
                            if resposta_menu==7:
                                Menu=False
                            else:
                                print(f"\n\n\t\tDígito Invalido!!!")
                                input(f"\n\n                            <<<   TECLE ALGO   >>> ")
os.system("cls")
print(f"\n\n\t\t\t  => Sistema De Sustentabilidade!!! <=")
print(f"\n\n\t\t\t  => Obrigado Por Utilizar!!! <=")