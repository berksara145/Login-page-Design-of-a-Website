from Flaskr import create_app
from flask_restful import Api, Resource, reqparse
from flask import request

app = create_app()
api = Api(app)


if __name__ == "__main__":
    app.run(debug=True)
