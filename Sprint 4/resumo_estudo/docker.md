# Docker

## Seção 1 - Introdução

Para saber o que cada comando docker faz → `docker <comando> --help`

### O que é?

- É um software que reduz a `complexidade de setup` de aplicações
- `Containers` → São os locais onde rodamos nossas aplicações, e.g. `container de Node` ou `container de PHP` ou tudo junto no mesmo container se necessário
- Permite criar ambientes independentes e que funcionam em diversos SO’s
- Deixa os projetos performáticos
- Podemos por exemplo rodas um banco de dados `MongoDB` sem instalar ele, apenas usando o `Docker`

### Por que?

- O `Docker` proporciona mais velocidade na configuração do ambiente de um dev
- `Pouco tempo gasto em manutenção`, containers são executados como configurados
- Mais performático que uma `VM`

## Seção 2 - Trabalhando com containers

### O que são containers

- Um `pacote de código que pode executar uma ação`, e.g. rodar uma aplicação **Node.js**, **PHP**, etc
- Um container não roda sem uma `imagem`
- Os nossos projetos serão executados dentro dos containers que criarmos/utilizarmos
- `Containers utilizam imagens` para poderem ser executados
- **Múltiplos containers podem rodar juntos**

### Container x Imagem

- `Imagem` e `Container` são recursos fundamentais no `Docker`
- Imagem é o `‘projeto’` que será executado pelo container, todas as instruções estarão declaradas nela
- **Container** é o Docker rodando alguma **imagem,** executando algum código proposto por ela
- `Fluxo` → Programamos uma `imagem` e a executamos por meio de um `container`

### Rodando um container

