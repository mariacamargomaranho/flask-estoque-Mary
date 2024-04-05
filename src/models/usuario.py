import uuid

from sqlalchemy.orm  import mapped_column, Mapped
from sqlalchemy.types import Uuid, String
from werkzeug.security import generate_password_hash, check_password_hash

from src.modulos import db
from src.models.mixin import DataMixin

class User(db.Model, DataMixin):
    __tablename__ = 'usuarios'

    id:Mapped[Uuid] = mapped_column(Uuid(as_uuid=True),primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    email_normalizado: Mapped[str] = mapped_column(String(256), nullable=False, unique=True, index=True)
    hash_password:Mapped[str] = mapped_column(String(256), nullable=False)

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

