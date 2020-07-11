from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from data.sql_alchemy import database as db
from src.models.user import UserModel
from .forms import LoginForm, RegisterForm
from .users import get_users


def session_to_add(obj):
    db.session.add(obj)
    db.session.commit()

def session_to_delete(obj):
    db.session.delete(obj)
    db.session.commit()


def init_routes(app):
    @app.route("/", methods=["GET","POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = UserModel.query.filter_by(email=form.email.data).first()

            if not user:
                flash(message="Erro, dados incorretos.", category="warning")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, form.password.data):
                flash(message="Erro, dados incorretos.", category="warning")
                return redirect(url_for("login"))

            login_user(user)
            return redirect(url_for("home"))

        return render_template("login.html", form=form)

    @app.route("/register", methods=["GET","POST"])
    def register():
        form = RegisterForm()
        
        if form.validate_on_submit():
            user = UserModel()
            user.name = form.name.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)

            try:
                session_to_add(user)
                flash(message="Usuário criado com sucesso!", category="success")
            except:
                flash(message="Erro, email já cadastrado.", category="warning")
                return redirect(url_for("register"))

            return redirect(url_for("login"))

        return render_template("register.html", form=form)

    @app.route("/current_user")
    @login_required
    def home():
        users = get_users()
        return render_template("home.html", users=users)

    @app.route("/current_user/account")
    @login_required
    def account():
        return render_template("account.html")

    @app.route("/current_user/delete")
    @login_required
    def delete_confimation():
        return render_template("delete_confimation.html")

    @app.route("/current_user/delete/<int:id>")
    @login_required
    def delete_user(id):
        user = UserModel.query.filter_by(id=id).first()
        try:
            session_to_delete(user)
            logout_user()
        except:
            flash(message="Erro ao deletar.", category="danger")

        return redirect(url_for("login"))

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login"))

    @app.route("/about_debits")
    @login_required
    def about_debits():
        users = get_users()
        return render_template("about_debits.html", users=users)