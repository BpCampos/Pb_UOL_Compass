# Resumo de estudo

### Docker

- Docker é um software que reduz a complexidade de setup de aplicações
- `Containers` → São os locais onde rodamos nossas aplicações
- Imagem é o **‘projeto’** que será executado pelo container, todas as instruções estarão declaradas nela
- Executar containers com interação com `-it`
- Expor portas com `-p`
- Reiniciando containers com `docker start <id> ou <nome_do_container>`
- Removendo Containers com `docker rm <id>/<nome_do_container>`
- Podemos pegar imanges do **Docker Hub**
- **Dockerfile** para criar imagens
- Executando a nossa imagem com `docker build <diretório da imagem>`
- Criação de volumes para persistir dados
- Network para conectar containers
- Arquivo `YAML`
- Docker Compose para rodar múltiplos containers
- Docker Swarm e Kubernetes para orquestração de containers

### [Anotações completas](./resumo_estudo/docker.md)

# Exercícios

1. Ex1
   [Resposta](exercicios/ex1.py)
2. Ex2
   [Resposta](exercicios/ex2.py)
3. Ex3
   [Resposta](exercicios/ex3.py)
4. Ex4
   [Resposta](exercicios/ex4.py)
5. Ex5
   [Resposta](exercicios/ex5.py)
6. Ex6
   [Resposta](exercicios/ex6.py)
7. Ex7
   [Resposta](exercicios/ex7.py)

# Tarefa

- [Respostas do desafio](./desafio/respostas_tarefa_docker.md)

# Certificados

- Certificado do curso **Docker**
  ![Curso Docker](certificados/Docker.jpg)

- Certificado do curso **Estatística Descritiva**
  ![Curso Estatística](certificados/Estatistica.jpg)
