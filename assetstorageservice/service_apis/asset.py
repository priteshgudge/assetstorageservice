from flask import session, request
from flask import current_app as app
from assetstorageservice.utils.resource import Resource
from assetstorageservice.utils.logger_utils import get_logger
from assetstorageservice.utils.response_utils import ok_response, error_response
from assetstorageservice.utils.exceptions.error_handler import ErrorHandler

logger = get_logger()

class Asset(Resource):
    @ErrorHandler("Asset GET", app)
    def get(self, asset_id=None):
        logger.info("Received Asset Get request from {}".format(request.remote_addr))

        if asset_id:
            response = None
            #response = get_crop_handler.handle_request(request_data)
        else:
            return error_response(400,"Bad Request")

        return ok_response(response, status_code=201)  # 201 HTTP Created

    get.authenticated = False

    @ErrorHandler("Asset POST", app)
    def post(self):
        logger.info("Received Asset Creation request from {}".format(request.remote_addr))

        response = None
        return ok_response(response)

    post.authenticate = False

    @ErrorHandler("Asset PUT", app)
    def put(self, crop_id):
        logger.info("Received Asset update request from {}".format(request.remote_addr))

        request_data = request.get_json(force=True)
        response = None
        return ok_response(response)

    put.authenticated = False

    @ErrorHandler("Asset PATCH", app)
    def patch(self, crop_id):
        logger.info("Received Asset update request from {}".format(request.remote_addr))

        request_data = request.get_json(force=True)
        response = None
        return ok_response(response)

    patch.authenticated = False
