from assetstorageservice.utils.resource import Resource
from assetstorageservice.utils.logger_utils import get_logger
from flask import request

logger = get_logger()


class Ping(Resource):
    def get(self):
        logger.info("Received Ping request from {}".format(request.remote_addr))
        return {"success": True}

    get.authenticated = False
