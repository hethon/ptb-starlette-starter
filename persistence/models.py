from sqlalchemy.orm import Mapped, mapped_column

from .db import Model


class User(Model):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(primary_key=True)
    tg_name: Mapped[str]
    tg_username: Mapped[str | None]

    def __repr__(self) -> str:
        return f"<User('{self.tg_id}', '{self.tg_name}')>"
