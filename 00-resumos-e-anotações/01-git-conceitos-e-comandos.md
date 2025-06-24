# Conceitos e Definições

## **Git**
VCS; Sistema de controle de versão distribuído
- gratuito e open source;
- branching e merging eficientes;
- leve e rápido.

## **GitHub**
Plataforma de hospedagem de cód p/ controle de versão com **Git**
Na tela de um repositório, ao digitar ., o GitHub abre o web editor, que é basicamente o VScode online

## Chave SSH
Funciona como uma espécie de senha/autenticador
Chave dupla (pública *.pub* e privada)

## 

---"---

## Comandos utilizados no Gith Bash
**--global** p/ usar config do usuário

**-ls** pra listar os arquivos

**-a** p/ incluir os arquivos ocultos na listagem

**cd ~/.ssh** p/ acessar o diretório principal a qualquer momento


**git init** inicializa um repositório local vazio <br>
**rm -rf .git** remove o init errado e apaga todos os arquivos do repositório iniciado erroneamente <br>
**git status** <br>
**git add .** adiciona os arquivos da pasta (o ponto adiciona todos; nome do arquivo ao invés do ponto pra mandar individualmente) <br>
**git commit -m "título do commit"** inicializa o commit (se colocar sem o -m, abre o editor pra escrever o commit no editor) <br>
**git remote add origin githhub.com/url** conecta com a url do repositório remoto <br>
**git push -u origin master/main** manda o commit do repositório local pro repositório remoto
(a cada atualização, segue apenas init > add > commit > push) <br>

**git commit --amend -m "título do commit"** altera frase do último commit (sem -m abre o editor)

**git log** mostra os commits feitos

**git reflog** histórico mais detalhados dos commits (se houver)

**touch arquivo.format** cria um arquivo

**touch pasta/.gitkeep** cria um arquivo .gitkeep dentro de uma pasta vazia, assim, mesmo sem arquivos, ela aparece no git status e pode ser commitada

**echo pastaprivada/ > .gitignore** cria o arquivo .gitignore c/ registro do título do arquivo/pasta que quer que fique oculto, pra ele não aparecer no status e não ser commitado

**git restore arquivo.format** restarua um arquivo que foi modificado; volta a uma versão anterior dele

**git reset --soft codDoCommit** reverte o commit (o Head apenas), mas mantem o staging area (index) e o working directory (código editado). Fazer antes do *push*.

**git rest --mixed codDoCommit** reverte o commit e limpa o staging area, mantendo apenas o working directory. O --mixed é o padrão, funciona direto se digitar apenas "git reset". Fazer antes do *push*.

**git reset --hard** limpa o head, o staging area e o working directory, tirando todas as mudanças não commitadas. Fazer antes do *push*.

**git checkout -b teste** "checkout" troca da branch que tava antes pra nova branch que está sendo criada "-b" e nomeada, aqui como "teste". Nesse comando não se sai totalmente da branch anterior

**git checkout main** troca pra branch já existente, nesse caso "main"

**git branch -v** lista as branchs e os últimos commits de cada uma

**git merge teste** funde a branch atual (no caso, a "main") com a branch nomeada ("teste")

**git branch -d teste** deleta a branch nomeada ("teste")

**git fetch origin main** "fetch" pra baixar as alterações feitas no repositório remoto "origin" na branch "main"

**git diff main origin** compara as diferenças entre as branches nomeadas ("main" e "origin")

**git merge origin/main** útil para baixar apenas o conteúdo da branch remota sem mesclar com a local

**git stash** arquiva modificação feita desde o último commit

**git stash list** lista as modificações arquivadas