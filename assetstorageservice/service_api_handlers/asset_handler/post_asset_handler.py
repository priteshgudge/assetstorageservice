from assetstorageservice.db.models.dao.asset_doc import AssetDocDao
from assetstorageservice.constants import status
from assetstorageservice.utils.s3_connection import S3Client

def handle_post_request(remote_addr):
    asset_doc_dao = AssetDocDao()
    asset_doc = asset_doc_dao.get_asset_doc()

    # Initial Update to Asset Doc to keep track of request
    asset_doc.set_status(status.CREATED)
    asset_doc.set_request_ip(remote_addr)
    asset_doc_dao.create_or_update_asset_doc()

    # Generate Upload URL
    url = S3Client().generate_presigned_put_url(asset_doc.get_id())

    # Set Upload URL and update to DB
    asset_doc.set_upload_url(url)
    asset_doc_dao.create_or_update_asset_doc()

    return asset_doc.get_api_dict()
