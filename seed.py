from peewee import *
from app import Stock
from app import db
import json

try:
    db.connect()

    db.drop_tables([Stock])
    db.create_tables([Stock])

    with open('stocks.json') as file:
        data = json.load(file)

    Stock.insert_many(data).execute()
    print("Data successfully inserted into the Stock table.")

except Exception as e:
    print("An error occurred:", e)

finally:
    db.close()
