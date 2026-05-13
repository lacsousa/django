# BDPrático - Django Framework

Projeto da Disciplina Frameworks - Pós-Graduação em Agentes e Sistemas Inteligentes - UFG

Uma aplicação Django para gerenciamento de dados com funcionalidades de autenticação, CRUD de pessoas, procedimentos e exames, além de importação de dados via upload de arquivos.

---

## 📋 Requisitos

- Python >= 3.12
- UV (gerenciador de pacotes Python)

## 🔧 Configuração Inicial

### 1. Instalar UV

O UV é um gerenciador de pacotes rápido e confiável para Python. Para instalá-lo:

```bash
# No Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# No Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verifique a instalação:
```bash
uv --version
```

### 2. Clonar o Repositório

```bash
git clone <url-do-repositório>
cd django
```

### 3. Instalar Dependências

```bash
uv sync
```

---

## 🚀 Executando o Projeto

### Iniciar o Servidor de Desenvolvimento

```bash
uv run python manage.py runserver
```

O servidor estará disponível em: `http://localhost:8000` ou `http://127.0.0.1:8000`

---

## 📚 Principais Comandos Django com UV

### Migrações do Banco de Dados

```bash
# Criar novas migrações
uv run python manage.py makemigrations

# Aplicar migrações ao banco de dados
uv run python manage.py migrate

# Ver status das migrações
uv run python manage.py showmigrations
```

### Gerenciamento de Usuários

```bash
# Criar superusuário (administrador)
uv run python manage.py createsuperuser

# Criar usuário comum
uv run python manage.py shell
# Dentro do shell:
# >>> from django.contrib.auth.models import User
# >>> User.objects.create_user(username='user', password='pass')
```

### Shell Interativo do Django

```bash
# Abrir shell para interagir com o banco de dados
uv run python manage.py shell

# Exemplo de uso no shell:
# >>> from exemplo01.models import Pessoa
# >>> Pessoa.objects.all()
# >>> Pessoa.objects.create(nome='João', email='joao@example.com')
```

### Testes

```bash
# Executar todos os testes
uv run python manage.py test

# Executar testes de um app específico
uv run python manage.py test exemplo01

# Executar com verbosidade
uv run python manage.py test --verbosity=2
```

### Administração

```bash
# Coletar arquivos estáticos (para produção)
uv run python manage.py collectstatic
```

---

## ✨ Funcionalidades Principais

### 1. **Autenticação de Usuários**
- Login e logout de usuários
- Gerenciamento de sessões
- Integração com Django Auth
- Página de autenticação: `http://localhost:8000/`

### 2. **Gerenciamento de Pessoas (CRUD)**
- Listar pessoas
- Criar nova pessoa
- Atualizar dados de pessoa
- Deletar pessoa
- Campos: Nome, E-mail, Celular, Função, Data de Nascimento, Status (ativo/inativo)

**Endpoints:**
- `GET /exemplo01/pessoa_list/` - Listar pessoas
- `GET /exemplo01/pessoa_create/` - Formulário de criação
- `GET /exemplo01/pessoa_update/<id>/` - Formulário de edição
- `GET /exemplo01/pessoa/delete/<id>/` - Deletar pessoa

### 3. **Menu de Navegação**
- Interface intuitiva com acesso às principais funcionalidades
- Páginas de exemplo (0-12)
- Acesso ao admin do Django: `http://localhost:8000/admin/`

**Endpoints:**
- `GET /exemplo01/menu` - Menu principal
- `GET /exemplo01/pessoa_menu` - Menu de pessoas

### 4. **Gerenciamento de Procedimentos e Exames**
- Registro de procedimentos executados
- Importação e gerenciamento de exames
- Modelos: `Procedimento`, `ProcedimentoExecutado`, `Exame`

### 5. **Importação de Dados via Upload**
- Upload de arquivos CSV/TXT com dados de exames
- Parse automático dos dados
- Armazenamento no banco de dados
- Validação de permissões de usuário

**Endpoint:**
- `POST /exemplo01/pagina11` - Upload de arquivo de exames

### 6. **Tabelas Interativas**
- Utiliza `django-tables2` para exibição de dados
- Paginação automática
- Ordenação de colunas

### 7. **Controle de Permissões**
- Controle granular de acesso por usuário
- Verificação de permissões antes de operações sensíveis (add, delete, update)
- Integração com Django Permissions

---

## 🗄️ Modelos de Dados

### Pessoa
```
- nome (CharField)
- email (EmailField)
- celular (CharField)
- funcao (CharField)
- nascimento (DateField)
- ativo (BooleanField)
```

### Procedimento
```
- descrição do procedimento
```

### ProcedimentoExecutado
```
- referência ao Procedimento
- data de execução
```

### Exame
```
- valor (FloatField)
```

---

## 📊 Páginas de Exemplo

O projeto inclui várias páginas de exemplo para demonstrar funcionalidades:

- **Página 0-10:** Exemplos básicos do framework
- **Página 11:** Upload/Importação de arquivos de exames
- **Página 12:** Página adicional de demonstração

---

## 🔐 Configurações de Segurança

### CSRF Protection
Todas as requisições POST requerem um CSRF token válido. Os templates incluem `{% csrf_token %}` automaticamente.

### Trusted Origins (CSRF)
Configuradas as seguintes origens confiáveis:
- `http://localhost:8000`
- `http://127.0.0.1:8000`
- `https://localhost:8000`
- `https://127.0.0.1:8000`

### Debug Mode
Atualmente em `DEBUG = True` para desenvolvimento. **Mude para `False` em produção!**

---

## 📁 Estrutura do Projeto

```
django/
├── bdpratico/              # Configurações principais do Django
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py            # URLs principais
│   ├── wsgi.py            # Interface WSGI
│   └── asgi.py            # Interface ASGI
├── exemplo01/             # App principal
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Visualizações
│   ├── urls.py            # URLs do app
│   ├── admin.py           # Admin configurado
│   ├── templates/         # Templates HTML
│   └── migrations/        # Migrações do banco
├── exemplo02/             # App adicional
├── config/                # Configurações alternativas
├── core/                  # Funcionalidades centrais
├── manage.py              # Script de gerenciamento
├── requirements.txt       # Dependências
├── pyproject.toml         # Configuração do projeto
└── db.sqlite3             # Banco de dados SQLite
```

---

## 🛠️ Troubleshooting

### Erro 404 ao acessar rotas
Verifique se as URLs estão corretamente configuradas em `bdpratico/urls.py` e `exemplo01/urls.py`.

### Erro de CSRF (403)
Certifique-se de que:
1. O template inclui `{% csrf_token %}`
2. A origem está em `CSRF_TRUSTED_ORIGINS` no settings.py
3. As cookies estão habilitadas no navegador

### Banco de dados desatualizado
Execute as migrações:
```bash
uv run python manage.py migrate
```

---

## 📝 Desenvolvedor

Projeto desenvolvido como trabalho da disciplina de Frameworks, por Luciano Cordeiro.

---

## 📄 Licença

Projeto educacional da Universidade Federal de Goiás (UFG).
