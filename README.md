# Inventário de Ativos de TI

Sistema profissional de gerenciamento de ativos de TI desenvolvido com **FastAPI**, **PostgreSQL** e **SQLAlchemy**.

---

## Funcionalidades

| Feature | Descrição |
|---------|-----------|
| **Cadastro de Ativos** | Tag única, nome, marca, modelo, número de série, valor, data de compra |
| **Controle de Status** | Ativo, Inativo, Manutenção, Descartado, Perdido, Reservado |
| **Usuário Responsável** | Atribuição de responsável por ativo |
| **Histórico de Movimentações** | Registro completo de atribuições, transferências, manutenções e descartes |
| **Upload de Imagem** | Foto do equipamento com validação de tipo e tamanho |
| **Exportar CSV / Excel** | Download da planilha completa do inventário |
| **Busca e Filtros** | Por tag, nome, status, categoria, localização, garantia, responsável |
| **Dashboard** | Totais por status, por categoria, movimentações recentes |
| **API REST** | Endpoints documentados via Swagger UI e ReDoc |
| **Autenticação JWT** | Login seguro com token Bearer |

---

## Tecnologias

- **[FastAPI](https://fastapi.tiangolo.com/)** — Framework web moderno e performático
- **[PostgreSQL 16](https://www.postgresql.org/)** — Banco de dados relacional
- **[SQLAlchemy 2.0](https://docs.sqlalchemy.org/)** — ORM com tipagem moderna
- **[Alembic](https://alembic.sqlalchemy.org/)** — Migrations de banco de dados
- **[Pydantic v2](https://docs.pydantic.dev/)** — Validação e serialização de dados
- **[Docker / Docker Compose](https://docs.docker.com/)** — Containerização
- **[Passlib + bcrypt](https://passlib.readthedocs.io/)** — Hash seguro de senhas
- **[python-jose](https://python-jose.readthedocs.io/)** — Geração e validação JWT

---

## Estrutura do Projeto

```
inventario-ti/
├── app/
│   ├── api/
│   │   ├── deps.py               # Dependências (auth, db)
│   │   └── v1/
│   │       ├── router.py         # Roteador principal
│   │       ├── auth.py           # Login / token
│   │       ├── assets.py         # CRUD de ativos
│   │       ├── users.py          # CRUD de usuários
│   │       ├── categories.py     # CRUD de categorias
│   │       ├── movements.py      # Movimentações
│   │       └── dashboard.py      # Dashboard
│   ├── core/
│   │   ├── config.py             # Configurações (env vars)
│   │   ├── database.py           # Engine e Session SQLAlchemy
│   │   ├── security.py           # JWT e hash de senha
│   │   └── exceptions.py        # Exceções HTTP customizadas
│   ├── models/                   # Modelos SQLAlchemy
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── asset.py
│   │   └── movement.py
│   ├── repositories/             # Camada de acesso a dados
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── asset.py
│   │   └── movement.py
│   ├── schemas/                  # Schemas Pydantic (request/response)
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── asset.py
│   │   ├── movement.py
│   │   ├── dashboard.py
│   │   └── common.py
│   ├── services/                 # Regras de negócio
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── asset.py
│   │   ├── movement.py
│   │   ├── dashboard.py
│   │   └── export.py
│   ├── utils/
│   │   └── file_upload.py        # Upload e validação de imagens
│   └── main.py                   # Entrypoint FastAPI
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 001_initial_schema.py
├── scripts/
│   ├── init_db.sql               # Extensões PostgreSQL
│   └── seed_data.sql             # Dados iniciais
├── tests/
│   ├── conftest.py
│   ├── test_assets.py
│   ├── test_users.py
│   ├── test_categories.py
│   └── test_movements.py
├── uploads/                      # Imagens enviadas
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

---

## Como Executar

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/)
- **ou** Python 3.12+ e PostgreSQL instalados localmente

---

### Opção 1 — Docker Compose (recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/sua-empresa/inventario-ti.git
cd inventario-ti

# 2. Suba os containers
docker compose up -d

# 3. Acesse a API
#    Swagger UI: http://localhost:8000/docs
#    ReDoc:      http://localhost:8000/redoc
#    pgAdmin:    http://localhost:5050  (admin@admin.com / admin)
```

O docker-compose executa automaticamente:
- Criação do banco PostgreSQL
- Scripts SQL de inicialização e seed
- Migrations do Alembic
- Servidor uvicorn

---

### Opção 2 — Instalação Local

```bash
# 1. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas configurações de banco

# 4. Crie o banco de dados no PostgreSQL
createdb inventario_ti

# 5. Execute as migrations
alembic upgrade head

# 6. (Opcional) Popule com dados iniciais
psql -U postgres -d inventario_ti -f scripts/seed_data.sql

# 7. Inicie o servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## Variáveis de Ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `DATABASE_URL` | `postgresql://...` | String de conexão PostgreSQL |
| `SECRET_KEY` | — | Chave secreta JWT (obrigatório alterar em produção) |
| `ALGORITHM` | `HS256` | Algoritmo JWT |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `1440` | Expiração do token (24h) |
| `UPLOAD_DIR` | `uploads` | Diretório de imagens |
| `MAX_UPLOAD_SIZE` | `5242880` | Tamanho máximo de upload (5MB) |
| `DEBUG` | `false` | Modo debug (log SQL) |

---

## Endpoints da API

### Autenticação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/v1/auth/token` | Login — retorna token JWT |
| `GET` | `/api/v1/auth/me` | Dados do usuário logado |

### Ativos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/v1/assets/` | Listar com filtros e paginação |
| `POST` | `/api/v1/assets/` | Cadastrar ativo |
| `GET` | `/api/v1/assets/{id}` | Buscar ativo por ID |
| `PUT` | `/api/v1/assets/{id}` | Atualizar ativo |
| `PATCH` | `/api/v1/assets/{id}/status` | Atualizar status |
| `POST` | `/api/v1/assets/{id}/image` | Upload de imagem |
| `DELETE` | `/api/v1/assets/{id}` | Desativar ativo (soft delete) |
| `GET` | `/api/v1/assets/export/csv` | Exportar CSV |
| `GET` | `/api/v1/assets/export/excel` | Exportar Excel |

### Movimentações

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/v1/movements/` | Registrar movimentação |
| `GET` | `/api/v1/movements/asset/{id}` | Histórico do ativo |
| `GET` | `/api/v1/movements/recent` | Movimentações recentes |
| `GET` | `/api/v1/movements/{id}` | Buscar por ID |

### Dashboard

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/v1/dashboard/` | Resumo geral do inventário |

### Categorias e Usuários

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET/POST` | `/api/v1/categories/` | Listar / Criar |
| `GET/PUT/DELETE` | `/api/v1/categories/{id}` | Gerenciar categoria |
| `GET/POST` | `/api/v1/users/` | Listar / Criar usuário |
| `GET/PUT/DELETE` | `/api/v1/users/{id}` | Gerenciar usuário |

---

## Tipos de Movimentação

| Tipo | Descrição |
|------|-----------|
| `atribuicao` | Atribuição para um responsável |
| `devolucao` | Devolução ao estoque |
| `transferencia` | Transferência entre locais/usuários |
| `entrada_manutencao` | Envio para manutenção |
| `saida_manutencao` | Retorno da manutenção |
| `descarte` | Descarte do equipamento |
| `aquisicao` | Registro de nova aquisição |

---

## Executar Testes

```bash
# Com SQLite (sem PostgreSQL)
pytest tests/ -v

# Com cobertura
pytest tests/ -v --cov=app --cov-report=html
```

---

## Migrations Alembic

```bash
# Criar nova migration
alembic revision --autogenerate -m "descricao da mudanca"

# Aplicar migrations
alembic upgrade head

# Reverter última migration
alembic downgrade -1

# Ver histórico
alembic history
```

---

## Credenciais Padrão

> Após executar o seed ou a primeira inicialização:

| Campo | Valor |
|-------|-------|
| Email | `admin@empresa.com` |
| Senha | `Admin@123` |

**Troque a senha imediatamente em produção.**

---

## Arquitetura em Camadas

```
Request → API (Router) → Service (Regra de Negócio) → Repository (Acesso ao BD) → Model (SQLAlchemy)
                ↑
           Schema (Pydantic) — validação de entrada e saída
```

| Camada | Responsabilidade |
|--------|-----------------|
| **API** | Recebe/responde requisições HTTP, extrai parâmetros |
| **Schema** | Valida e serializa dados (Pydantic) |
| **Service** | Regras de negócio, orquestra repositórios |
| **Repository** | Queries ao banco, sem lógica de negócio |
| **Model** | Mapeamento ORM da tabela |

---

## Licença

MIT License — use à vontade para projetos comerciais e pessoais.
