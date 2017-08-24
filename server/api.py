from flask import Flask, request
from flask_restful import Resource, Api, reqparse
#from flask_jwt import JWT, jwt_required
import sqlite3

#from security import authenticate,identity
#from user import UserRegister

app = Flask(__name__)
api = Api(app)
app.secret_key = 'karan'

items = []

#jwt = JWT(app, authenticate,identity) # creates a new endpoint /auth,
                                      # sends username and password to authnetiate function


class CreateLinks(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('full_url',
        type=str,
        required=True,
        help="This Field can not be left blank"
    )

    # post
    def post(self):
        data = CreateLinks.parser.parse_args()
        # generate hashed value
        hashedValue = "ljweqwe"
        item = {'hash': hashedValue , 'full_url': data['full_url']}
        return item, 201

    def delete(self, name):
       global items
       items = list(filter(lambda x: x['name'] != name, items))
       return {'message': 'Item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(CreateLinks, '/create') # localhost:9000/create
#api.add_resource(ItemList, '/') # localhost:9000/Item/Rolf
#api.add_resource(UserRegister, '/register') # localhost:9000/register

app.run(port=9000, debug=True)
