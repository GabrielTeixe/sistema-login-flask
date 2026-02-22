(Português Abaixo)

🔐 Authentication System with Flask

 English

Web authentication system built with Flask, focused on best practices, security, and a professional project structure. Ideal as a foundation for applications that require user management and access control.

🚀 Features

The system includes:

✅ User registration

✅ Login

✅ Logout

✅ Password recovery via email token

✅ Protected dashboard (authenticated users only)

✅ Secure password hashing using bcrypt

✅ SQLite database

✅ Organized templates and routing system

🛠 Technologies Used

Python 3.x

Flask

Flask-WTF (forms)

Flask-Login (user authentication)

Flask-Mail (email sending for password reset)

SQLite (lightweight embedded database)

Bcrypt (password hashing)

Jinja2 (HTML templates)

📁 Project Structure
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
├── static/
│   └── css/
├── config.py
├── run.py
└── requirements.txt
▶️ Running the Project
1. Clone the repository
git clone <URL_DO_REPOSITORIO>
cd project-name
2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Install dependencies
pip install -r requirements.txt
4. Configure email (Flask-Mail)

Edit config.py with your credentials.

5. Run the server
python run.py
6. Open in browser
http://127.0.0.1:5000


Sistema de Autenticação com Flask

Sistema de autenticação web desenvolvido com Flask, com foco em boas práticas, segurança e estrutura profissional. Ideal para servir como base para projetos web que requerem login de usuários.

Funcionalidades

O sistema inclui:

✅ Cadastro de usuários

✅ Login

✅ Logout

✅ Recuperação de senha via token enviado por e-mail

✅ Dashboard protegida (apenas para usuários autenticados)

✅ Hash de senha seguro utilizando bcrypt

✅ Banco de dados SQLite

✅ Sistema de templates e rotas organizadas

Tecnologias Utilizadas

Python 3.x

Flask

Flask-WTF (forms)

Flask-Login (autenticação de usuários)

Flask-Mail (envio de e-mails para recuperação de senha)

SQLite (banco de dados leve e integrado)

Bcrypt (hash de senhas)

Jinja2 (templates HTML)

├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       └── reset_password.html
├── static/
│   └── css/
├── config.py
├── run.py
└── requirements.txt

Como Rodar o Projeto

1.Clonar o repositório

git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto

2. Criar um Ambiente Virtual
   python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3.Instalar Dependecias
pip install -r requirements.txt
Configurar variáveis de ambiente

4.Configurar informações do e-mail para envio de token (Flask-Mail) em config.py.

Exemplo:
MAIL_SERVER = 'smtp.seuprovedor.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'seuemail@provedor.com'
MAIL_PASSWORD = 'sua_senha'

5.Rodar o Servidor 
python run.py

6.Acessar no Navegador

http://127.0.0.1:5000


   

