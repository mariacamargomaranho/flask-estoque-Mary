import uuid

from flask_login import UserMixin
from sqlalchemy.orm  import mapped_column, Mapped
from sqlalchemy.types import Uuid, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from src.modulos import db
from src.models.mixin import DataMixin

class User(db.Model, DataMixin, UserMixin):
    __tablename__ = 'usuarios'

    id:Mapped[Uuid] = mapped_column(Uuid(as_uuid=True),primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    email_normalizado: Mapped[str] = mapped_column(String(256), nullable=False, unique=True, index=True)
    hash_password:Mapped[str] = mapped_column(String(256), nullable=False)

    ativo: Mapped[Boolean] = mapped_column(Boolean, nullable= True, default=True)

    @property
    def is_active(self):
        return self.ativo
    @property
    def email(self):
        return self.email_normalizado
    @email.setter
    def email(self, value: str):
        self.email_normalizado = value.lower()

    def set_password(self, senha_aberta):
        self.hash_password = generate_password_hash(senha_aberta)

    def check_password(self,senha_aberta) -> bool:
        return check_password_hash(self.hash_password, senha_aberta)

    @classmethod
    def get_by_email(cls, email):
        sentenca = db.select(User).where(User.email_normalizado == email.lower())
        usuario = db.session.execute(sentenca).scalar_one_or_none()
        return usuario