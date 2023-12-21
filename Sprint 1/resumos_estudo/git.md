## Seção 1 - Introdução

- Controle de versão ajuda a `gerenciar o código-fonte`
- Podemos `reverter mudanças` feitas em versões atuais para versões mais antigas e funcionais
- `Git` é a ferramenta de controle de versão mais utilizada no mercado
- Baseado em repositórios e contem todas as versões do código

## Seção 2 - Git fundamentals

- Repositório é onde o código está armazenado
- `git init` → **Comando** que cria um repositório local
- `Github` → Serviço para gerenciar repositórios
- Passo a passo para conectar o repositório local ao `github`:
  - git init
  - git add README.md
  - git commit -m "first commit"
  - git branch -M main
  - `git remote add origin` https://github.com/BpCampos/curso_git1.git
  - git push -u origin main
- Usando `git remote -v`, podemos descobrir qual é a origem para qual o nosso repositório local está enviando os dados
- `git remote` → Pode ser usado para adicionar um repo para trackear ou remover
- `git remote rm origin` → remove a url de origem que conecta o repo local com o github
- `git status` → Mapeia todas as alterações do projeto bem como arquivos que foram modificados e quais estão sendo ou não monitorados pelo git
- `git add` → Adiciona arquivos ao git, para que eles possam ser monitorados. Podemos adicionar vários arquivos de uma vez ou todos os arquivos através do `.`
- `git commit` → Salva um retrato dos arquivos adicionados e os deixa preparados para serem enviados para o **github**
- `git push` → Envia as alterações para o github
- `git pull` → Recebe todas as alterações de arquivos que estão no github mas ainda não estão na sua máquina local. Se estivermos em um branch que não a `main`, precisaremos fazer `git pull origin main` para pegar as alterações da `main`
- `git rm <nome_do_arquivo>`→ Remove um arquivo do git fazendo com que ele não seja mais considerado pelo git ao realizar atualizações nesse arquivo
- `git log` → Acessa um log de modificações feitas no projeto. É possível ver todos os commits realizados sem especificações usando `git log --oneline`
- `git mv` → Pode renomear o arquivo assim como mover ele para outro diretório. O arquivo antigo é deletado e o git passa a monitorar o novo arquivo
- `git checkout <nome_do_arquivo>` → Retorna o arquivo modificado ao seu estado original e o retira do `staging`(area de monitoramento do git). Esse processo apaga as informações do arquivo local em comparação ao do github
- `git reset --hard` → Todas as alterações commitadas e pendentes serão excluídas.

### Clonando repositórios

- Processo de clonar um repositório que está no github para a nossa máquina
- `git clone <URL_do_projeto>` → Clona o projeto do Github para o diretório local

### Ignorando arquivos

- `.gitignore` → Arquivo responsável por impedir que certos diretórios ou arquivos com informações sensíveis sejam enviados ao github. E.g. pasta node_modules é comum ser adicionada ao git ignore pois ela sempre será adicionada pelo usuário que clonar o projeto

## Seção 3 - Branches

### O que são branches

- É a forma que o git separa as versões dos projetos
- Quando o projeto é iniciado, ele está na branch `main`
- Geralmente cada feature nova do projeto fica em um branch separada
- Após criar a feature a branch sofre um merge com a branch `main`

### Criando e visualizando branches

- `git branch <nome_da_branch>` → Cria uma nova branch no nosso projeto
- Se passarmos apenas `git branch`, serão listadas todas as branchs do projeto

### Deletando branches

- `git branch -d <nome_da_branch>` → Apaga a branch
- **Não é comum deletar branches,** normalmente guardamos o histórico do trabalho

### Mudando de branch

- `git checkout <nome_da_branch>` → Muda para a branch especificada contanto que ela já tenha sido criada
- `git checkout -b <nome_da_branch>` → Cria uma branch com o nome passado e muda para ela
- É sempre bom commitar mudanças na branch antes de voltar para a `main/master` para evitar que as mudanças feitas na branch alternativa apareçam na `main/master`
- **Sempre partir da master para criar uma branch nova**

### Unindo branches

- `git merge <nome_da_branch>` → Junta a branch atual com a especificada no comando
- Server para trabalhar com a versão mais atualizada da main/master na sua branch

### Stash - guardando e recuperando o código

- `git stash` → Volta o código para o momento em que a branch foi criada, guardando as mudanças em um ‘baú’ que pode ser acessado posteriormente
- `git stash list` → Para verificar as stashs criadas
- `git stash apply <numero_da_stash>` → Recupera os arquivos da stash
- `git stash clear` → Limpa todas as stashs

### Tag

- Podemos criar tags nas branchs por meio do comando `git tag -a <nome> -m <’msg’>`
- A tag é diferente do stash, serve como um checkpoint da uma branch
- `git tag` → Mostra todas as tags
- `git checkout <nome_da_tag>` → Muda para a tag especificada, voltando ou avançando o código a depender do conteúdo da tag

