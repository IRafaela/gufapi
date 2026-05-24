# 🔐 Sistema de Autenticação de Usuários

Este é um projeto de **Autenticação e Autorização de Usuários** desenvolvido para servir como uma base sólida e segura para o gerenciamento de credenciais, criação de contas e proteção de rotas em aplicações modernas.

O sistema implementa práticas de segurança recomendadas pelo mercado, como criptografia de senhas e geração de tokens de acesso por tempo limitado.

---

##  Funcionalidades

* **Cadastro de Usuários:** Registro seguro com validação de dados.
* **Criptografia de Senhas:** Armazenamento seguro de senhas utilizando hash (como `bcrypt`).
* **Login & Autenticação:** Validação de credenciais e geração de tokens **JWT (JSON Web Tokens)**.
* **Rotas Protegidas:** Bloqueio de endpoints que exigem que o usuário esteja devidamente autenticado.
* **Gerenciamento de Banco de Dados:** Persistência de dados dos usuários com relacionamentos estruturados.

---

##  Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** FastAPI (Uvicorn)
* **Banco de Dados:** MySQL
* **ORM / Conectores:** SQLAlchemy ou MySQL Connector
* **Segurança:** JWT (JSON Web Tokens) & Passlib (Bcrypt)

---

##  Endpoints Principais da API

| Método | Endpoint | Descrição | Requer Token? |
| :--- | :--- | :--- | :---: |
| `POST` | `/auth/register` | Cria uma nova conta de usuário | ❌ Não |
| `POST` | `/auth/login` | Autentica o usuário e retorna o token JWT | ❌ Não |
| `GET` | `/users/me` | Retorna os dados do usuário logado atualmente | 🔒 Sim |

---



```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio
