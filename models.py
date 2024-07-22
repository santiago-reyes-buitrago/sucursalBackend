from sqlalchemy import String,BIGINT,Column
from database import Bd

class PrestamosCarros(Bd):
    __tablename__ = "PRESTAMOS_CARROS"
    id = Column(BIGINT, primary_key=True,autoincrement=True)
    marca_carro = Column(String(50))
    sucursal = Column(String(100))
    aspirante = Column(String(50))
