# Big Data

## Seção 2 - O que é Big Data

- Coleção de conjuntos de dados, grandes e complexos, que não podem ser processados por banco de dados ou aplicações de processamento tradicionais
- Volume gigantesco de dados
- 90% dos dados gerados no planeta são de até 2 anos
- A humanidade gerou 300 Exabytes de dados no últimos 5 anos
- Necessita de ferramentas preparadas para lidar com tanto dado para que as informações contidas nos dados possam ser extraídas
- No mundo do Big Data não temos de nos fixar na causalidade; podemos descobrir padrões e correlações nos dados que nos propiciem novas e valiosas ideias

### 4 V’s do Big Data

- `Velocidade` → Como os dados são gerados e velocidade na qual eles são gerados, exemplo: posts em uma rede social
- `Volume` → Altos volumes de dados, vindos de diversos lugares diferentes
- `Variedade` → Formato dos dados, seja vídeos, áudios, imagem, entre outros
- `Veracidade` → Confiabilidade dos dados, não podem ser dados aleatórios e sem sentido

### Números do Big Data

- Espera-se que `40 Zettabytes` de dados sejam criados no mundo por ano
- Cerca de `2.5 Quintilhões` de dados são criados por dia
- Mais de `4 bilhões` de horas por mês são usadas para assistir vídeos no YouTube
- `30 bilhões` de imagens são publicadas por mês no Facebook
- `1 Terabyte` de informação é criada durante uma única sessão da bolsa de valores americana
- Estima-se que `3.1 trilhões` de dólares por ano sejam desperdiçados por conta de problemas de qualidade dos dados

### Big Data x Ciência de dados

- Ciência de dados é um conjunto de técnicas para análise de dados, gerados pelo `Big Data` por exemplo
- Ao aplicar Ciência de dados ao Big Data extraímos valor e temos assim `Big Data Analytics`

## Seção 3 - Sistemas de armazenamento de dados

### O “V” de volume

- `3 perguntas` para saber se a empresa tem condição de trabalhar com Big Data
  - Como vamos armazenar grandes conjuntos de dados?
  - Como vamos acessar esses grandes conjuntos de dados?
  - Precisamos realmente armazenar tudo?
- **Armazenamento tem custo**

### Como armazenar ?

- Em linhas gerais, o armazenamento pode ser feito com base na seguinte **regra**:
  - Os dados podem ser estruturados ou podem ser estruturados antes do armazenamento? Caso sim, usamos um `Data Warehouse`
  - Os dados não são estruturados ou não podem ser estruturados? Caso sim, usamos um `Data Lake` ou `Data Store`
- Vamos usar cada formato de armazenamento de acordo também com a demanda da empresa
- Podemos usar Bancos de Dados Não Relacionais para construir `Data Lakes` e `Data Stores`

### Data Warehouse

- É um sistema de armazenamento que conecta e harmoniza grandes quantidades de dados de muitas fontes diferentes
- Necessita de um `schema` para saber como os dados serão armazenados
- Utilizamos o processo `ETL` para `Extrair Transformar e Carregar(Loading)` os dados das fontes e mandar para um `Banco de Dados Relacional`, para depois usar ferramentas de tratamento de dados e enviar esses dados onde melhor os convém
- Seu objetivo é alimentar a inteligência de negócios, relatórios e análises e oferecer suporte aos requisitos de negócio, para que as empresas possam tomar decisões baseadas em dados
- **Data Sources → Data Warehouse → Final destination**
- O `Schema` do banco de dados deve ser definido antes do processo de armazenamento de dados
- `DW` podem também lidar com dados não estruturados, por mais que os `DL(Data Lakes)` sejam mais recomendados

### Benefícios do DW

- `Melhor análise de negócios` → É possível agora tomar decisões com base em dados concretos
- `Consultas mais rápidas` → Com um `DW`, você pode consultar rapidamente grandes quantidades de dados consolidados
- `Melhoria na Qualidade dos Dados` → Os dados passam por um processo de limpeza antes de serem armazenados
- `Visão Histórica` → É possível aprender com tendências e desafios passados, usando os dados históricos armazenados do `DW`

### Data Lakes

