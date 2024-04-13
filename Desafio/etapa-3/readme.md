# Etapa 3 - Sprint 9

### A terceira etapa do desafio teve como objetivo pegar os dados, tanto em JSON quanto em CSV, da camada `Raw` do Data Lake s3 e realizar as modificações necessárias para que ele pudesse chegar na camada `Refined` de acordo com o modelo dimensional criado por cada um. Para isso foram necessárias `três etapas`:

## 1 - Processamento da Trusted

### Através do `Apache Spark` e do `AWS Glue`, criamos dois jobs, um para processar os dados em **JSON** da camada `Raw` e outro para processar os dados em format **CSV** na mesma camada, escrevendo os dados no formato **parquet** e enviando-os para a camada `Trusted` do Data Lake.

### [Script Spark arquivos JSON](./json_parquet.py)

### Screenshot job Spark para arquivos em JSON

## ![](./json_parquet.png)

### [Script Spark arquivos CSV](./csv_parquet.py)

### Screenshot job Spark para arquivos em CSV

![](./csv_parquet.png)

### Screenshot dados em parquet oriundos do CSV na camada Trusted

## ![](./camada_trusted.png)

### Screenshot dados em parquet oriundos da API TMDB na camada Trusted particionados por data de coleto

## ![](./arquivos_json_trusted.png)

### Screenshot query feita no arquivo em parquet dos dados oriundos do TMDB na camada Trusted

## ![](./query_json_Trusted.png)

### Screenshot query feita no arquivo em parquet dos dados oriundos do CSV na camada Trusted

## ![](./query_csv_Trusted.png)

## 2 - Modelagem de dados da Refined

### Essa etapa compreendeu a criação do modelo dimensional no qual os dados em parquet da camada `Trusted` seguirão. O modelo foi feito através da plataforma `draw.io` e contém todas as tabelas dimensão que serão necessárias para se ter uma melhor uma vizualização de cada filme da tabela `fato_filme` e as seus respectivos relacionamentos entre as tabelas sendo eles tanto de um para muitos quanto de muitos para muitos em alguns casos

### [Arquivo draw io do modelo dimensional](./modelagem.drawio)

### Visualização das tabelas dimensão e da tabela fato_filme

![](./modelo_dimensional.PNG)

## 3 - Processamento da Refined

### Para a última etapa utilizamos novamento o `Apache Spark` para criar as tabelas dimensão e a tabela fato através dos dados em parquet da camada `Trusted` e posteriormente salvar essas tabelas na camada `Refined` do Data Lake. Além da criação das tabelas, foi criado também um crawler através do serviço `AWS Glue Data Catalog` para que as tabelas na camada `Refined` fossem armazenadas em um banco de dados para posteriormente serem consultadas

### [Script Spark para criação das tabelas](./parquet_refined.py)

### Screenshot job Spark de criação das tabelas fato e dimensão

![](./parquet_refined.png)

### Screenshot tabelas no Data Lake s3 na camada Refined

![](./tabelas_s3_refined.png)

### Screenshot query dos dados da tabela fato_filme

![](./query_fato_filme.png)

### Screenshot do crawler utilizado para a criação das tabelas

![](./crawler.png)

### Screenshot das tabelas criadas pelo crawler no Glue Data Catalog

![](./data_catalog.png)
