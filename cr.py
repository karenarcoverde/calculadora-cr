#Programa cr.py
#Autora: Karen dos Anjos Arcoverde
#Data: 30/07/2019
#
#Programa que calcula o CR na UFRJ
#



##################### Funcoes #####################

def calculadora_cr (nota, credito, indice, lista_notas, lista_creditos):
    soma_creditos = 0
    soma_notas_ponderada = 0
    
    lista_notas.append (nota)
    lista_creditos.append (credito)
    
    for indice_crescente in range (0, indice + 1): 
            soma_notas_ponderada = float(soma_notas_ponderada) + float(lista_notas [indice_crescente]) * int(lista_creditos [indice_crescente])
            soma_creditos = soma_creditos + int(lista_creditos [indice_crescente])

    
    return float(soma_notas_ponderada / soma_creditos)




def calculadora_cr_alterada (indice, lista_notas, lista_creditos):
    soma_creditos = 0
    soma_notas_ponderada = 0
    
    for indice_crescente in range (0, indice): 
            soma_notas_ponderada = float(soma_notas_ponderada) + float(lista_notas [indice_crescente]) * int(lista_creditos [indice_crescente])
            soma_creditos = soma_creditos + int(lista_creditos [indice_crescente])

    
    return float(soma_notas_ponderada / soma_creditos)




def remover_materia (numero_materia, indice, lista_notas, lista_creditos):
      if (0 < numero_materia <= indice):
              del lista_notas [numero_materia - 1]
              del lista_creditos [numero_materia - 1]
              indice -= 1

      else:
              print('Essa matéria não existe. Verifique novamente o número da matéria digitado.')
              
      return indice


##################### Programa Principal #####################
def menu():
    indice = 0
    indice_tabela = 1
    opcao = 0
    nota = 0
    lista_notas = []
    lista_creditos = []
    alteracao_materia = 0
    nova_nota = 0
    
    while (opcao != 5):
            print()
            print()
            print ('######################################')
            print ('########### CALCULADORA CR ###########')
            print ('######################################')
            print ('OBS: AO TERMINAR DE DIGITAR AS NOTAS, DIGITE -1')
            print ('1. Adicionar nota, crédito e calcular CR')
            print ('2. Alterar nota e crédito')
            print ('3. Remover matéria')
            print ('4. Consultar Notas, Créditos e CR')
            print ('5. Sair')
            print()
            print()
            
            opcao = int(input())
    
            if (opcao == 1):
                while (nota != -1): 
                    print()
                    print('#############################')
                    print ('Nota', indice + 1)
                    nota = float(input('Nota: '))

                    if (nota != -1):
                                credito = int(input('Crédito: '))
                                if (credito <= 0):
                                        print ('Número de créditos inválido. Digite um número maior que zero.')
                                else:
                                        cr = calculadora_cr (nota, credito, indice, lista_notas, lista_creditos)
                                        print ('CR = ', cr)
                                        print('############################')
                                        indice += 1
                nota = 0
                                
            if (opcao == 2):
                    print('Digite para alterar: 1. Nota   2. Crédito')
                    alteracao_materia = input ()
                    numero_materia = int(input ('Digite o número da matéria: '))
                    
                    if (alteracao_materia == '1'):
                            nova_nota = float(input('Nova nota: '))
                            lista_notas [numero_materia - 1] = nova_nota
                            
                            cr = calculadora_cr_alterada (indice, lista_notas, lista_creditos)
                           
                            print ('Novo CR: ', cr)

                    if (alteracao_materia == '2'):
                            novo_credito = int(input('Novo crédito: '))
                            if (novo_credito <= 0):
                                        print ('Número de créditos inválido. Digite um número maior que zero.')
                            else:
                                    lista_creditos [numero_materia -1] = novo_credito
                                    cr = calculadora_cr_alterada (indice, lista_notas, lista_creditos)
                                    print ('Novo CR: ', cr)

    
            if (opcao == 3):
                    numero_materia = int(input('Número da matéria que deseja remover: '))
                    indice = remover_materia(numero_materia, indice, lista_notas, lista_creditos)
                    cr = calculadora_cr_alterada (indice, lista_notas, lista_creditos)
                    print ('Novo CR: ', cr)

                    
                    
            if (opcao == 4):
                print()
                print()
                print('---------------------------------------')
                print ("{:<15}{:<15}{}".format('Número','Nota','Crédito'))

                for indice_tabela in range (indice):
                    print ("{:<15}{:<15}{}".format(indice_tabela + 1, lista_notas [indice_tabela], lista_creditos [indice_tabela])) 
                    indice_tabela += 1
                    
                print('---------------------------------------')
                print ('CR: ', cr)
                print()
                print()


######## chamada ao menu
menu()