- Serve principalmente para armazenar dados sem a necessidade de uma limpeza ou transformação prévia. Pode também armazenar dados estruturados
- `Data Lake` é um `conceito` para armazenamento de dados
- Quando necessário, o analista de dados busca do `DL` a porção de dados necessária e aplica a limpeza nos dados
- Dependendo da empresa, ela necessitará de um `DL` e um `DW`, pois eles atendem a diferentes necessidades e casos de uso
- A estrutura de dados`(schema)` não é definida quando os dados são capturados por isso o `DL` se torna mais rápido quando uma empresa precisa pegar informações de forma imediata
- Os Data Lakes permitem que as empresas gerem diferentes tipos de percepções sobre os dados, desde relatórios sobre dados históricos até modelos preditivos criados por `ML`
- Os `DL` podem ser construídos com varias tecnologias como `Apache Hadoop` ou **Bancos de Dados NoSQL**
- Podemos importar dados do `DW` para o `DL` e vice-versa, porém para passar os dados de um `DL` para um `DW` é precisar usar os processos `ETL` para estruturar os dados
-

### Benefícios do DL

- `Armazenamento em formato bruto` → Não precisamos limpar e transformar os dados antes do armazenamento
- `Importação de qualquer quantidade de dados em tempo real` → Não há perda de tempo na coleta de dados sendo que estes vem em seu formato bruto
- `Repositório central para todos os dados da empresa` → Permite que várias pessoas de áreas diferentes acessem o mesmo `DL` para buscar as informações
- `Sem necessidade de movimentação de dados` → Cada vez mais ferramentas permitem conexão direta com o `DL`

### Data Stores

- É um `repositório` para armazenar e gerenciar de foram persistente coleções de dados que incluem não apenas dados estruturados, mas também tipos de armazenamento variados, como documentos no formato chave-valor, fila de mensagens
- Resumindo, o `Data Stores` permite que você armazene dados em formatos variados e normalmente específicos
- Normalmente não é um armazenamento em massa

### Benefícios do DS

- `Armazenamento de variados tipos de dados` → Dados que não se encaixam em outros repositórios de armazenamento
- `Flexibilidade` → Armazenamento de dados aderente às necessidades da aplicação final
- `Suporte a dados semi-estruturados` → Dados que possuem alguma organização prévia, mas que devem ser usados em seu formato original
- `Custo total menor` → O custo tende a ser menor que outras solução de armazenamento, por ser mais específico

## Seção 4 - Armazenamento de Processamento Paralelo

- Muito provavelmente os dados que a empresa coleta, devido a quantidade, não cabem apenas em um servidor, por isso usa-se algo chamado `processamento paralelo`, para que os dados consigam ser armazenados e mais de um local

### Cluster de computadores

- Existe um limite de quanto é possível armazenar de dados em um único servidor já que ele é uma máquina com limitações
- Por isso foram criados clusters de computadores, que são conjuntos de servidores com um mesmo propósito
- `Clusters` são cada vez mais usados em `Big Data`, nos permitindo realizar armazenamento e processamento paralelos

### Armazenamento paralelo

- Consiste em distribuir o armazenamento de dados através de diversos servidores, o que permite aumentar de forma considerável a capacidade de armazenamento usando hardware de baixo custo
- Para entender como os dados são distribuídos entre os computadores, precisamos olhar para a parte do software que gerencia os dados - `Apache Hadoop`
- Os dados que vão para os servidores vem de várias fontes e através de `switches` são direcionados para as máquinas que contém o `Apache Hadoop` para alocar esses dados

### Software para armazenamento paralelo - Apache Hadoop

- Todo os computadores possuem um sistema de arquivos, porém em sua grande maioria **não são distribuídos**
- Através do software de `sistemas de arquivos distribuídos` como **`Hadoop Distributed File System(HDSF)`**, é possível enviar arquivos para um cluster de computadores e o `HDSF` gerenciará quais máquinas vão conter esses arquivos para caso haja perda de uma máquina
- O `Apache Hadoop` foi programado para funcionar hardware de baixo custo , esperando que alguma máquina do cluster possa dar problema
- `HDSF` é o software responsável pela gestão do cluster definindo com os arquivos serão distribuídos
- Permitiu que o Big Data pudesse ser usado em larga escala

