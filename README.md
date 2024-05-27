### Uso do script
```
python main.py > sql.txt
```

### Documentação Script-SQL-Superset

A apresentação dos dados de um dataset foi um dos problemas reencontrados na exploração do Superset. Na implementação antiga do site do LDE, a equipe de front-end foi responsável pela escrita de todos os "CASE WHEN's" necessários para a transformação correta dos dados provenientes do banco. Tome como exemplo a coluna COD_CAPITAL:

|Tipo| Descricao                     |
|----| ----------------------------- |
| 11 | Município de Porto Velho (RO) |
| 12 | Município de Rio Branco (AC)  |
| 13 | Município de Manaus (AM)      |
| 14 | Município de Boa Vista (RR)   |
| 15 | Município de Belém (PA)       |
| 16 | Município de Macapá (AP)      |
| 17 | Município de Palmas (TO)      |
| 21 | Município de São Luís (MA)    |
| 22 | Município de Teresina (PI)    |
| 23 | Município de Fortaleza (CE)   |
| 24 | Município de Natal (RN)       |
| 25 | Município de João Pessoa (PB) |
| 26 | Município de Recife (PE)      |
| 27 | Município de Maceió (AL)      |
| 28 | Município de Aracaju (SE)     |
| 29 | Município de Salvador (BA)    |
| 31 | Município de Belo Horizonte (MG) |
| 32 | Município de Vitória (ES)     |
| 33 | Município de Rio de Janeiro (RJ) |
| 35 | Município de São Paulo (SP)   |
| 41 | Município de Curitiba (PR)    |
| 42 | Município de Florianópolis (SC) |
| 43 | Município de Porto Alegre (RS) |
| 50 | Município de Campo Grande (MS) |
| 51 | Município de Cuiabá (MT)      |
| 52 | Município de Goiânia (GO)     |
| 53 | Município de Brasília (DF)    |

Nesse caso, será necessário fazer um CASE WHEN para cada tipo encontrado, um trabalho extensivo e desnecessário. Por isso, foi feito o script acima, que utiliza a planilha de pareamento.

>  OBS.: o arquivo "pnad_novo.csv" é um arquivo proveniente do hotmapper (em mapping_protocols). Não é estritamente necessário, porém o utilizamos para o nomeamento das colunas transformadas. Como no exemplo acima:
>
>```
>END AS cod_cap_format
>```
>Onde cod_cap é o nome da variável COD_CAPITAL no banco.

## Mas e as variáveis transformadas?
Para as variáveis transformadas, é um pouco mais complicado. Em um primeiro momento, é necessário saber se essas variáveis já foram computadas no banco, pois seus valores provém de outros CASE WHEN's, realizados pelo time de banco de dados.

Depois disso, num processo manual, verifica-se as notas técnicas uma a uma para entender qual transformação de valores é necessária ser feita.

Para que o script pudesse atender as variáveis transformadas, foi necessário preencher uma outra planilha (parecida com o de pareamento) com as informações descritas na nota técnica. Nossa planilha está como "pnad_transformadas.csv".

Com isso, seria interessante que as variáveis transformadas pudessem ser integradas a um documento só, com destaque para planilhas. Assim, nosso trabalho com a visualização dos dados se torna mais fácil, com o uso continuado do script.