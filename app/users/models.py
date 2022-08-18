import uuid
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy_utils import UUIDType
from app.config.db import meta, engine


db_user = Table("users", meta,
                Column("id", Integer, primary_key=True),
                Column("user_id", UUIDType(binary=False), unique=True, default=uuid.uuid4),
                Column("username", String(255), nullable=True),
                Column("email", String(255), unique=True),
                Column("password", String(255)),
                Column("first_name", String(255), nullable=True),
                Column("last_name", String(255), nullable=True),
                Column("disabled", Boolean, default=False)
                )

meta.create_all(engine)
