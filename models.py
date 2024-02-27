from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, Date, TIMESTAMP

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('date_of_birth', Date, nullable=False),
    Column('registered_at', TIMESTAMP, nullable=False, default=datetime.utcnow())

)