import nose
import unittest
import uuid
from assetstorageservice.db.models.asset_model import AssetDoc


class TestAssetDoc(unittest.TestCase):
    def test_read_write_basic_details(self):
        basic_url = "url://test-url"
        basic_timestamp = 3883882882
        basic_status = "status"
        uid = str(uuid.uuid4())
        asset_doc = AssetDoc()
        asset_doc.set_upload_url(basic_url)
        asset_doc.set_updated_on(basic_timestamp)
        asset_doc.set_created_on(basic_timestamp)
        asset_doc.set_status(basic_status)
        asset_doc.set_id(uid)

        db_dict = asset_doc.get_db_dict()

        assert basic_url == db_dict['uploadURL']
        assert uid == db_dict['_id']
        assert basic_status == db_dict['status']
        assert basic_timestamp == db_dict['createdOn']
        assert basic_timestamp == db_dict['updatedOn']

