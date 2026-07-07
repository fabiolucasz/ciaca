from sqlalchemy import create_engine, Column, Integer, String, Boolean
#from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base



# Configurações do banco de dados
DATABASE_URL = "sqlite:///./database.db"

# Configurar engine com pool de conexões
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    name = Column(String, nullable=True)
    title = Column(String, nullable=True)
    



# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)