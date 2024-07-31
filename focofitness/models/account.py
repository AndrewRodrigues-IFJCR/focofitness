from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Account(Base):
    __tablename__ = 'accounts'

    email: Mapped[str] = mapped_column(
        String(256), unique=True, index=True, nullable=False
    )

    password_hash: Mapped[str] = mapped_column(String(256))
