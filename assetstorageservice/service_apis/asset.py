from flask import session, request
from flask import current_app as app
from assetstorageservice.utils.resource import Resource
from assetstorageservice.utils.logger_utils import get_logger
from assetstorageservice.utils.response_utils import ok_response, error_response
from assetstorageservice.utils.exceptions.error_handler import ErrorHandler
from assetstorageservice.service_api_handlers.asset_handler import (patch_asset_handler,post_asset_handler,
                                                                    get_asset_handler)

logger = get_logger()

class Asset(Resource):
    '''
    Interface for Asset Entry Creation, Updation and Download Link Generation
    '''
    @ErrorHandler("Asset GET", app)
    def get(self, asset_id=None):
        '''
        Generates the Presigned URL for File Download from S3
        :param asset_id:
        :return:
        '''
        logger.info("Received Asset Get request from {}".format(request.remote_addr))

        request_data = request.args.to_dict()
        if asset_id:
            response = get_asset_handler.handle_get_request(asset_id,request_data)
        else:
            return error_response(400,"Bad Request")

        return ok_response(response)  # 200 HTTP OK

    get.authenticated = False

    @ErrorHandler("Asset POST", app)
    def post(self):
        '''
        Generates Presigned URL for file upload
        :return:
        '''
        logger.info("Received Asset Creation request from {}".format(request.remote_addr))

        response = post_asset_handler.handle_post_request(request.remote_addr)

        return ok_response(response, status_code=201)

    post.authenticate = False

    @ErrorHandler("Asset PUT", app)
    def put(self, asset_id):
        logger.info("Received Asset update request from {}".format(request.remote_addr))

        request_data = request.get_json(force=True)
        response = patch_asset_handler.handle_patch_request(asset_id,request_data,request.remote_addr)

        return ok_response(response)

    put.authenticated = False

    @ErrorHandler("Asset PATCH", app)
    def patch(self, asset_id):
        '''
        API to mark asset as Uploaded
        :param asset_id:
        :return:
        '''
        logger.info("Received Asset update request from {}".format(request.remote_addr))

        request_data = request.get_json(force=True)
        response = patch_asset_handler.handle_patch_request(asset_id, request_data, request.remote_addr)

        return ok_response(response)

    patch.authenticated = False
