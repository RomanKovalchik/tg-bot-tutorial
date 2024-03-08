from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)

# Здесь необходимо указать ваше соединение с базой данных MySQL
# Пример: mysql://username:password@hostname:port/database_name
# Замените username, password, hostname, port и database_name на ваши реальные данные

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/bot')
Base.metadata.create_all(engine)
