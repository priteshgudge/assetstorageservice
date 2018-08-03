headers_mapping = {'csv': {'content-type':'application/csv'},
                           'json': {'content-type':'application/json'}}


def ok_response(response, status=True, message="OK", headers='json',status_code=200):
    return status, response, status_code, message, headers_mapping[headers]


def error_response(code, message, headers='json', response={}):
    return False, response, code, message, headers_mapping[headers]
