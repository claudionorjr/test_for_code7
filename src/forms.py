from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField, DecimalField
from wtforms.fields import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import Length, Email, DataRequired, Regexp, Optional


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Length(5, 80, "Email deve conter entre 5 a 80 caracteres."),
        Email('Digite um email válido.')
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "Senha deve conter entre 3 a 6 caracteres.")
    ])
    submit = SubmitField("Logar")


class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        Length(5, 80, "Nome deve conter entre 5 a 80 caracteres."),
        DataRequired("Campo Obrigatório.")
    ])
    email = EmailField("Email", validators=[
        Email('Digite um email válido.'),
        Length(5, 80, "Email deve conter entre 5 a 80 caracteres."),
        DataRequired("Campo Obrigatório.")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "Campo deve conter entre 3 a 6 caracteres."),
        DataRequired("Campo Obrigatório.")
    ])
    submit = SubmitField("Registrar")


class NewDebitForm(FlaskForm):
    reason = StringField("Motivo", validators=[
        Length(5, 35, "Motivo deve conter entre 5 a 35 caracteres."),
        DataRequired("Campo Obrigatório.")
    ])
    debit_date = DateField("Data", format="%d/%m/%Y", validators=[
        DataRequired("Campo Obrigatório.")
    ], render_kw={"placeholder": "Ex: dd/mm/aaaa"})
    amount = StringField("Valor", validators=[
        Regexp(regex=r'^[0-9]*[.,]{0,1}[0-9]*$', message="Digite um valor válido."),
        DataRequired("Campo Obrigatório.")
    ], render_kw={"placeholder": "Ex: 1550.50"})
    submit = SubmitField("Novo Débito")

class EditDebitForm(FlaskForm):
    reason = StringField("Motivo", validators=[
        Length(0, 35, "Motivo deve conter entre 5 a 35 caracteres.")
    ])
    debit_date = DateField("Data", format="%d/%m/%Y", render_kw={"placeholder": "Ex: dd/mm/aaaa"}, validators=[Optional()

    ])
    amount = StringField("Valor", validators=[
        Regexp(regex=r'^[0-9]*[.,]{0,1}[0-9]*$', message="Digite um valor válido.")
    ], render_kw={"placeholder": "Ex: 1550.50"})
    submit = SubmitField("Atualizar Débito")
