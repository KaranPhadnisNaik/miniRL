from flask_restful import Resource,reqparse
#from flask_jwt import jwt_required
from models.link import LinksModel
from resources.hashing import ShortURL


class Links(Resource):
    """
    Links: Resource that adds a new link to links table
    UserRegister.post() - store url and return hash

    Required Arguments:
    + HEADER: none
    + url (str)
    """

    parser = reqparse.RequestParser()
    parser.add_argument('url',
        type=str,
        required=True,
        help="You need to enter a URL to shorten"
    )

    def post(self):
        data = Links.parser.parse_args()
        # if we are inserting first URL, set the starting key
        row = LinksModel.find_by_url(data['url'])
        if row:
            return {'message': 'An item with the URL {} already exists!'.format(data['url']), 'hash':row.hash},400
        link = LinksModel(data['url'],0,'')
        if not LinksModel.occupied():
            link.id = 423122
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
    """
    InterpretHash: Resource that returns the url corresponding to a hash
    InterpretHash.get() - get url corresponding to the hash and update clicks

    Required Arguments:
    + HEADER: <str:hash>
    """

    def get(self,hash):
        row = LinksModel.find_by_hash(hash)
        if row:
            return row.json(), 200

        return {'message': 'That hash was not found.'},404


class LinksList(Resource):
    """
    LinksList: Resource to return all fields of all urls (mostly for debugging)
    LinksList.get() - get all urls and attributes

    Required Arguments:
    + HEADER: None
    """

    def get(self):
        return {'links': list(map(lambda x: x.json(), LinksModel.query.all()))}
