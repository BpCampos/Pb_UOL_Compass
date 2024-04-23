# Etapa 4 - Sprint 10

### O objetivo desta etapa final é pegar os dados que estão em um banco de dados através do `AWS Athena` e trazer as tabelas para o `QuickSight`, fazendo os relacionamentos necessários para que possamos montor o dashboard com os dados dos filmes.

### Tabelas dimensão e fato trazidas para o `QuickSight` através do `AWS Athena`

## ![](./tables.png)

### O próximo passo é, dentro da tabela fato, criar as relações entre a fato e as dimensões

![](./relationships.png)

### Com os dados já prontos e as relações criadas, podemos montar o dashboard usando as informações dos conjuntos de dados

### [PDF do Dashboard](./Dashboard_2024-04-23T18_41_00.pdf)

### Para o dashboard do desafio eu utilizei as informações de **países produtores** para criar uma função que me retornasse todos os continentes do mundo para que eu pudesse filtrar os dados posteriormente tanto por país quanto por continente, além de filtrar pelos gêneros `drama` e `romance` que eu escolhi trabalhar

### Função continente que separa todos os países presentes na dimensão paises produtores em seus respectivos continentes

![](./campo_continente.png)

### Visual final do dashboard mostrando o continente América

![](./dashboard_final.png)

### Versão do dashboard mostrando o continente Ásia para demonstrar a mudança de valores ao alterar o campo continente e o campo gênero para romance

![](./dashboard_final_asia.png)
