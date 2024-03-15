# Resumo de estudo

# Evidências

## Tarefa 1

### Exercícios envolvendo a biblioteca Pandas, trabalhando com DataFrames

- [Notebook tarefa 1](./exercicios/tarefa%201/tarefa1.ipynb)

## Tarefa 2

### O objetivo dessa tarefa foi rodar um container Docker com Apache Spark e criar um contador de palavras através da Spark API

### Container rodando Spark e Jupyter através da imagem jupyter/all-spark-notebook

![](./evidencias/tarefa%202/docker.png)

### Código Spark responsável pelo contador de palavras rodando dentro do container

```Python
path = "/home/jovyan/work/README.md"
readme = spark.sparkContext.textFile(path)
contador = readme.flatMap(lambda p: p.split(" ")).countByValue()
for palavra, quantidade in contador.items():
    print(f"{palavra} -> {quantidade}")
```

![](./evidencias/tarefa%202/spark.png)

## Tarefa 3

### Exercícios com o intuito de aprender sobre AWS Glue, uma ferramenta de ETL

### Ex 1

### Script Spark para ler o arquivo csv do s3

![](./evidencias/tarefa%203/Glue_ex1_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex1_log.png)

### Ex 2

### Script Spark para mostrar qual o schema do DataFrame 'nomes'

![](./evidencias/tarefa%203/Glue_ex2_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex2_log.png)

### Ex 3

### Script Spark para transformar os valores da coluna nomes para uppercase

![](./evidencias/tarefa%203/Glue_ex3_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex3_log.png)

### Ex 4

### Script Spark para contar o número de linhas do DataFrame através do método count()

![](./evidencias/tarefa%203/Glue_ex4_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex4_log.png)

### Ex 5

### Script Spark para contar o número de nomes agrupando por sexo e ano com groupBy()

![](./evidencias/tarefa%203/Glue_ex5_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex5_log.png)

### Ex 6

### Script Spark para transformar a coluna 'total' em integer para que possa ser ordenada de forma decrescente e um script qque filtra a coluna sexo pelo termo 'F' para descobrir o nome feminino mais usado

![](./evidencias/tarefa%203/Glue_ex6_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex6_log.png)

### Ex 7

### Script Spark idêntico ao anterior porém procurando através do filtro de sexo pelo termo 'M'

![](./evidencias/tarefa%203/Glue_ex7_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex7_log.png)

### Ex 8

### Script Spark para mostrar o total de registros para cada ano usando groupBy() e uma função agregadora somando os totais

![](./evidencias/tarefa%203/Glue_ex8_script.png)

### Log do resultado

![](./evidencias/tarefa%203/Glue_ex8_log.png)

### Ex 9

### Script Spark para transformar a coluna 'nomes' em uppercase e criar partições do DataFrame baseado nas colunas 'sexo' e 'ano'

![](./evidencias/tarefa%203/Glue_ex9_script.png)

### Pastas contendo os arquivos JSON escritos no s3

![](./evidencias/tarefa%203/Glue_ex9_s3_folder1.png)
![](./evidencias/tarefa%203/Glue_ex9_s3_folder2.png)
![](./evidencias/tarefa%203/Glue_ex9_s3_folder3.png)

### Exercício Crawler

### O objetivo desse exercício é desenvolver um crawler para criar uma tabela automaticamente a partir de dados escritos no s3

![](./evidencias/tarefa%203/Glue_crawler.png)

### Tabela criada no banco de dados glue-lab

![](./evidencias/tarefa%203/Glue_crawler_table.png)

# Certificados

### Learn By Example: Hadoop, MapReduce for Big Data problems

![](./certificados/Hadoop.jpg)

### Formação Spark com Pyspark : o Curso Completo

![](./certificados/Spark.jpg)
