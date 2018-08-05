from assetstorageservice.db.models.dao.asset_doc import AssetDocDao
from assetstorageservice.constants import status_constants
from assetstorageservice.utils.exceptions import custom_error


def handle_patch_request(asset_id, request_data,remote_addr):
    if not request_data.get('status') or request_data['status'] != "uploaded":
        raise custom_error.CustomError(400, "Bad Request")

    asset_doc_dao = AssetDocDao(asset_doc_id=asset_id)
    asset_doc = asset_doc_dao.get_asset_doc()

    asset_doc.set_status(status_constants.UPLOADED)
    asset_doc.set_request_ip(remote_addr)

    asset_doc_dao.create_or_update_asset_doc()

    return asset_doc.get_api_dict()