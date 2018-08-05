from assetstorageservice.db.models.dao.asset_doc import AssetDocDao
from assetstorageservice.utils.s3_connection import S3Client
from assetstorageservice.constants.application_constants import DEFAULT_GET_TIMEOUT
from assetstorageservice.constants import status_constants
from assetstorageservice.utils.exceptions.custom_error import CustomError

def handle_get_request(asset_id,request_data):

    timeout = request_data.get('timeout')
    if timeout:
        timeout_int = int(timeout)
    else:
        timeout_int = DEFAULT_GET_TIMEOUT

    asset_doc_dao = AssetDocDao(asset_doc_id=asset_id)
    asset_doc = asset_doc_dao.get_asset_doc()

    if asset_doc.get_status() != status_constants.UPLOADED:
        raise CustomError(422, "Asset is not marked as uploaed")

    url = S3Client().generate_presigned_get_url(asset_doc.get_id(),timeout=timeout_int)

    response_dict = {
        'downloadURL': url
    }
    return response_dict
