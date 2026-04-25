# Resumo de Comandos do UV


## Criar ambiente virtual
- `uv init`: Inicializa um novo projeto gerenciado pelo uv, criando o ambiente virtual e arquivos de configuração (como `pyproject.toml`).
- `uv venv`: Cria um novo ambiente virtual python isolado no diretório atual (geralmente em `.venv`).


## Instalação dos requirements
- `uv add django`: Adiciona o pacote Django como dependência do projeto e o instala no ambiente virtual automaticamente.
- `uv list` / `uv pip list`: Lista todos os pacotes e dependências instaladas no ambiente atual.


## Criação do Requirements
- `uv pip freeze > requirements.txt`: Cria o arquivo com todas as dependências necessárias ao projeto agora


## Execução do projeto
- `uv run django-admin startproject <nome> .`: Executa o utilitário do Django para criar a estrutura inicial do projeto no diretório atual. O "." é para não criar uma outra pasta config dentro da pasta config

- `uv run python manage.py startapp <nome>`: Cria a estrutura de um novo aplicativo dentro do projeto Django.

- `uv run python manage.py makemigrations`: Gera os arquivos de migração baseados nas alterações feitas nos modelos do projeto.

- `uv run python manage.py migrate`: Aplica as migrações geradas no banco de dados.

- `uv run python manage.py createsuperuser`: Inicia o prompt para criação de um usuário administrador para acessar o painel administrativo (Admin) do Django.

- `uv run python manage.py runserver`: Inicia o servidor de desenvolvimento local do Django para rodar o projeto.


## Comandos Django - Aula 1 (Framework-aula-1.pdf)

- `uv run python -m django --version`: Verifica se o Django está instalado e exibe a versão atual.

- `uv run python manage.py makemigrations exemplo01`: Gera os arquivos de migração para o app `exemplo01` especificamente, com base nas alterações feitas no seu `models.py`.

- `uv run python manage.py migrate`: Aplica ao banco de dados todas as migrações pendentes do projeto.

- `uv run python manage.py createsuperuser`: Cria interativamente um usuário administrador para acessar o painel Admin do Django.

- `uv run python manage.py runserver`: Inicia o servidor de desenvolvimento local do Django.


## Comandos Django - Aula 2 (Framework-aula-2.pdf)

- `uv add django-tables2`: Instala o pacote `django-tables2`, que permite criar tabelas HTML dinâmicas e paginadas a partir de models ou querysets Django.

- `pip install django-bootstrap-v5`: Instala o pacote de integração do Bootstrap 5 com Django (via tags de template). Observação: este pacote suporta apenas Django até a versão 4.x. Em projetos com Django 5+, use Bootstrap via CDN diretamente nos templates HTML.

