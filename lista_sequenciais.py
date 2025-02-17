from pprint import pprint

def encontrar_sequencias_repetidas(a):
    
    listadup = []
    numrepetidos = []
    parada = False
    listatupla = []
    tupla_em_lista = []
    sequencias_e_posicoes = {}
    posicoes_dict = []

    for tam in range(len(a) - 1, 1, -1): # ler o tamanho da lista
        seqtam = len(a) - tam
        seqtam2 = tam
        listadup.append(a[0:tam])
        seq = 0
        
        for i in range(seqtam): # vai diminuindo o tamanho da lista até chegar no tamanho minimo 2 de sequencia
            indice = i + 1
            seq += 1
            seqtam2 += 1
            listadup.append(a[seq:seqtam2])
        
        for i in range(len(listadup)): 
            for j in range(i + 1, len(listadup)):
                if listadup[i] == listadup[j]: # compara lista por lista,  se achar lista iguais, da um append em numerepetidos
                    numrepetidos.append(listadup[i])
                    parada = True # variavel para parar o for, para assim ter a maiors sequencia, assim descartando as menores
                    
        if parada == True: # if de parada
            break
            
        listadup.clear()
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    if numrepetidos: # achar a posição das listas repetidas

        for c in range(len(numrepetidos)): # remover os numeros repetidos usando set
            tupla = tuple(numrepetidos[c])
            listatupla.append(tupla)

        tuplas = tuple(listatupla)
        excluir_repetidas = (set(tuplas))

        for g in excluir_repetidas:
            transformar_em_lista = list(g)   
            tupla_em_lista.append(transformar_em_lista) 
            
        for sequencias in tupla_em_lista:
            sequecnias2 = len(sequencias)
            contador_de_sequencias = 0

            posicoes_dict.clear()
            for tam_lista_original in range(len(a)):
                posicoes = (a[tam_lista_original:sequecnias2])
                sequecnias2 += 1

                lista_em_tupla = ()
                
                
                if posicoes == sequencias:
                    
                    lista_em_tupla = tuple(posicoes)
                    posicoes_dict.append(tam_lista_original)
                    sequencias_e_posicoes[lista_em_tupla] = posicoes_dict.copy()
                    

                    # sequencias_e_posicoes[lista_em_tupla] = posicoes_dict
                contador_de_sequencias += 1
                if len(a[tam_lista_original:sequecnias2]) < len(sequencias) + 1:
                    break

        for tam_lista_original, valores in sequencias_e_posicoes.items():
            print(f'Sequencias: {list(tam_lista_original)} | Posições: {valores}')

    else: # se não achar nenhuma lista repetida, retorna o print
        print('Nenhuma sequencia repetida na lista')
    

a = [7, 9, 5, 4, 3, 8, 10, 5, 4, 3, 99, 5, 4, 99, 3, 8, 10]

resultado = encontrar_sequencias_repetidas(a)