## Seção 4 - Compartilhamento e atualização de repositórios

### Encontrando branches

- O comando `git fetch` te atualiza de todas os branchs e tags que ainda não foram reconhecidos por você. Se usar a tag `-a` pegamos todos os branchs do repositório remoto
- Este comando é útil para utilizar o branch de outro dev do seu time
- Ao usar o `git fetch -a` podemos através do `git checkout <nome_do_branch>` entrar no branch adquirido e fazer com que ele faça parte dos nossos branchs

### Recebendo atualizações

- Ao criar branches, sempre tenha a branch main atualizada para versão mais recente
- Ao enviar o código de um branch para o github, espere ele ser aprovado(pull request) e incorporado ao branch main

### Submodules

- É a maneira que temos de possuir **dois ou mais projetos em um só repositório**
- `git submodule add <repo>` → Cria um submódulo no seu projeto
- O submódulo é um diretório criado dentro do diretório onde o comando foi chamado

## Seção 5 - Análise e inspeção de repositórios

### Exibindo detalhes de branches e tags

- `git show` → Mostra as alterações feitas no nosso repositório como branchs criadas, commits, fetchs entre outros
- Podemos ver detalhes de cada `tag` que foi adicionada ao nosso projeto através do `git show <nome_da_tag>`

### Exibindo diferenças

- `git diff <branch>` → Serve para exibir as diferenças de um branch em comparação ao repositório remoto
- Podemos verificar a diferença entre arquivos git com: `git diff <arquivo1> <arquivo2>`

## Seção 6 - Administração de repositórios

### Limpando arquivos untracked

- `git clean` → Verifica e limpa todos os arquivos que não estão sendo trackeados pelo git, ou seja, todos arquivos que não passaram pelo `git add`
- É usado bastante para limpar arquivos de log ou de erro que não são necessários

### Otimizando o repositório

- `git gc` → Abreviação para `garbage collector`. Identifica arquivos que não são mais necessários e os exclui

### Checando integridade de arquivos

- `git fsck` → Verifica a integridade dos arquivos

### Reflog

- `git reflog` → Mapeia todos os passos do usuário no repositório
- Os logs ficam salvos até expirar, que dura, por padrão, 30 dias

## seção 7 - Melhorando os commits do projeto

- Commits sem sentido atrapalham o projeto
- É necessário padronizar os commits para que o projeto cresça de forma saudável
- Commits bem feitos ajudam na hora do pull request e facilitam o entendimento dos logs

### Private branches

- `git rebase <branch_atual> <branch_da_funcionalidade> -i` → Server para passar os commits não importantes de uma branch para outra, deletando ou alterando as mensagens de todos os commits que vieram do branch de funcionalidade
- Para mexer na interface que aparece após o comando `rebase` basta apertar a tecla `i` e selecionar a linha que será modificada, podemos usar `squash` para deletar a mensagem do commit ou `reword` para alterar a mensagem, basta substituir o `pick` pelas outra opções acima

- Para salvar alterações basta apertar `esc` e digitar → `:x!`

## Seção 8 - Explorando e entendendo o Github

### Aba Issue

- Na aba issue podemos criar tarefas ou possíveis bugs do projeto
- É interessante para a organização se manter ciente do que ainda precisa fazer ou corrigir
- Deve ter uma label e um responsável

### Aba Actions

- Aba onde se cria automatizações de deploy com integração em outros serviços
- Incluindo CI/CD

### Gist

- São pequenos blocos de código que podem ser hospedados no Github
- Você pode armazenar uma solução que achou interessante para um problema e não quer perder

## Seção 9 - Markdown

### O que é Markdown

- Uma forma de adicionar estilo a textos web
- Permite exibir: trechos de códigos, links, imagens etc
- Gera uma melhor experiência para o usuário nas suas documentações

### Criando títulos

- Cabeçalhos em markdown são representados pelo símbolo `#`
- `#` → h1; `##` → h2; `###` → h3

### Ênfase no texto

- Para escrever em negrito: `**texto**` ou `__texto__`
- Para escrever em itálico: `*texto*` ou `_texto_`

### Listas

- Temos listas ordenadas e não ordenadas em markdown
- As listas não ordenadas começam com `-` ou `*`
- Para listas ordenadas começamos com números: 1. 2. etc

### Imagens

- Para inserir imagens → `![Texto alt](link da imagem)`
- Imagem pode ser externa também

### Links

- Sintaxe: `[Texto do link](link)`
- Links do github podem ser adicionados sem a sintaxe acima, apenas copiando e colando o link

### Código fonte

- Podemos inserir código no markdown
- Sintaxe: `‘’’código’’’`
