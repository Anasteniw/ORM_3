import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

SQLsystem = 'postgresql'
login = 'postgres'
password = '02091990'
host = 'localhost'
port = 5432
db_name = "bookshop_db_2"
DSN = f'{SQLsystem}://{login}:{password}@{host}:{port}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

with open('tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }
    session.add(model)
session.commit()

def publisher_name_search():
    join_column = session.query(Publisher).join(Book).join(Stock).join(Shop).join(Sale)
    publisher_name = input('Введите имя издателя: ')
    result = join_column.filter(Publisher.name == publisher_name)
    for res in result.all():
        print(res.Book.title, res.Shop.name, res.Sale.price, res.Sale.date_sale, sep='|')

if __name__ == '__main__':
    publisher_name_search()

session.close()
