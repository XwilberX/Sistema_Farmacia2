from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table,DateTime, Date , ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists, select
import datetime
import pandas as pd
from sqlalchemy.sql import func


engine = create_engine('mysql+pymysql://root:wil99@localhost/prueba')
#engine = create_engine('postgresql+psycopg2://postgres:wil99@localhost/farm')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120))
    contrasena = Column(String(30))

class Clave(Base):
    __tablename__ = 'clave'
    
    #idClave = Column(Integer, primary_key=True, autoincrement = True)
    corta = Column(String(30), primary_key=True, autoincrement=False)
    clave = Column(Text())
    descripcion = Column(Text())
    presentacion = Column(Text())
    tipo = Column(Boolean)
    
    farmacos = relationship("Farmaco")
    salidas = relationship("Salida")
    
    
class Farmaco(Base):
    __tablename__ = 'farmaco'
    
    idFarmaco = Column(Integer, primary_key=True, autoincrement = True)
    lote = Column(String(30))
    cantidad = Column(Integer)
    caducidad = Column(String(30))
    area = Column(String(50))
    origen = Column(String(50))
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    clave_corta = Column(String(30), ForeignKey('clave.corta'))
    #clave_corta = Column(String(50), ForeignKey('clave.corta'))
    
    Salidas = relationship("Salida")

class Salida(Base):
    __tablename__ = 'salida'
    
    idSalida = Column(Integer, primary_key=True, autoincrement = True)
    cantidadSal = Column(Integer)
    fechaEntrega = Column(Date)
    FechaPedido = Column(Date)
    
    clave_corta = Column(String(30), ForeignKey('clave.corta'))
    farmaco_idFarmaco = Column(Integer, ForeignKey('farmaco.idFarmaco'))
    

Base.metadata.create_all(engine)

# # Pandas
# medicamentos_df = pd.read_csv('medicamentos.csv', encoding = 'utf-8')
# frame_Medi = pd.DataFrame(medicamentos_df)
# frame_Medi.to_sql(con=engine, name='clave', if_exists='append', index=False)
#
# farmacos_df = pd.read_csv('farmacos.csv', encoding = 'utf-8')
# frame_Farma = pd.DataFrame(farmacos_df)
# frame_Farma.to_sql(con=engine, name='farmaco', if_exists='append', index=False)

#query = session.query(Usuario).filter(Usuario.nombre == '11').first()

# q = select([Usuario])

# df_dara = pd.read_sql(q, con=engine)

# password = b"hola"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# print(hashed)

#print(df_dara)