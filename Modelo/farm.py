from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table,DateTime, Date , ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists, select
import datetime
import pandas as pd
from sqlalchemy.sql import func


user = 'root'
passw = ''
host = 'localhost'
port = '3306'

database = 'farmaciaDB'

mysql_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}'.format(user, passw, host, port))

mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {0}".format(database))

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(user, passw, host, port, database))
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
    caducidad = Column(Date)
    area = Column(String(50))
    origen = Column(String(50))
    fechaIngreso = Column(Date, server_default=func.now())
    clave_corta = Column(String(30), ForeignKey('clave.corta'))

class Salida(Base):
    __tablename__ = 'salida'
    
    idSalida = Column(Integer, primary_key=True, autoincrement = True)
    clave_corta = Column(String(30), ForeignKey('clave.corta'))
    cantidadSal = Column(Integer)
    Caducidad = Column(Date)
    FechaPedido = Column(Date)
    fechaEntrega = Column(Date)
    area = Column(String(50))
    lote = Column(String(30))
    numero_pedido = Column(Integer)

class Historial(Base):
    __tablename__ = 'historial'

    idFarmaco = Column(Integer, primary_key=True, autoincrement = True)
    lote = Column(String(30))
    cantidad = Column(Integer)
    caducidad = Column(Date)
    area = Column(String(50))
    origen = Column(String(50))
    fechaIngreso = Column(Date, server_default=func.now())
    clave_corta = Column(String(30), ForeignKey('clave.corta'))
    
    
    
Base.metadata.create_all(engine)

# # Pandas
q = session.query(Clave).count()
if q  <= 0:
    medicamentos_df = pd.read_csv('medicamentos.csv', encoding = 'utf-8')
    frame_Medi = pd.DataFrame(medicamentos_df)
    frame_Medi.to_sql(con=engine, name='clave', if_exists='append', index=False)

    farmacos_df = pd.read_csv('farmacos.csv', encoding = 'utf-8')
    frame_Farma = pd.DataFrame(farmacos_df)
    frame_Farma.to_sql(con=engine, name='farmaco', if_exists='append', index=False)
else:
    print('ya hay datos')

#query = session.query(Usuario).filter(Usuario.nombre == '11').first()

# q = select([Usuario])

# df_dara = pd.read_sql(q, con=engine)

# password = b"hola"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# print(hashed)

#print(df_dara)