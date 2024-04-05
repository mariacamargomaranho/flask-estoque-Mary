from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

def existe_esquema(app) -> bool:
    # Se estivéssmos com um SGBD, poderíamos consultar os metadados para ver
    # se o esquema do banco existe, com algo como (mariaDB)
    # SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '<nome>'
    # No caso do SQLite, vamos apenas verificar se existe ou não o arquivo no
    # sistema de arquivos
    arquivo = Path(app.instance_path) / Path(app.config.get('SQLITE_DB_NAME', 'application_db.sqlite3'))
    return arquivo.is_file()
    # configurar o alembic
    #   alembic init instance/migrations
    # configurar o alembic.ini
    #   [alembic]
    #   sqlalchemy.url = sqlite+pysqlite:///instance/application_db.sqlite3
    # ajustar o env.py
    #   from src.modules import Base
    #   target_metadata = Base.metada

def seeding(db:SQLAlchemy):
    from src.models.usuario import User

    senteca = sa.select(User).limit(1)
    rset = db.session.execute(senteca).scalar_one_or_none()
    if rset is None:
        usuario = User()
        usuario.nome = "Administrador do sistema"
        usuario.email = "admin@admin.com.br"
        usuario.set_password("admin")
        db.session.add(usuario)
        db.session.commit()



