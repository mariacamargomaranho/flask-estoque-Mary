import uuid
from sqlalchemy.types import Uuid, String
from sqlalchemy.orm import Mapped, mapped_column
from src.modulos import db
from src.models.mixin import DataMixin, BasicRepositoryMixin

class Categoria(db.Model, DataMixin, BasicRepositoryMixin):
    __tablename__ = 'categorias'

    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True),
                                     primary_key=True,
                                     default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(60),
                                      nullable=False)




