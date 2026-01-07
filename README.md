# Backend de Delivery

Este é um backend simples para um sistema de delivery, desenvolvido com FastAPI. Ele permite gerenciar usuários, autenticação e pedidos de delivery.

## Funcionalidades

- **Autenticação de usuários**: Rotas básicas para autenticação.
- **Gerenciamento de pedidos**: Rotas para criar e gerenciar pedidos de delivery.
- **Banco de dados**: Usa SQLite com SQLAlchemy para armazenar dados de usuários, pedidos e itens dos pedidos.

## Tecnologias Utilizadas

- **FastAPI**: Framework para criar APIs rápidas e modernas.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **Alembic**: Ferramenta para migrações do banco de dados.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.
- **Outros**: PassLib para hashing de senhas, Python-JOSE para JWT, etc.

## Estrutura do Projeto

```
delivery_backend/
├── main.py              # Arquivo principal da aplicação FastAPI
├── models/
│   ├── model_db.py      # Definições dos modelos do banco de dados (Usuario, Pedido, ItemPedido)
├── routes/
│   ├── auth_routes.py   # Rotas de autenticação
│   ├── order_routes.py  # Rotas de pedidos
├── alembic/             # Configurações e versões das migrações
├── pyproject.toml       # Dependências e configurações do projeto
└── README.md            # Este arquivo
```

## Instalação e Configuração

1. **Clone o repositório** (se aplicável) e navegue até a pasta do projeto.

2. **Instale as dependências**:
   ```bash
   uv sync
   ```

3. **Configure o banco de dados**:
   - O banco usado é SQLite (`database.db`).
   - Execute as migrações iniciais:
     ```bash
     uv run alembic upgrade head
     ```

## Como Rodar a Aplicação

Para iniciar o servidor de desenvolvimento:

```bash
uv run uvicorn main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

- **Documentação da API**: Acesse `http://127.0.0.1:8000/docs` para ver a documentação interativa gerada pelo FastAPI.

## Migrações do Banco de Dados

O projeto usa Alembic para gerenciar mudanças no banco de dados.

### Criar uma nova migração:
```bash
uv run alembic revision --autogenerate -m "descrição da migração"
```

### Aplicar migrações:
```bash
uv run alembic upgrade head
```

### Exemplo: Remover uma coluna
1. Faça as mudanças no código dos modelos (em `models/model_db.py`).
2. Gere a migração: `uv run alembic revision --autogenerate -m "remover coluna"`
3. Aplique: `uv run alembic upgrade head`

## Endpoints da API

### Autenticação (`/auth`)
- `GET /auth/`: Verifica acesso à rota de autenticação (básico).

### Pedidos (`/pedidos`)
- `GET /pedidos/`: Lista pedidos (básico).

*Nota*: As rotas estão em desenvolvimento. Consulte a documentação em `/docs` para detalhes atualizados.

## Modelos do Banco de Dados

- **Usuario**: Armazena informações de usuários (id, email, nome, senha, ativo).
- **Pedido**: Representa um pedido (id, status, usuário, preço).
- **ItemPedido**: Itens de um pedido (quantidade, sabor, tamanho, preço unitário, pedido).

## Contribuição

Para contribuir:
1. Faça um fork do projeto.
2. Crie uma branch para sua feature.
3. Commit suas mudanças.
4. Abra um Pull Request.

## Licença

Este projeto é de código aberto. Consulte o arquivo de licença para mais detalhes.