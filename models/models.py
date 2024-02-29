from datetime import datetime


from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Date,
    Time,
    ForeignKey,
    JSON,
    TIMESTAMP
)
from sqlalchemy.orm import DeclarativeBase

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

class Base(DeclarativeBase):
    pass




role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permission', JSON)
)



user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('date_of_birth', Date, nullable=False),
    Column('registered_at', TIMESTAMP, nullable=False, default=datetime.utcnow())
)


day = Table(
    'day',
    metadata,
    Column('id'),
    Column('date', Date, nullable=False),
)



note = Table(
    'note',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String, nullable=True),
    Column('time', Time, nullable=False, default=datetime.utcnow()),
    Column('user_id', Integer, ForeignKey(user.c.id)),
)


