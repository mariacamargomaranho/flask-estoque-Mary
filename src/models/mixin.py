from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime
from sqlalchemy import func
class DataMixin:
    dta_cadastro: Mapped[DateTime] = mapped_column(DateTime,
                                                  nullable=False,
                                                  server_default=func.now())
    dta_atualizado: Mapped[Optional[DateTime]] = mapped_column(DateTime,
                                                               nullable=True,
                                                               server_default=func.now(),
                                                               onupdate=func.now())