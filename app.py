from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('stocks', user='stocktrader', password='abc123', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Stock(BaseModel):
  symbol = CharField()
  name = CharField()
  shares = IntegerField()
  date_acquired = DateField()
  purchase_price_per_share = FloatField()
  current_price = FloatField()

app = Flask(__name__)

@app.route('/stocks/', methods=['GET', 'POST'])
@app.route('/stocks/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Stock.get(Stock.id == id)))
    else:
        stocks_list = []
        for stock in Stock.select():
            stocks_list.append(model_to_dict(stock))
        return jsonify(stocks_list)

  if request.method =='PUT':
    body = request.get_json()
    Stock.update(body).where(Stock.id == id).execute()
    return "Stock " + str(id) + " has been updated."

  if request.method == 'POST':
    new_Stock = dict_to_model(Stock, request.get_json())
    new_Stock.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Stock.delete().where(Stock.id == id).execute()
    return "Stock " + str(id) + " deleted."

app.run()