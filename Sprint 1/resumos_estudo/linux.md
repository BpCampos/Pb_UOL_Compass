# Linux

## Seção 1

- Utilizaremos a distribuição `Ubuntu` do Linux
- Através da `Virtual Machine` da Oracle, alocamos um pouco da capacidade de processamento do computador físico para utilização da máquina virtual. Dentro da máquina virtual foi instalado o sistema operacional do Linux Ubuntu, versão gratuita
- Podemos escolher a quantidade de `RAM`, o espaço de `armazenamento` e a quantidade de `processadores` que a máquina virtual vai utilizar

## Seção 2

- A distribuição `Ubuntu` é a mais utilizada no mercado e a mais recomendada para iniciantes, tendo em vista que ela é utilizada também para a criação de servidores na AWS
- `Kernel`:
  - É o core do sistema
  - Gerencia CPU, memória e etc
  - Faz a ligação entre usuário e hardware
  - Programado em C e Assembly

### Por que usar o Linux?

- A distribuição mais popular do Linux é grátis
- Utilizado na maioria dos servidores web
- Requisitos para muitas vagas
- Comunidade ativa
- Segurança, os servidores mais seguros são Linux
- Suporte nativo para muitas linguagens

## Seção 3

### Terminal e Shell

- O shell executa os comandos digitados no terminal
- `Padrão para mexer no shell` → COMANDO -OPÇÕES ARQUIVOS/DIRETORIOS

```bash
#Usamos o comando 'ls' com a opção '-ltr' no diretório 'Downloads', para listar os arquivos dentro de Downloads
ls -ltr Donwloads
```

- No Linux o diretório ‘/’ é o raiz, não existe nenhum antes dele

### Comandos

- `cd` → change directory, navega entre os diretórios da máquina. usando a `‘/’` podemos sair de um diretório e ir para outro totalmente diferente e.g. `/var/log/` independente de onde estivermos, podemos ir para var → log usando a `/` , sem a barra o Linux entende que queremos acessar algo no diretório que estamos no momento
- Ações avançadas do `cd`:
  - `cd -` → Leva para o último diretório e mostra na tela do terminal qual era o último diretório
  - `cd ~` → Vai para a home do usuário
  - `cd <diretorio> && ls` → Vai até o diretório especificado e executa o comando ls, podemos usar dois comandos por conta do `&&`
  ***
- `ls` → list, lista todos os arquivos e diretórios dentro de diretório específico
- podemos usar opções junto do `ls`, como `-l` por exemplo que traz mais informações sobre os arquivos e diretórios
- `ls -a` → Mostra também os arquivos ocultos
- Podemos combinar comandos como: `ls -la` para listar os ocultos de forma detalhada
- `ls -ltr` → Mostra os arquivos pela data da ultima alteração
- `ls -l /etc` → Lista os arquivos do diretório `etc` de forma detalhada
- Ações avançadas do `ls`:
  - `ls -lr /etc` → Usar o `r` de reverse para listar os arquivos em ordem reversa
  - `ls -lS` → Usando o `S` maiúsculo, podemos ordenar os arquivos por tamanho

---

- `cat <arquivo>` → Mostra o conteúdo dentro do arquivo, por exemplo o texto escrito dentro de um arquivo de notas
- Pode ser usado também para `juntar 2 arquivos em um novo`, o novo arquivo vai conter o conteúdo dos outro dois → `cat arquivo1 arquivo2 > arquivo3`
- Usando `cat arquivo4 >> arquivo3`, podemos adicionar o conteúdo do arquivo4 ao final do arquivo3

---

- `touch` → Cria um arquivo no diretório atual

---

- `man` → Manual do sistema, pode ser usado junto de outros comandos e mostra como aquele comando funciona e.g. `man ls`

## Seção 4 - Gerenciamento de diretórios

### Comandos

- `mkdir <nomeDoDiretorio>` → make directory, cria um diretório no caminho atual. Podemos criar mais de um diretório por vez
- Usando o -v, podemos ter mais informações sobreo o comando mkdir → `mkdir -v teste1`
- Podemos criar um diretório já com outro dentro dele, usando `mkdir dir1/dir2`, porém apenas podemos criar um
- Para criarmos mais do que 1, podemos usar `mkdir -p` e.g. `mkdir -v dir5/dir6/dir7/dir8`
- `mkdir ../dir10` → Volta um diretório e cria um

---

- `rm` → `remove`, apaga um arquivo, é possível apagar um conjunto deles
- `rm -dv` → Remove diretórios vazios
- `rm -rfv` → Remove diretórios que tenham arquivos e ou diretórios dentro dele
- `rmdir` → É um comando específico para remover diretórios

---

- `cp <arquivo> <diretório>` → Cria uma cópia de um arquivo em armazena no diretório selecionado e.g. `cp c.txt dir5` → cria uma cópia do arquivo c.txt no diretório dir5
- Podemos copiar mais de um arquivo para um outro diretório
- `cp -r <diretorioCriado> <novoDiretorio>` → Usando a flag `-r` podemos criar cópias de diretórios, com todos os arquivos do diretório base
- Podemos usar a flag `*` para copiar tudo que está dentro de um diretório

