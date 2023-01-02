from sqlmodel import Field, SQLModel
from typing import Optional
from decouple import config
from uuid import UUID


class CriarDTO(SQLModel, table=True):
    __tablename__: str = config('TABELA_DB')

    id: Optional[UUID] = Field(
        default=None, 
        primary_key=True
    )
    nome: str
    modelo: str
    marca: str
    ano_modelo: int
    preco: int