### Processamento paralelo

- O objetivo é dividir uma tarefa em várias sub tarefas e executá-las em paralelo
- Para executar essas sub tarefas, podemos usar frameworks como `Apache Spark` `Apache Hadoop MapReduce` com linguagens como `Python`
- O programa criado com o `Apache Spark` por exemplo, entra em contato com o serviço que está rodando em todas as maquinas do cluster e procura onde estão os dados solicitados
- Cada máquina executa a sub tarefa, devolve o resultado para o **framework** que apresentará o resultado para o usuário

Através de `Name Nodes`(ou gestor do cluster), `Data Nodes`(nodes que armazenam os dados), `Job Trackers` e `Task Trackers` é que conseguimos acessar os clusters de computadores, usando sub tarefas criadas por frameworks para processamento paralelo, e obter os dados que precisamos apresentar. A camada de `HDFS` cuida dos `Name e Data Nodes` e a camada do Framework cuida dos `Job e Task Trackers`

## Seção 5 - Cloud Computing

### O que é

- É a entrega de serviços de computação, `servidores`; `bancos de dados`; etc pela internet (nuvem) para oferecer recursos flexíveis, inovação e economia de escala
- Normalmente, pagamos apenas pelos serviços em nuvem que usamos, ajudando a reduzir os custos operacionais e escalar conforme a necessidade

### Cloud Computing e Big Data

- Podemos criar cluster do computadores usando provedores em nuvem, com a infraestrutura física do provedor
- Adotar o modelo de **nuvem** tende, na maioria dos casos, ser `mais barato` do que as soluções físicas em uma empresa já que, na **nuvem**, podemos desligar a utilização de um serviço quando não formos usar por exemplo
- A `segurança do cloud computing` é maior se comparado com as soluções físicas, pois os provedores investem de forma pesada em segurança

### Conhecendo a AWS

- Possui 12 meses grátis para quem estiver acessando pela primeira vez, com recursos limitados, e engloba todas as ferramentas da Amazon, como `machine learning`, `data analysis`, entre outros
- Com `EC2` Elastic Cloud, você consegue criar máquinas na nuvem por exemplo
- O sistema operacional mais utilizado para mexer em máquinas criadas pela AWS é o `Linux`

## Seção 6 - MLOps e DataOps

### O que é Machine Learning

- É uma `sub área` da `Inteligência Artificial` e da `Ciência da Computação` que se concentra no uso de `dados` e `algoritmos` para imitar a forma como humanos aprendem, melhorando gradativamente sua precisão
- O processo simplificado seria:
  - Dados históricos → Alimenta um algoritmo, treina esse algoritmo → Cria-se um modelo, que é uma formulação matemática

### Pipeline de Machine Learning

- Chamado também de `workflow`, é o processo para que você saia de uma ponta a outra em aprendizado de máquina
- **Separado em etapas:**
  - `Preparação dos Dados` → Limpeza, transformação, normalização, processamento
  - `Construção e Treinamento do Modelo` → Modelagem: Seleção do algoritmo, otimização de hiperparâmetros, treinamento, teste e avaliação
  - `Deploy do Modelo` → O deploy pode ser feito de várias maneiras, seja uma aplicação web, um aplicativo, dashboards, etc

### O que é Machine Learning Ops

- É um conjunto de práticas para colaboração e comunicação entre Cientistas de Dados e profissionais de operações
- A aplicação dessas práticas aumenta a qualidade, simplifica o processo de gerenciamento e automatiza a implantação de modelos de aprendizado de máquina em ambientes de produção em grande escala
- MLOps visa unificar o desenvolvimento de sistemas de ML (dev) e a implantação de sistemas de ML (ops) para padronizar e agilizar a entrega contínua de modelos de alto desempenho em produção

### O que é DataOps

- É uma metodologia ágil e orientada a processos para desenvolver e entregar análises
- Fornece as ferramentas, processos e estruturas organizacionais para apoiar a empresa focada em dados
- É também a capacidade de `habilitar soluções`, `desenvolver produtos de dados` e `ativar dados` para valor comercial em todas as camadas de tecnologia, da infraestrutura à experiência do usuário final

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/51282dd0-38dd-4009-bfbb-3f8d4cadedd6/72e65d2f-e533-4495-9af5-ca52210cfb4b/Untitled.png)

