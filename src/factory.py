import json
import os
import sys
import uuid

from flask import Flask, render_template
from src.modulos import bootstrap, minify, db, login
from src.utils import existe_esquema, seeding



def create_app(config_filename: str = 'config.dev.json'):
    app = Flask(__name__,
                instance_relative_config=True,
                template_folder='template',
                static_folder='static')


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    try:
        app.config.from_file(config_filename, load=json.load)
    except FileNotFoundError:
        app.logger.critical('Não existe o arquivo de configuração informado')
        sys.exit(1)

    bootstrap.init_app(app)
    if app.config.get ('MINIFY', False):
        minify.init_app(app)
    db.init_app(app)
    login.init_app(app)
    login.login_view ='auth.login'
    login.login_message ='Você precisa estar logado para acessar esse endereço'
    login.login_message_category ='warning'

    @login.user_loader
    def load_user(user_id):
        try:
            auth_id = uuid.UUID(str(user_id))
        except ValueError:
            return None
        sentenca = db.select(User).where(User.id == auth_id)
        usuario = db.session.execute(sentenca).scalar_one_nome()
        return usuario


    with app.app_context():
        if not existe_esquema(app):
            app.logger.critical('Efetuar a migração/upgrade do banco')
            sys.exit(1)

        if app.config.get ('SEEDING', False):
            seeding(db)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.jinja',
                               title='página inicial')
    from src.blueprints.auth import bp
    app.register_blueprint(bp)

    return app