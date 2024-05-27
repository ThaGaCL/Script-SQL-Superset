import csv

def iterarPareamento(pareamento, map_bd):
    # Itera sobre o arquivo
    i = 0
    while i < len(pareamento):
        row = pareamento[i]
        
        if row[0]:  # Verifica se a primeira coluna não está vazia
            title = row[0]  # Nome da variável da PNAD
            title_bd = title # Nome da variável no banco de dados

            # Busca o nome da variável no banco de dados
            for row_bd in map_bd:
                if row_bd[0] == title:
                    title_bd = row_bd[3]
                    break

            print(f"CASE WHEN {title} = '{row[4]}' THEN '{row[5]}'") # Imprime o cabeçalho do CASE
            
            i += 1
            # Procede a imprimir os WHENs enquanto a variável da PNAD for a mesma
            while i < len(pareamento) and pareamento[i][0] == '':
                next_row = pareamento[i]
                print(f"    WHEN {title} = '{next_row[4]}' THEN '{next_row[5]}'")
                i += 1

            print(f"END AS {title_bd}_format" + ("," if i < len(pareamento) else ""))
        else: # Se a primeira coluna estiver vazia, pula para a próxima linha
            i += 1



# Abre o arquivo de pareamento, o arquivo de mapeamento e o arquivo de transformações
with open('pareamento_PNAD.csv', newline='', encoding='utf-8') as file, \
     open('pnad_novo.csv', newline='', encoding='utf-8') as file_bd, \
     open('pnad_transformadas.csv', newline='', encoding='utf-8') as file_trans:
    
    # Converte para lista para permitir reiterações
    pareamento = list(csv.reader(file))
    map_bd = list(csv.reader(file_bd))  
    pareamento_trans = list(csv.reader(file_trans))

    # Pula os cabeçalhos
    pareamento = pareamento[5:]
    map_bd = map_bd[1:]
    pareamento_trans = pareamento_trans[1:]

    
    iterarPareamento(pareamento, map_bd)
    print(',')
    iterarPareamento(pareamento_trans, map_bd)