```bash
#Aqui estamos copiando tudo que está dentro de dir5 e passando para o dirTeste criado
cp -r dir5/* dirTeste
```

- Para o caso de arquivos, o `*` copia todos os arquivos que contiverem o mesmo nome do que o passado antes do `*` e.g. doc2.txt doc1.txt doc3.txt → o comando `cp doc* dirTeste` passa todos os arquivos doc para o dirTeste

---

- `mv` → `move`, move um arquivo de um diretório para outro, serve também para renomear arquivos
- Podemos mover todos arquivos de um diretório para outro usando a flag `*` → `mv * dir5`

## Seção 5 - Gerenciar pacotes

### Atualizando pacote

- É recomendado realizar atualizações pelo menos uma vez por mes
- `sudo apt-get <comando>` → Comando padrão para manipular aplicativos no Linux
- O `sudo` permite que ganhemos permissões extras para poder mexer no sistema que normalmente não seriam concedidas à usuários normais
- `sudo apt-get update` → Atualiza a lista de pacotes e suas versões, porém não instala nada
- `sudo apt-get upgrade` → De fato atualiza os pacotes para sua versões mais novas
- É recomendado utilizar o `update` antes do `upgrade`

### Instalando pacotes/aplicativos

- `sudo apt-get install <nomeDoPrograma>` → Permite instalar um ou mais programas
- O aplicativo `tree` facilita a visualização dos arquivos e diretórios
- `sudo apt-get purge <nomeDoPrograma>` → Deleta um ou mais programas

### Limpando pacotes/aplicativos

- `sudo apt-get autoremove` → Busca aplicativos que não são mais utilizados no nosso sistema e os remove. Aconselhado a rodar este comando uma vez por mês

### Buscando aplicativos

- `apt-cache search <nomeDoAplicativo>` → O Linux procura a partir do nome passado, pacotes/aplicativos relacionados ao nome passado

---

- Na versão mais nova do Linux, podemos ocultar o `-get` do comando `apt-get` para apenas `apt` → `sudo apt install`

## Seção 6 - Filtro e buscas de arquivos e diretórios

- Encontrar arquivos/textos e buscas mais inteligentes
- `head <arquivo>`→ Mostra apenas uma parte do arquivo começando do início, para dar uma noção do que se trata o arquivo
- `head -n 1 <arquivo>` → Mostra apenas a primeira linha do arquivo, podemos mudar o numero de linhas apresentadas
- Podemos usar os mesmos métodos do `cat` no `head` como, criar um novo arquivo com informações de outro arquivo

---

- `tail <arquivo>` → Funciona como o inverso do `head` e nos permite ver o final do arquivo
- `tail -f <arquivo>` → Toda vez que o arquivo no qual o `tail` foi utilizado for alterado, nós conseguiremos ver as alterações de forma automática já que elas aparecerão do final do arquivo, a utilização do `-f` tem grande importância na hora de conferir `logs de erros`

---

- `grep 'palavra' <arquivo>` → Procura dentro de um arquivo a palavra passada
- O `grep` é case sensitive, por isso só irá achar a palavra exata que o usuário digitar
- Ao adicionar a flag `-i` em `grep -i`, conseguiremos achar palavra digitada em qualquer formato que ela estiver

---

- `find -name 'nomeDoArquivo'` → Encontra o arquivo especificado pelo nome exato passado, mostrando o caminho dele
- `find -iname ‘nomeDoArquivo’` → Encontra o arquivo ignorando o fato de ele ser case sensitive
- Usando o `*` junto do nome do arquivo, podemos encontrar todos os arquivos que começam com a palavra digita e.g. `document*` → encontra todos os arquivos que começam com `document`
- `find -empty` → Mostra todos os diretórios e arquivos que estão vazios. Podemos filtrar o resultado encontrado usando `-type f` ou `d` para achar apenas arquivos ou diretórios vazios; `find -empty -type f/d`

---

- Usando o `!!` podemos reutilizar o comando digitado anteriormente sem chamar ele de fato
- `which <comando>` → Mostra de onde vem o comando que estamos passando

## Seção 7 - Editores de texto mais utilizados

### Nano

- Para entrar no editor de texto, basta apenas digitar nano no terminal
- `ctrl + o` → Salva o arquivo e te deixa nomea-lo
- `ctrl + x` → Sai do nano
- `ctrl + r` → Adiciona o conteúdo de um arquivo externo dentro do arquivo atual
- `alt + a` → Marca o texto selecionado
- `alt + 6` → Copia o texto
- `ctrl + u` → Cola o texto no local desejado
- `ctrl + k` → Recorta o texto
- `ctrl + w` → Permite procurar palavras por um prompt e leva para a primeira ocorrência da palavra no arquivo
- `alt + r` → Comando para substituir palavras

### Vim

- `sudo apt install vim` → Instala o Vim
- Ele tem dois modos: Insert, apertando `i` no teclado; E `esc` para o modo de comandos
- Para salvar e sair do arquivo → No modo de comandos, digite `:x`
- Para salvar um arquivo, no modo comandos digite `:w`; Para sair do editor, digite `:q`
- Para deletar um linha inteira, no modo comando, aperte duas vezes `d`
- Para desfazer uma alteração, no modo comando aperte `u`

