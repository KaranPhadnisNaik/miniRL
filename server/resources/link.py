from flask_restful import Resource,reqparse
#from flask_jwt import jwt_required
from models.link import LinksModel
from resources.hashing import ShortURL


class Links(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
        type=str,
        required=True,
        help="You need to enter a URL to shorten"
    )

    def post(self):
        # if the url that is sent via POST EXISTS
        #    get the hash and return it
        # else
        #    add add a new hash and store it
        data = Links.parser.parse_args()
        row = LinksModel.find_by_url(data['url'])
        if row:
            return {'message': 'An item with the URL {} already exists!'.format(data['url']), 'hash':row.hash},400
        link = LinksModel(data['url'],0,'')
        try:
            link.save_to_db()
        except:
            return {'message': 'An error occured inserting the URL.'}, 500
        # get the row of the same URL that you entered
        row = LinksModel.find_by_url(data['url'])
        if not row:
            return {'message': 'There was an error retrieving the URL {} !'.format(data['url'])}, 400
        row.hash = ShortURL().encode(row.id)
        try:
            row.save_to_db()
        except:
            return {'message': 'An error occured inserting the hash.'}, 500
        return row.json(), 201

class InterpretHash(Resource):
    def get(self,hash):
        row = LinksModel.find_by_hash(hash)
        if row:
            return row.json(), 200
        return {'message': 'That hash was not found.'},404


class LinksList(Resource):
    def get(self):
        return {'links': list(map(lambda x: x.json(), LinksModel.query.all()))}