- Usando o comando → `docker run <nome_da_imagem>`, conseguiremos baixar a imagem que queremos, caso ela já não esteja no nosso sistema
- Através do site [\*\*`https://hub.docker.com/`](https://hub.docker.com/)\*\* podemos encontrar as imagens que iremos precisar para os nossos containers
- Para `parar um container` usamos: `docker stop <nome_do_container>`

### Verificando containers já executados

- Comando `docker ps` ou `docker container ls` exibe quais containers estão sendo executados no momento
- Utilizando a flag `-a`, temos também todos os containers já executados na máquina
- Esse comando é util para saber quais containers estão sendo rodados

### Executar containers com interação

- Podemos rodar um container e deixá-lo executando no terminal;
- Vamos utilizar a flag `-it`
- Com isso podemos executar `comandos disponíveis no container` que estamos utilizando o comando `run`, e.g. escrever código javascript em um container `Node`

### Container x VM

- Container é uma aplicação que serve para um determinado fim, `não possui sistema operacional` e seu tamanho é de alguns `mbs`
- Containers gastam menos recursos, por causa do seu uso específico
- VM gasta mais recursos, porém podem exercer mais funções

### Executar container em background

- Quando iniciamos um container que persiste, `ele fica ocupando o terminal`
- Podemos executar um container em background, para não precisar ficar com diversas abas de terminal aberto, utilizamos a flag `-d` for `detached`
- Usamos `docker ps` para verificar os containers em background

### Expor portas

- Os `containers docker` não tem conexão com nada fora deles
- Por isso, precisamos expor portas, com a flag `-p` e podemos fazer → `-p 80:80` → `docker run -d -p 80:80 <nome_da_imagem>`: **comando completo**
- Com isso o container está acessível na `porta 80`
- Podemos mudar a porta que acessamos no nosso navegador através da tag `-p` e.g. `-p 3000:80` → a porta que iremos acessar no navegador é a `3000` nesse caso

### Reiniciando containers

- Para voltar a rodar um container podemos usar o comando `docker start <id> ou <nome_do_container>`
- O comando `run` sempre `cria um novo container`**,** por isso é melhor usar o comando `start` para reiniciar um container

### Definindo nome do container

- Podemos definir o nome do container com → `--name`
- Caso não definamos, recebemos um nome aleatório que irá atrapalhar na hora de encontrar os containers
- **Comando completo:**

```docker
#nginx_app é o novo nome do container escolhido pelo usuário
docker run -d -p 80:80 --name nginx_app nginx

#Para reiniciar um container que foi parado e.g. 'nginx'
docker start nginx_app
```

### Verificando logs

- Podemos verificar o que aconteceu em um container com o comando `logs`
- Comando → `docker logs <id>/<nome_do_container>`
- Últimas ações realizadas no container, serão `exibidas no terminal`

### Removendo Containers

- Podemos remover containers da máquina que não estão sendo utilizados
- Comando → `docker rm <id>/<nome_do_container>`
- Se o container ainda estiver rodando, podemos usar a flag `-f` (force)
- O container removido não é mais listado em `docker ps -a`

## Seção 3 - Criando imagens e avançando em containers

### O que é uma imagem

- Imagens são originadas de `arquivos que programamos` para que o Docker crie uma estrutura que execute determinadas ações em containers
- Elas contém informações como: **imagens base**, **diretório base**, **comandos a serem executados**, **porta da aplicação** e **etc**
- Ao rodar um container baseado na imagem, as instruções serão `executadas em camadas`

### Como escolher uma imagem

- Pegamos imagens no `hub docker` → [**https://hub.docker.com/**](https://hub.docker.com/)
- Qualquer pessoa pode fazer um upload de imagem no site do `hub docker`, gerando um **problema de segurança**
- Devemos nos atentar às `imagens oficiais`, vendo também a quantidade de downloads como base

### Criando nossa primeira imagem

- Para criar uma imagem, vamos precisar de um arquivo `Dockerfile` em uma pasta que ficará o projeto
- Este arquivo vai precisar de algumas `instruções para poder ser executado`:
  - `FROM` → imagem base
  - `WORKDRIR` → Diretório da aplicação
  - `EXPOSE` → Porta da aplicação
  - `COPY` → Quais arquivos precisam ser copiados
  - `RUN` → Executa o comando passado
- O comando `docker images` mostra todas as imagens que a gente usou, sejam `nossa imagens` ou imagens do site `docker hub`

### Executando a nossa imagem

- Para executar uma imagem, primeiramente vamos precisar fazer o build, esta executará os comandos presentes do `Dockerfile`
- Comando → `docker build <diretório da imagem>`
- Depois vamos utilizar o `docker run <imagem>` para executá-la

### Alterando nossa imagem

- Sempre que alteramos uma imagem, precisamos `fazer o build novamente`
- Para o Docker é como se fosse uma imagem `nova`
- Após fazer o build, vamos executá-la por outro id único criada com o `docker run`

### Cache de camadas

- As imagens do Docker são divididas em `camadas`(layers)
- Cada instrução no `Dockfile`, como `FROM, EXPOSE etc` representa uma layer
- Quando algo é atualizado apenas as **layers depois da linha atualizada são refeitas**

```docker
#Isso é o que está dentro de um arquivo Docker
FROM node

#Se nós mudarmos o WORKDIR, apenas ele e o que está abaixo passarão pelo build
WORKDIR /app

COPY package*.json .
```

- O resto permanece em cache, tornando o `build mais rápido`

### Fazendo download de imagens

- Podemos fazer o download de alguma imagem do hub e deixá-la disponível em nosso ambiente
- Comando → `docker pull <imagem>`
- Desta maneira, caso ela seja necessária em outro container, ela já está disponível

### Múltiplas aplicações, mesmo container

- Podemos inicializar vários containers com a mesma imagem
- As aplicações funcionarão em paralelo
- Para testar isso, podemos determinar uma porta diferente para cada uma, e rodar no modo `detached` `-d`

### Nomeando imagens

- Podemos, assim como os containers, `nomear as imagens`
- Vamos utilizar o comando `docker tag <nome>`
- Também podemos modificar a tag, que seria como uma versão da imagem, semelhante ao git
- Para inserir a tag utilizamos: `docker tag <nome>:<tag>`

### Iniciando imagem com um nome

- Podemos nomear a imagem já na sua criação
- Utilizando a flag `-t` → `docker build -t <nome> <diretório do arquivo>`
- É possível inserir o nome e a tag, na sintaxe: `nome:tag`
- Facilita o processo de nomeação

### Comando start interativo

- Com a flag `-i` podemos reiniciar o container com o console interativo, ao invés de apenas deixar ele `detached` rodando no background
- Comando → `docker start -i <container>`

### Removendo imagens

- Comando → `docker rmi <imagem>`
- Podemos adicionar a `:tag` depois da imagem para remover um versão específica
- Imagens que estão sendo utilizadas por um container apresentarão um erro no terminal
- Com a flag `-f` podemos forçar a remoção

### Removendo imagens e containers

- Comando → `docker system prune`
- Podemos remover imagens, containers e networks não utilizados
- É preciso confirmar essa operação de remoção

### Removendo container após utilizar

- Um container pode ser automaticamente deletado após sua utilização
- Para isso vamos usar a flag `--rm` durante a execução do `run`
- Comando → `docker run --rm <container>`
- Desta maneira `economizamos espaço no computador` e deixamos o ambiente mais organizado
- Podemos usar esse padrão do `rm` para testar um container várias vezes sem precisar ficar criando vários diferentes

### Copiando arquivos

- Podemos copiar arquivos do docker para um diretório e vice versa
- Comando → `docker cp <fonte> <destino>`

### Verificar informações de processamento

- Para verificar dados de execução de um container utilizamos: `docker top <container>`
- Desta maneira temos acesso a quando ele foi iniciado, id do processo, descrição do comando CMD

### Verificar dados de um container

- Para verificar diversas informações como: id, data da criação, imagem e muito mais
- Comando → `docker inspect <container>`
- Com isso entendemos como o container está configurado

### Autenticação no Docker Hub

- Ao criarmos uma conta no `docker hub` podemos nos autenticar via terminal
- Comando → `docker login`
- E então inserir o usuário e senha
- Agora podemos `enviar nossas imagens` para o `HUB`
- Para `logout` → `docker logout`

### Enviando imagem para o Docker Hub

- Comando → `docker push <imagem>`
- Porém é preciso criar o repositório para a imagem do no site do Hub primeiro
- Também é necessário `estar autenticado`

### Enviando atualização de imagem

- Para enviar uma atualização vamos primeiramente fazer o build
- Trocando a tag da imagem para a versão atualizada
- Depois vamos fazer um push novamente para o repositório
- Com isso teremos todas as versões disponíveis

## Seção 4 - Introduzindo volumes aos nosso containers

### O que são volumes

- Uma forma prática de `persistir dados` em aplicações e não depender de containers para isso
- Todo dado criado por um container é salvo nele, quando o container é removido, perdemos os dados
- Então precisamos dos volumes para gerenciar os dados e também conseguir `fazer backups` de forma mais simples

### Tipos de volumes

- `Anônimos` → Diretórios criados pela flag `-v`, porém com um nome aleatório
- `Nomeados` → São volumes com nomes, podemos nos referir a estes facilmente e saber para que são utilizados no nosso ambiente
- `Bind mounts` → Uma forma de salvar dados na nossa máquina, sem o gerenciador do Docker, informamos um diretório para este fim

### Trabalhando com volumes

- **Todos os arquivos gerados dentro de um container fica dentro dele**
- Se o container for removido, `os dados são perdidos`
- Por isso precisamos dos volumes

### Volumes anônimos

- Podemos criar um volume anônimo com o comando → `docker run -v /data`
- O `/data` será o diretório que contém o volume anônimo
- Este container será atrelado ao volume anônimo
- Com o comando `docker volume ls`, podemos ver todos os volumes do nosso ambiente

### Volumes nomeados

- Para volumes nomeados temos → `docker run -v nomedovolume:/data`. Para volumes nomeados o diretório será sempre o `mesmo caminho do WORKDIR`, apenas adicionando o diretório específico para o volume

```docker
# O nome do volume é 'phpvolume' e o diretório será o mesmo do WORKDIR do Dockerfile
docker run -v phpvolume:/var/www/html/messages
```

- Agora o volume tem um nome e pode ser facilmente referenciado
- De novo com `docker volume ls`, podemos ver nosso volume nomeado
- Tem a mesma função do volume anônimo

### Bind mounts

- Também é um volume, porém ele fica em um diretório que nós especificamos
- Então não criamos um volume em si, apenas apontamos um diretório
- Comando → `docker run -v /dir/data:/data`
- Desta maneira o diretório `/dir/data` no nosso computador, será o volume deste container
- `Bind Mount` não serve apenas para volume
- Podemos usar esta técnica para atualização em tempo real do projeto
- Sem ter que refazer o build a cada atualização do mesmo

### Comandos para volumes

- **Criar volume manualmente** → `docker volume create <nome>`
- Com isso temos um `named volume` criado, podemos atrelar a algum container em execução do mesmo
- **Listar todos os volumes** → `docker volume ls`
- **Checar um volume** → `docker volume inspect <nome do volume>`
- Desta forma temos acesso ao `local em que o volume guarda dados`, nome, escopo e mais
- **Remover um volume** → `docker volume rm <nome do volume>`
- **Remover todos os volumes não utilizados** → `docker volume prune`

## Seção 5 - Conectando containers com Networks

### O que são Networks

- Uma forma de gerenciar a conexão do `Docker` com outras plataformas ou até entre containers
- As networks são `criadas separadas dos containers`, assim como os volumes
- Uma rede deixa muito simples a comunicação entre containers

### Tipos de conexão

- Os containers costumam ter `3 tipos de conexão`
- `Externa` → conexão com uma API de um servidor remoto
- `Com o host` → comunicação com a máquina que está executando o Docker
- `Entre containers` → comunicação que utiliza o `driver bridge` e permite a comunicação entre dois ou mais containers

### Tipos de redes (drivers)

- `Bridge` → o mais comum e `default do Docker`, utilizado quando containers precisam se conectar
- `host` → permite a conexão entre um container à máquina que está hosteando o `Docker`
- `macvlan` → permite conexão a um container por um MAC address
- `none` → remove todas as conexões de rede de um container
- `plugins` → permite extensões de terceiros para criar outras redes

### Listando networks

- Comando → `docker network ls`
- Algumas redes já estão criadas, estas fazem parte da configuração inicial do docker

### Criando rede

- Comando → `network create <nome da rede>`
- Esta rede será do tipo `bridge`, que é o mais utilizado
- Podemos criar diversas redes
- Para `remover redes` → `docker network rm <nome da rede>`
- Devemos tomar cuidado com `containers já conectados`
- **Remover redes em massa** → `docker network prune`
- Remove redes que não estão sendo utilizadas

### Conexão externa

- Containers podem se conectar livremente ao mundo externo
- Um caso seria: uma API de código aberto
- Podemos acessá-la livremente e usar seus dados

### Conexão com o host

- Podemos também conectar um container com o host do Docker
- Host é a maquina que está executando o Docker, podendo ser a nossa máquina ou um servidor da AWS por exemplo

### Conexão entre containers

- Podemos estabelecer uma `conexão entre containers`
- `Exemplo`: duas imagens distintas rodando em `containers separados` que precisam se conectar para inserir um dado no banco de dados
- Vamos precisar de uma rede `bridge` para fazer esta conexão

### Conectando um container a uma rede

- Comando → `docker network connect <rede> <container>`
- Após o comando, o container estará dentro da rede
- Para desconectar → `docker network disconnect <rede> <container>`

### Inspecionando redes

- Comando → `docker network inspect <nome da rede>`

## Seção 6 - Introdução ao YAML

### O que é YAML

- Uma `linguagem de serialização`
- Usada geralmente para `arquivos de configuração`, inclusive do Docker , para configurar o Docker Compose
- É de fácil leitura para nós humanos
- Extensão dos arquivos é `yml` ou `yaml`

### Criando nosso arquivo YAML

- O arquivo `.yaml` geralmente possui chaves e valores
- Que é de onde vamos retirar as configurações do nosso sistema

```yaml
# Esse é o jeito de escrever em um arquivo YAML
nome: 'Bruno' # É obrigatório espaço depois da chave
idade: 25
```

### Espaçamento e indentação

- O fim de uma linha indica o fim de uma instrução, não há ponto e virgula
- A indentação deve conter um ou mais espaços, e `não devemos utilizar tab`
- Cada linha define um novo bloco
- O `espaço é obrigatório` após a declaração da chave
- Para `comentar` usamos o `#`, eles serão ignorados pelo programa

### Tipos de dados

- `Inteiros` = 12
- `Floats` = 15.8
- Dados textuais podem ser escritos `sem aspas`
- Podemos definir um `dado nulo` com: `~` ou `null`

### Booleanos

- `True` e `On` = verdadeiro
- `False` e `Off` = falso

### Arrays

- Duas sintaxes:
- `Primeira` → [1,2,3,4,5]
- items:
  - 1

  - 2

  - 3

### Dicionários

- obj: {a: 1, b: 2, c: 3}
- ou

```yaml
objeto:
	chave: 1
	chave: 2
```

## Seção 7 - Docker Compose

### O que é

- É uma ferramenta para `rodar múltiplos containers`
- Teremos `apenas um arquivo de configuração`, que orquestra totalmente esta situação
- É uma forma de rodar `múltiplos builds e runs` com um comando
- Em `projetos maiores` é essencial o uso do `Compose`

### Criando nosso arquivo de Compose

- Primeiramente vamos criar um arquivo chamado `docker-compose.yaml` na raiz do projeto
- Este arquivo vai `coordenar os containers e imagens`, e possui algumas chaves muito utilizadas
- `version`: versão do Compose
- `services`: Containers/serviços que vão rodar nessa aplicação
- `volumes`: Possível adição de volumes
- Todas as palavras acima são `reservadas` do Docker Compose

### Rodando o Compose

- Comando → `docker compose up`
- Isso fará com que as instruções no arquivo sejam executadas
- Da mesma forma que realizamos os builds e também os runs
- Podemos parar o Compose com `ctrl + c` no terminal
- Ao rodar o Compose, o terminal será ocupado com a ferramenta do Compose, podemos roda-lo em `background` para ter o terminal livre

### Compose em background

- O Compose também pode ser executado em modo `detached`
- Para isso usamos a flag `-d` no comando. Com isso os containers estarão rodando em `background`
- Para o Compose `rodando no background` usamos: `docker compose down`

### Variáveis ambiente

- Podemos definir variáveis de ambiente para o Docker Compose
- Para isso vamos definir um arquivo base em `env_file`
- As variáveis podem ser chamadas pela sintaxe: `${VARIAVEL}`
- Esta técnica é útil quando o dado a ser inserido é `sensível/não pode ser compartilhado`, como uma senha por exemplo

### Rede no Compose

- O Compose cria uma `rede básica Bridge` entre os containers
- Porém podemos isolar as redes com a chave `networks` no arquivo `docker-compose`
- Desta maneira podemos conectar apenas os containers que optarmos

### Build no Compose

- Podemos gerar o build durante o Compose também
- Isso elimina o processo de `buildar a imagem` a cada atualização
- Para fazer isso basta, dentro do arquivo `docker-compose.yaml`, alterar a campo que seria `image` para `build` passando o caminho para o `Dockerfile` da imagem

### Verificando o que tem no Compose

- Comando → `docker-compose ps`
- Receberemos um `resumo dos serviços` que sobem ao rodar o compose

## Seção 8 - Docker Swarm para orquestração

### O que é orquestração de containers

- É o ato de conseguir `gerenciar e escalar os containers` da nossa aplicação
- Temos um serviço que rege sobre outros serviços, verificando se os mesmos estão funcionando como deveriam
- Desta forma conseguimos garantir uma aplicação saudável e também que esteja sempre disponível
- Alguns serviços: `Docker Swarm, kubernetes e Apache Mesos`

### O que é Docker Swarm

- Uma ferramenta do Docker para `orquestrar containers`
- Podendo `escalar horizontalmente` nossos projetos de maneira simples
- A facilidade do Swarm para outros orquestradores é que todos os `comandos são muito semelhantes ao do Docker`
- Podemos rodar o `Swarm` em máquinas na nuvem através da `AWS`, esse é o método mais utilizado

### Conceitos fundamentais

- `Nodes` → é uma instância (máquina) que participa do Swarm
- `Manager Node` → Node que gerencia os demais Node
- `Worker Node` → Nodes que trabalham em função do Manager
- `Service` → Um conjunto de tasks que o Manager Node manda o Work Node executar
- `Task` → Comandos que são executados nos Nodes

### Iniciando o Swarm

- Comando → `docker swarm init`
- Em alguns casos, como no docker labs, precisamos declarar o IP do servidor com a flag → `--advertise-addr`
- Isso fará com que a instância/máquina vire um `Node`
- E também transforma o Node em um `Manager`

### Listando Nodes ativos

- Comando → `docker node ls`
- Desta forma os serviços serão exibidos no terminal e podemos monitorar o que o `Swarm` está orquestrando
- Este comando é de grande utilidade conforme formos adicionando serviços

### Adicionando máquinas ao Swarm

- Comando → `docker swarm join --token <token><ip>:<porta>`
- Desta forma duas máquinas estarão conectadas
- A nova máquina entra na hierarquia como `Worker`
- Todas as ações `(Tasks)` utilizadas na Manager, serão replicadas em Nodes que foram adicionados com join

### Subindo serviço no Swarm

- Comando → `docker service create --name <nome> <imagem>`
- Desta forma teremos um container novo sendo adicionado ao nosso Manager
- E este serviço estará sendo gerenciado pelo Swarm

### Listando serviços

- Comando → `docker services ls`, mostra os projetos rodando nas máquinas
- Desta maneira todos os serviços que iniciamos serão exibidos
- Algumas informações importantes sobre eles estão: `nome, replicas, imagem, porta`

### Removendo um serviço

- Comando → `docker service rm <nome>`
- Desta maneira o serviço para de rodar
- Isso pode significar: `para um container que está rodando` e as consequências dessa ação

### Replicando serviços

- Podemos criar um serviço com um número maior de réplicas → `docker service create --name <nome> --replicas <numero> <imagem>`
- Desta maneira uma task será emitida, replicando este serviço nos Workers
- Agora iniciamos de fato a orquestração

### Checando o token do Swarm

- As vezes vamos precisar checar o token do Swarm, `para dar join em alguma outra instância futuramente`
- Comando → `docker swarm join-token manager`
- Desta forma recebemos o token pelo terminal

### Removendo instância do Swarm

- Podemos parar de executar o `Swarm` em uma instância
- Comando → `docker swarm leave`
- Agora a instância para de ser um `Node`
- O Node ainda aparece pelo comando `docker node ls`, porém esta em estado `Down`

### Removendo um Node

- Comando → `docker node rm <ID>`
- O container continuará rodando a instância

### Inspecionando serviços

- Comando → `docker service inspect <ID>`
- Retorna informações como: `nome, data de criação, portas, etc`

### Rodando Compose com Swarm

- Comando → `docker stack deploy -c <arquivo.yaml> <nome>`
- Temos agora o Compose sendo executado, porém agora estamos em `modo swarm` e podemos utilizar os Nodes como réplicas

### Aumentado réplicas do Stack

- Podemos criar novas réplicas nos `Worker Nodes`
- Comando → `docker service scale <nome>=<replicas>`
- Desta forma as outras máquinas receberão as Tasks a serem executadas

### Fazer serviço não receber mais Tasks

- Podemos fazer com que um serviço `não receba mais ‘ordens’ do Manager`
- Comando → `docker node update --avaliability drain <ID>`
- Podemos voltar para `active` e ele volta ao normal

### Atualizando uma imagem no Swarm

- Comando → `docker service update --image <imagem> <servico>`
- Desta forma apenas os nodes que estão com o status `active` receberão atualizações

## Seção 9 - Orquestração com Kubernetes

### O que é Kubernetes

- Uma ferramenta de `orquestração de containers`
- Escalando projetos, formando um `cluster`
- Gerencia serviços, garantindo que as aplicações sejam `executadas sempre da mesma forma`

### Conceitos fundamentais

- `Control Plane` → Onde é gerenciado o controle os processos dos Nodes
- `Nodes` → Máquinas que são gerenciadas pelo `Control Plane`
- `Deployment` → A execução de uma imagem/projeto em um Pod
- `Pod` → Um ou mais containers que estão em um Node
- `Services` → Serviços que expõe os Pods ao mundo Externo
- `Kubectl` → Cliente de linha de comando para o Kubernetes

### Dependências necessárias

- O kubernetes pode ser executado de uma maneira simples em nossa máquina
- Vamos precisar do client, `kubectl`, que é a maneira de executar o Kubernetes
- E também o `Minikube`, uma espécie de simulador de Kubernetes, para não precisarmos de vários computadores/servidores

### Iniciando o Minikube

- Comando → `minikube start --driver=<driver>`
- Onde o driver vai, depende de como foi sua instalação das dependências, e por qualquer um deles atingirem o mesmo resultado
- Você pode testar com: `virtualbox, hyperv e docker`
- Podemos testar o Minikube com: `minikube status`

### Parando o Minikube

- Sempre que o computador for reiniciado, deveremos iniciar o Minikube
- Podemos pará-lo com → `minikube stop`

### Acessando a dashboard do Kubernetes

- O `Minikube` nos disponibiliza um dashboard
- Nela podemos ver todo o detalhamento de nosso projeto: `serviços, pods e etc`
- Comando → `minikube dashboard`

### Deployment teoria

- O `Deployment` é uma parte fundamental do Kubernetes
- Com ele criamos nosso serviço que vai rodar nos `Pods`
- Definimos uma `imagem e um nome`, para posteriormente ser replicado entre os servidores
- A partir da criação do deployment teremos containers rodando
- Vamos precisar de uma `imagem do Hub do Docker`, para gerar um Deployment

### Criando nosso Deployment

- Após passar a imagem para o `Hub`, vamos rodar o projeto no Kubernetes
- Para isso vamos precisar de um `Deployment`, que é onde rodamos os containers das aplicações nos `Pods`
- Comando → `kubectl create deployment <nome> --image=<imagem>`
- Desta maneira o projeto de Flask estará sendo orquestrado pelo Kubernetes

### Checando Deployments

- Podemos checar se tudo foi criado corretamente, tanto o Deployment quanto a recepção do projeto pelo `Pod`;
- Comando → `kubectl get deployments`
- E para receber mais detalhes deles: `kubectl describe deployments`

### Checando Pods

- Os Pods são componentes muito importantes também, `onde os containers realmente são executados`
- Comando → `kubectl get pods`
- E para receber mais detalhes deles: `kubectl describe pods`

### Services teoria

- As aplicações do Kubernetes `não tem conexão com o mundo externo`
- Por isso precisamos criar uma Service, que é o que possibilita expor os Pods
- Então o `Service é uma entidade separada dos Pods`, que expõe eles a uma rede

### Criando o Service

- Comando → `kubectl expose deployment <nome> --type=<tipo> --port=<port>`
- Colocaremos o nome do Deployment já criado
- O tipo de Service, há vários para utilizarmos, porem o `LoadBalancer` é o mais comum, onde `todos os Pods são expostos`
- E uma `porta` para o serviço ser consumido
- Para ver quantos serviços já foram criados → `kubectl get services`

### Gerando IP de acesso

- Comando → `minikube service <nome>`
- Desta forma o `IP aparece no nosso terminal`
- E também uma aba no navegador é aberta com o projeto

### Replicando nossa aplicação

- Vamos ver como utilizar outros Pods, replicando assim a nossa aplicação
- Comando → `Kubectl scale deployment/<nome> --replicas=<numeros>`
- Podemos agora verificar no `Dashboard` o aumento de Pods
- Para diminuir o **número de réplicas →** `kubectl scale deployment/<nome> --replicas=<numero_menor>`

### Checar o número de réplicas

- Comando → `kubectl get rs`
- Desta maneira temos os status de réplicas dos projetos

### Atualização de imagem

- Para atualizar a imagem vamos precisar o nome do container, isso é dado na `Dashboard` dentro do Pod
- E também a nova imagem deve ser uma outra versão da atual, precisamos `subir uma nova tag no Hub ':'`
- Depois o comando → `kubectl set image deployment/<nome> <nome_container>=<nova_imagem>`

```python
#Exemplo de como seria o comando de atualização da imagem
kubectl set image deployment/flask-deployment flask-kub-projeto=bpcampos/flask-kub-projeto:2
```

### Desfazer alteração

- Conhecida como `rollback`
- Comando → `kubectl rollout undo deployment/<nome>`
- Comando para verificar se uma alteração foi feita → `kubectl rollout status deployment/<nome>`

### Deletar um service

- Comando → `kubectl delete service <nome>`
- Dessa forma os nosso pods não terão mais a conexão externa

### Deletar um Deployment

- Comando → `kubectl delete deployment <nome>`
- Desta maneira o `container não estará mais rodando`, pois paramos os Pods
- Assim precisaremos criar um novo Deployment com a mesma ou outra imagem

### Modo declarativo

- Até agora utilizamos o modo imperativo, que é `quando iniciamos a aplicação com comandos`
- O `modo declarativo` é guiado por um arquivo, semelhante ao `Docker Compose`
- Desta maneira tornamos nossas configurações mais simples e `centralizamos tudo em um comando`
- O arquivo para tudo isso é escrito em `YAML`

### Chaves mais utilizadas

- `apiVersion` → versão utilizada da ferramenta
- `kind` → tipo do arquivo (Deployment, Service)
- `metadata` → descrever algum objeto, inserindo chaves como name
- `replicas` → número de réplicas de Nodes/Pods
- `containers` → definir as especificações de containers como: nome e imagem

### Criando o arquivo

- Temos que criar um arquivo `YAML` com as chaves passadas acima

```yaml
#Exemplo de arquivo
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app-deployment
spec:
  replicas: 4
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
        - name: flask
          image: bpcampos/flask-kub-projeto:2
```

### Executando o arquivo

- Comando → `kubectl apply -f <arquivo>`
- Desta maneira o Deployment será criado conforme configurado no arquivo `.yaml`

### Parando o Deployment

- Comando → `kubectl delete -f <arquivo>`
- Desta maneira teremos os Pods sendo excluídos e o serviço finalizado

### Criando o serviço

- Vamos criar um arquivo para realizar o `Service (kind)`
- O arquivo será semelhante ao Deploy, porém tem uma responsabilidade diferente

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  selector:
    app: flask-app
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
  type: LoadBalancer
```

### Executando o serviço

- Comando → `kubectl apply -f <arquivo>`
- E o serviço vai estar disponível
- Precisaremos também gerar o IP de acesso com: `minikube service <nome>`

### Parando o serviço

- Comando → `kubectl delete -f <arquivo>`
- Agora o serviço não estará mais disponível

### Atualizando o projeto declarativo

- Primeiramente vamos `criar uma versão da imagem` com **build**
- Fazer o `push para o Hub`
- Depois é só alterar no arquivo de Deployment a `tag` e reaplicar o comando `apply`

### Unindo arquivos do projeto

- Podemos unir o Deployment e o Service em um só arquivo
- A separação de objetos para o YAML é com: `---`
- Desta forma cada um deles será executado
- Uma boa prática é colocar o `service antes do deployment`
