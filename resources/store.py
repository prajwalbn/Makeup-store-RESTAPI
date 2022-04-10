from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Brand not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A Brand with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the brand."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Brand deleted'}


class StoreList(Resource):
    def get(self):
        return {'Brands': list(map(lambda x: x.json(), StoreModel.query.all()))}
