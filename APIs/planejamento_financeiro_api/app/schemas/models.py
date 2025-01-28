from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Despesa(Base):
    __tablename__ = "despesas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    valor = Column(Float)
    categoria = Column(String)
