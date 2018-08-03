from functools import wraps

from flask import request, session, current_app as app
import flask_restful as restful

from assetstorageservice.constants.application_constants import API_KEY

def sanitize_response(response):
    data = None
    status = 200
    headers = {}

    if isinstance(response, tuple) and len(response) is 3:
        (data, status, headers) = response
    if isinstance(response, tuple) and len(response) is 5:
        (status, data, code, message, header) = response
        return status, data, code, message, headers.update(header)
    else:
        data = response
    return (data, status, headers)


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        if request.headers.get('X-API-KEY'):
            if request.headers.get('X-API-KEY') == API_KEY:
                return func(*args, **kwargs)

        app.logger.error("Unauthorized request from %s", request.remote_addr)
        return False, {}, 401, 'Unauthorized', {'Content-Type': 'application/json'}

    return wrapper


def patch_response_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = sanitize_response(func(*args, **kwargs))
        if isinstance(response, tuple) and len(response) is 5:
            status, data, code, message, headers = response
            data = {"responseData": data,
                    "status": status,
                    "message": message}

            return data, code, headers
        else:
            data, status, headers = response

        patched = isinstance(data, dict) and (
            "errorCode" in data or "responseData" in data
        )

        if not patched:
            data = {
                "responseData": data
            }

        if 'errorCode' in data.keys():
            status = data['errorCode']

        return (data, status, headers)

    return wrapper


def cors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data, status, headers = sanitize_response(func(*args, **kwargs))

        cors_allow_headers = ', '.join(app.config.get('CORS_ALLOW_HEADERS', []))
        cors_allow_origins = ', '.join(app.config.get('CORS_ALLOW_ORIGINS', []))
        cors_allow_methods = ', '.join(app.config.get('CORS_ALLOW_METHODS', []))

        headers.update({
            'Access-Control-Allow-Headers': cors_allow_headers,
            'Access-Control-Allow-Origin': cors_allow_origins,
            'Access-Control-Allow-Methods': cors_allow_methods
        })

        return (data, status, headers)

    return wrapper


class Resource(restful.Resource):
    def options(self, **kwargs):
        app.logger.info("Obtained options request from %s",
                        request.remote_addr)
        return "OK"

    options.authenticated = False

    method_decorators = [
        authenticate,
        patch_response_data
        # cors  # Keep it in the end
    ]
