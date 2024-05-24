import csv

# Abre os arquivos de pareamento e do banco de dados
with open('pareamento_PNAD.csv', newline='', encoding='utf-8') as file, \
     open('pnad_novo.csv', newline='', encoding='utf-8') as file_bd:
    
    pareamento = list(csv.reader(file))
    map_bd = list(csv.reader(file_bd))  # Converte para lista para permitir reiterações

    # Pula os cabeçalhos
    pareamento = pareamento[1:]
    map_bd = map_bd[1:]

    # Itera sobre o arquivo de pareamento
    
    i = 0
    while i < len(pareamento):
        row = pareamento[i]
        
        if row[0]:  # Verifica se a primeira coluna não está vazia
            title = row[0]  # Nome da variável da PNAD
            title_bd = title

            # Pesquisa o nome da variável no banco de dados
            for row_bd in map_bd:
                if row_bd[0] == title:
                    title_bd = row_bd[3]
                    break

            print(f"CASE WHEN {title} = '{row[4]}' THEN '{row[5]}'")
            
            i += 1
            while i < len(pareamento) and pareamento[i][0] == '':
                next_row = pareamento[i]
                print(f"    WHEN {title} = '{next_row[4]}' THEN '{next_row[5]}'")
                i += 1

            print(f"END AS {title_bd}_format" + ("," if i < len(pareamento) else ""))
        else:
            i += 1
