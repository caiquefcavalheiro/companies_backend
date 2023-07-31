# Backend Empresas

Nesta API o usuário será capaz de fazer todo o CRUD de usuários e empresas e terá uma rota de login, para ter permissão em alguns acessos.

## Configurações

Para iniciar o projeto, é necessário criar um ambiente virtual, após clonar o projeto abra o terminal no vscode dentro do projeto e digite:

```bash
python -m venv venv
```

Em seguida, entre no ambiente virtual:

### Linux:

```bash
Source venv/bin/activate
```

### Windows

```bash
.\venv\Scripts\activate
```

ou

```bash
source venv/Scripts/activate
```

Após entrar no ambiente virtual execute os comandos para instalar as bibliotecas do projeto

```bash
pip install -r requirements.txt
```

Agora antes de iniciar o projeto precisamos configurar as variáveis de ambiente.

Criei um arquivo na raiz do projeto com o nome de .env e copie todas as variáveis contidas em no arquivo .env.example

Na variável **SQLALCHEMY_DATABASE_URI** do seu arquivo .env, coloque a url do seu banco de dados postgres, no formato indicado, **postgresql:username:password@localhost:5432/database**

Substituia os campos **username**, **password** e **database** pelos do seu banco de dados.

Agora com a variável de ambiente configurada, precisando persistir as mudanças na tabela no banco de dados configurado.

```bash
flask db upgrade
```

## Ligando a API

Para iniciar o projeto agora basta digitar

```bash
flask run
```

E o projeto será iniciado na porta **http://127.0.0.1:5000**

A documentação será encontrada na porta **http://127.0.0.1:5000/docs**

Nos arquivos da aplicação também se encontra um arquivo **insomnia_companies.json**, já tendo toda automatização de rotas lá
