import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ =  'publishers'
    id_publisher= sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True)
    def __repr__(self):
        return f"Publisher(id={self.id_publisher}, name={self.name})"


class Book(Base):
    __tablename__ =  'books'
    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publishers.id_publisher"), nullable=False)
    publisher = relationship(Publisher, backref="books")
    

class Shop(Base):
    __tablename__ =  'shops'
    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True)
    def __repr__(self):
        return f"Shop(id={self.id_shop}, name={self.name})"


class Stock(Base):
    __tablename__ = 'stocks'
    id_stock = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("books.id_book"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shops.id_shop"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref="stocks")
  

class Sale(Base):
    __tablename__ = 'sales'
    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stocks.id_stock"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship(Stock, backref="sales")
  


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)