## Seção 7 - Dados como serviço DaaS

- Conceito de ter disponível todos os dados necessários para usa empresa sem precisar criar toda infraestrutura para captação e armazenamento dos dados

### Data as a Service

- É uma estratégia de gerenciamento de dados que visa alavancar os dados como um ativo de negócios para maior agilidade no processo de análise
- Semelhante a outros modelos `as a service`, o `DaaS` fornece uma maneira de gerenciar as grandes quantidade de dados que as organizações geram todos os dias e fornecer essas informações valiosas em toda a empresa para a tomada de decisões baseada em dados

### Arquitetura DaaS

- A Arquitetura `DaaS` se concentra no provisionamento de dados de uma variedade de fontes sob demanda por meio de `APIs`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/51282dd0-38dd-4009-bfbb-3f8d4cadedd6/0094951b-f9d5-4a57-ba0c-9a6cbd5cfac1/Untitled.png)

- Os dados podem vir de fontes de dados externas como: `DL` `DW`
- O `Virtual Data Layer` funciona como um canal para todas os dados de fontes externas
- `API` nesse caso funciona como um `Software` que permite a pessoa pegar os dados com base em critérios, filtros etc
- Por fim o usuário recebe os dados, podendo esse ser um analista de dados ou até mesmo uma aplicação web
- O `DaaS` fornece também dados já tratados ou fluxos de dados

### Benefícios do DaaS

- `Monetização de dados`
- `Redução de custos`
- `Caminho mais rápido para inovação`
- `Agilidade no processo de decisão baseado em dados`
- `Menor risco no uso de dados`
- `Criação de uma cultura data-driven`

## Seção 8 - ETL Extração, Transformação e Carga de Dados

### Definindo ETL

- Processo de movimentação dos dados
- É um `conceito`
- Separado entre:
  - `Source` → Fonte de onde `extraímos` os dados **(Extract)**
  - `Staging area` → Não é sempre necessária, mas serve para ser um local onde possamos transformar os dados **(Transform)**
  - `Data Warehouse` → Lugar para onde os dados transformados vão para poderem ser `analisados` e utilizados para os mais diferentes propósitos. Fazemos um carregamento dos dados da `staging area` para o `DW` **(Load)**

### ETL x ELT

- `ELT` se diferencia do `ETL` no sentido que, nós buscamos os dados das fontes, armazenamos eles em `Data Lakes` e depois um cientista de dados, por exemplo, pega e transforma/processa os dados

### Principais soluções de ETL e ELT

- `Oracle Data Integrator`
- `Pentaho Data Integrator`
- `Apache Nifi` → Open source
- `Apache Spark` → Mais usado para processamento de dado do que ETL
- `AWS Glue` → Serverless

## Seção 9 - Como iniciar um projeto de Big Data

### O que é Big Data Analytics

- O valor do Big Data é extraído quando você aplica alguma técnica de análise de dados, daí que vem o termo `Analytics`
- As técnicas de análise de dados existem ha anos, porém agora estão sendo usadas em Big Data

### Como as empresas estão usando o Big Data

- Na área de `manufatura` por exemplo, as máquinas, cada vez mais equipadas com sensores, enviam dados sobre o processo realizado, permitindo que o analista de dados possa criar `insights` e `projeções` com base nesses dados
- A área de `finanças` foi uma das primeiras a utilizar `Big Data`, com a enorme quantidade de dados de fundos, investimentos, etc, existe uma enorme variedade de aplicações para análise de dados
- Área da `saúde` também é um ótimo setor para `Big Data`

### Definição do Business Case

- Quais são os objetivos do projeto
- Não é um documento técnico, serve para ter uma `Big Picture`
- Esse projeto deve vir da área de negócios

### Planejamento do projeto

- Fazer um passo a passo do projeto
- Ter uma imagem do orçamento necessário para realização do projeto
- Treinar ou contratar profissionais especializados para a realização das tarefas técnicas
- Levantar os requisitos técnicos e seus custos
