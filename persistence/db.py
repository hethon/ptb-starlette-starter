from dotenv import load_dotenv
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

import config.config as config


load_dotenv()


class Model(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })


engine = create_async_engine(config.DATABASE_URL, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)
