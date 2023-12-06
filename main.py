from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from datetime import date
from config import DATABASE_CONNECTION

DATABASE_URL = DATABASE_CONNECTION
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Item(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    created_at = Column(Date)

Base.metadata.create_all(bind=engine)
ItemPydentic = sqlalchemy_to_pydantic(Item, exclude=['id'])
db_item = ItemPydentic(title = 'Dead Souls', author = 'Gogol', genre = 'poem', created_at = date(1835,1,1))

def create_item(db_item: ItemPydentic):
    """
    добавляет новый элемент в таблицу
    """    
    with SessionLocal() as db:
        db_item = Item(**db_item.dict())
        db.add(db_item)
        db.commit() 
        db.refresh(db_item) 
    return db_item

def get_item():
    """
    получение всех элементов из таблицы
    """
    result = []
    with SessionLocal() as db:
        items = db.query(Item).all()
        for item in items:
            result.append({
            'id':item.id,
            'title':item.title,
            'author':item.author,
            'genre': item.genre,
            'created_at': item.created_at})
    return result

def retrieve_item(item_id:int):
    """
    получение информации по ID
    """
    with SessionLocal() as db:
        retrieved_item = db.query(Item).get(item_id) # filter_by(id=item_id).first()

        if retrieved_item:
            data = {
                'title':retrieved_item.title,
                'author':retrieved_item.author,
                'genre': retrieved_item.genre,
                'created_at': retrieved_item.created_at
                }
            return data
        else:
            return None

def update_item(item_id: int, item:ItemPydentic):
    with SessionLocal() as db:
        db_item = db.query(Item).get(item_id)
        if db_item is None:
            return None
        for field, value in item.dict().items():
            setattr(db_item, field, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    
def delete_item(item_id: int):
    """
    Удаление по ID.
    """
    with SessionLocal() as db:
        item_to_delete = db.query(Item).get(item_id)
        if item_to_delete:
            db.delete(item_to_delete)
            db.commit()
            return f"Продукт с ID {item_id} успешно удален"
        else:
            return None



