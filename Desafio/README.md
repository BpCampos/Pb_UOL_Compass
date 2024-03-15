# Etapas

## Etapa 1

#### O primeiro desafio da etapa 1 foi criar o script python que será executado pelo container Docker. O script se utiliza da biblioteca boto3 para ter acesso aos recursos da AWS, através de chaves de acesso vinculadas à conta o método client() da biblioteca

### [Script Python](./etapa-1/desafio_pt1.py)

#### Após criado o script Python, o próximo passo é construir uma imagem de Python a partir de um Dockerfile para executar o script. Em seguida será criado o container com um volume para armazenar os arquivos csv necessários

### [Dockerfile Desafio](./etapa-1/Dockerfile)

#### Ao rodar o container, os arquivos `movies.csv` e `series.csv` serão enviados ao bucket s3 e alocados nas respectivas subpastas pelo caminho informado no script Python

### Print do arquivo movies.csv no bucket s3 no caminho: desafiofinalcompass/Raw/local/CSV/Movies/2024/03/15/

![](./etapa-1/movies_csv.png)

### Print do arquivo series.csv no bucket s3 no caminho: desafiofinalcompass/Raw/local/CSV/Series/2024/03/15/

![](./etapa-1/series_csv.png)
