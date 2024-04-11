from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[InputRequired("É obrigatório indicar o email")])
    password = PasswordField('Senha',
                             validators=[InputRequired("Informe sua senha")])
    remember_me = BooleanField('Lembrar de mim?')
    submit = SubmitField('Logar no sistema')