from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import sqlite3

app = Flask(__name__)
app.secret_key = "segredo123"

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Configuração de email para recuperação
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'SEU_EMAIL@gmail.com'
app.config['MAIL_PASSWORD'] = 'SUA_SENHA_DE_APP'
mail = Mail(app)

serializer = URLSafeTimedSerializer(app.secret_key)

# Banco e Modelo de Usuario
class User(UserMixin):
    def __init__(self, id_, email, senha):
        self.id = id_
        self.email = email
        self.senha = senha

def get_user_by_email(email):
    conn = sqlite3.connect("instance/db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    row = c.fetchone()
    conn.close()
    if row:
        return User(row[0], row[1], row[2])
    return None

def get_user_by_id(id):
    conn = sqlite3.connect("instance/db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (id,))
    row = c.fetchone()
    conn.close()
    if row:
        return User(row[0], row[1], row[2])
    return None

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)

# Rotas
@app.route('/')
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        senha = bcrypt.generate_password_hash(request.form["senha"]).decode("utf-8")

        conn = sqlite3.connect("instance/db.sqlite3")
        c = conn.cursor()
        c.execute("INSERT INTO users (email, senha) VALUES (?, ?)", (email, senha))
        conn.commit()
        conn.close()

        flash("Conta criada com sucesso!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        user = get_user_by_email(email)

        if user and bcrypt.check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Email ou senha incorretos!", "danger")

    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user.email)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

# Recuperar senha
@app.route("/reset", methods=["GET", "POST"])
def reset():
    if request.method == "POST":
        email = request.form["email"]
        user = get_user_by_email(email)

        if user:
            token = serializer.dumps(email, salt="senha-reset")

            link = url_for("reset_token", token=token, _external=True)

            msg = Message("Recuperação de Senha",
                          recipients=[email],
                          body=f"Clique no link para redefinir sua senha: {link}")
            mail.send(msg)

            flash("Um email foi enviado para recuperação!", "info")
            return redirect(url_for("login"))

    return render_template("reset_password.html")

@app.route("/reset/<token>", methods=["GET", "POST"])
def reset_token(token):
    try:
        email = serializer.loads(token, salt="senha-reset", max_age=3600)
    except:
        flash("Token inválido ou expirado!", "danger")
        return redirect(url_for("login"))

    if request.method == "POST":
        nova_senha = bcrypt.generate_password_hash(request.form["senha"]).decode("utf-8")

        conn = sqlite3.connect("instance/db.sqlite3")
        c = conn.cursor()
        c.execute("UPDATE users SET senha=? WHERE email=?", (nova_senha, email))
        conn.commit()
        conn.close()

        flash("Senha redefinida com sucesso!", "success")
        return redirect(url_for("login"))

    return render_template("reset_password.html")

if __name__ == "__main__":
    conn = sqlite3.connect("instance/db.sqlite3")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, senha TEXT)"
    )
    conn.commit()
    conn.close()

    app.run(debug=True)
