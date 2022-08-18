from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from app.db.session import metadata

Base: Any = declarative_base(metadata=metadata)
