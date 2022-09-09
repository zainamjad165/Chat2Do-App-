from unittest import defaultTestLoader
import databases
import sqlalchemy
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

#MODELS 
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("username", sqlalchemy.String)
)

reciver = sqlalchemy.Table(
    "reciver",
    metadata,
    sqlalchemy.Column("reciver", sqlalchemy.String)
)

todos = sqlalchemy.Table(
    "todos",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("tittle", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("username",sqlalchemy.String),
)

texts = sqlalchemy.Table(
    "texts",
    metadata,
    sqlalchemy.Column("message", sqlalchemy.String),
    sqlalchemy.Column("to",sqlalchemy.String),
    sqlalchemy.Column("by",sqlalchemy.String),
    sqlalchemy.Column("created_at",sqlalchemy.String),
)

messages = sqlalchemy.Table(
    "messages",
    metadata,
    sqlalchemy.Column("message", sqlalchemy.String),
    sqlalchemy.Column("by",sqlalchemy.String),
    sqlalchemy.Column("created_at",sqlalchemy.String),
)

#BINDING DATABASE
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

#SCHEMAS
class AddTodo(BaseModel):
    tittle: str
    description : str

class SeeTodo(BaseModel):
    tittle: str
    description : str

class SeeUser(BaseModel):
    username: str

class AddMessage(BaseModel):
    message: str
    created_at: str
    
class SeeMessage(BaseModel):
    by: str
    message: str
    created_at: str

class AddText(BaseModel):
    message: str
    to: str
    created_at: str

class SeeText(BaseModel):
    by: str
    message: str
    created_at: str