### Seção 8 - Gerenciamento de usuários e grupos

### Usuários

- `sudo adduser <nomeDoUsuario>` → Adiciona um usuário ao sistema
- `sudo userdel —remove <nomeDoUsuario>` → Remove um usuário do sistema
- `sudo usermod -c  ‘novoNome’ <nomeAntigo>` → Altera o nome do dado ao usuário na hora da criação
- `sudo usermod -l <novoNome> -d /home/<novoNome> -m <nomeAntigo>` → Altera o nome do usuário dentro do sistema, assim como o nome do seu diretório na pasta home
- `sudo usermod -L <nomeDoUsuario>` → Bloqueia o usuário, não permitindo ele de acessar sua conta e seus diretórios
- `sudo usermod -U <nomeDoUsuario>` → Desbloqueia o usuário

### Grupo

- Contém vários usuários e facilita gerenciar permissões
- `getent group` → Lista todos os grupos do sistema
- `sudo groupadd -g <ID_Do_Grupo> <nomeDoGrupo>` → Cria um novo grupo com ID e nome específicos
- `sudo groupdel <nomeDoGrupo>` → Apaga o grupo
- `sudo usermod -a -G <nomeDoGrupo> <nomeDoUsuario>` → Muda o usuário de um grupo para outro
- `sudo gpasswd -d <nomeDoUsuario> <nomeDoGrupo>` → Deleta um usuário específico de um grupo

---

- `passwd` → Permite mudar a senha do usuário

## Seção 9 - Gerenciamento de permissões

### O que são

- Possibilidade de alterar 3 propriedades do arquivo:
- `leitura` → Se os usuários poderão ler o arquivo (R - read)
- `escrita` → Se os usuários poderão escrever no arquivo (W - write)
- `execução` → Se os usuários poderão executar o arquivo (X - execute)

### Permissões

- 1 222 333 444
- `1` → Diretório ou arquivo
- `222` → Permissões do owner (dono)
- `333` → Permissões do grupo (que o arquivo pertence)
- `444` → Permissões dos demais usuários (que não são donos nem fazem parte do grupo)
- Traduzindo para como será mostrado no Linux → `drwxr-xr-x`: É um diretório onde o dono tem todas as permissões, o grupo pode apenas ler e executar (r-x) e os usuários pode apenas ler e executar também (r-x)
- `d`→ Diretório, se no lugar do `d` for um `-` significa que é um arquivo
- `r` → read
- `w` → write
- `x` → execute
- `-` → não há permissão

### Alterando permissões

- Comando para executar as permissões: `chmod xxx file/dir`
- Onde ‘x’ representa as permissões em números e cada `x` representa `owner`; `grupo`; `usuário` respectivamente
- `0` → Sem permissões - - -
- `1` → Executar - - x
- `2` → Escrever - w -
- `3` → Ler e Executar - w x
- `4` → Ler r - -
- `5` → Ler e executar r - x
- `6` → Ler e escrever r w -
- `7` → Ler escrever e executar r w x

### Alterar owner do arquivo

- `chown <novoUsuario> <arquivo>` → Altera o dono do arquivo
- `chgrp <nomeDoGrupo> <arquivo>` → Altera o grupo do arquivo

- `ctrl + shift + c` → Copia um conteúdo no terminal
- `ctrl + shift + v` → Cola o conteúdo
- `history` → Mostra o histórico do terminal

## Seção 10 - Gerenciamento básico de redes

- Portas são basicamente `endpoints` que nos permite conectar com site para executar processos diferentes dependendo da porta
- Porta `80` → Para requisições HTTP
- Porta `20` → Para transferência de arquivos
- Porta `443` → Para HTTPS

### Comandos

- `ping` → Para saber se estamos conectados à internet e se temos perda de pacote ou se podemos nos conectar a um site específico
- `netstat` → Mostra as conexões de rede do nosso sistema
- `ifconfig` → Mostra as interfaces de rede
- `hostname -I` → Mostra o nosso `IP`

## Seção 11 - Compactação e descompactação de arquivos e diretórios

- `tar -czvf compactado.tar.gz <nomeDoArquivoOuDir>` → Cria um arquivo compactado chamado `compactado.tar.gz` contendo o arquivo ou diretório passado. Podemos passar mais de um arquivo ou diretório
- `tar -xzvf <nomeDoArquivo>` → Descompacta o arquivo no diretório atual
- Para compactar arquivos em `.zip` → `zip -r <nomeDoNovoArquivoZip>.zip <nomeDoArquivo>`
- Descompactar arquivos `zip` → `unzip <nomeDoNovoArquivoZip> -d <destinoDoConteudo>`

## Seção 12 - LAMP

- `sudo apt install apache2` → Instala o servidor apache
- `sudo apt install mysql-server` → Instala o mysql
- `sudo mysql_secure_installation` → Assegura a instalação do MySQL Server no Linux
- `sudo apt install php libapache2-mod-php php-mysql php-cli` → Instala todas as dependências necessárias para se utilizar o php
