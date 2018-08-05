from os.path import dirname, abspath
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from assetstorageservice.service_apis.ping import Ping
from assetstorageservice.service_apis.asset import Asset

# Setting Up App
app = Flask("AssetStorage")
CORS(app)
# Session

app.root_dir = dirname(dirname(abspath(__file__)))
api = Api(app, prefix='/assetstorage/')

app.logger.info("Setting up Resources")

# Setting Up API Resources
api.add_resource(Ping, 'ping/')
api.add_resource(Asset, 'asset/<string:asset_id>/', 'asset/')


if __name__ == '__main__':
    app.logger.info("app {} started..".format(app))
    app.run(host="0.0.0.0", debug=True, port=7500)
