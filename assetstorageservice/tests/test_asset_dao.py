import nose
import unittest
from unittest.mock import MagicMock
import uuid
from assetstorageservice.db.db_operations import mongo_read_write
from assetstorageservice.db.models.dao.asset_doc import AssetDocDao,AssetDoc
import datetime
import re
from assetstorageservice.constants import status_constants

uuid4regex = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')

def utc_to_dt(utc_timestamp):
    dt = datetime.datetime.fromtimestamp(utc_timestamp/1000.0)
    return dt

class TestAssetDao(unittest.TestCase):
    UUID = "test-uuid"
    CREATED_STATUS = status_constants.CREATED
    UPLOADED_STATUS = status_constants.UPLOADED
    URL = "http://s3-mock-url/test"
    CREATED_ON = 97738829919

    def __setup_read_asset_doc(self):
        mock_read_document = dict(
            _id=self.UUID,
            createdOn=self.CREATED_ON,
            updatedOn=self.CREATED_ON,
            uploadURL=self.URL,
            status=self.CREATED_STATUS
        )
        self.mock_read_doc = mock_read_document
        return mock_read_document
    def __setup_mongo_client(self,mock_read_doc):
        mock_mongo_client = MagicMock()
        mock_mongo_client.write_to_db = MagicMock(return_value=True)
        mock_mongo_client.read_from_db = MagicMock(return_value=mock_read_doc)
        self.mock_mongo_client = mock_mongo_client

    def setUp(self):
        self.__setup_read_asset_doc()
        self.__setup_mongo_client(self.mock_read_doc)

    def test_create_asset_doc(self):
        mock_mongo_client = self.mock_mongo_client
        test_asset_dao = AssetDocDao(mongo_client=mock_mongo_client,asset_doc_id=None)
        test_asset_dao.create_or_update_asset_doc()
        test_asset_dao.update_upload_url(self.URL)

        asset_doc = test_asset_dao.asset_doc
        current_time = datetime.datetime.now()
        asset_doc_created_on = utc_to_dt(asset_doc.created_on)
        assert asset_doc.get_status() == self.CREATED_STATUS
        assert asset_doc.get_upload_url() == self.URL
        assert asset_doc_created_on.date() == current_time.date()
        assert uuid4regex.match(asset_doc.get_id())
        assert type(asset_doc.get_db_dict()) == dict
        assert type(asset_doc.get_api_dict()) == dict

    def test_read_asset_doc(self):
        mock_mongo_client = self.mock_mongo_client
        test_asset_dao = AssetDocDao(mongo_client=mock_mongo_client,asset_doc_id=self.UUID)
        asset_doc = test_asset_dao.get_asset_doc()

        assert asset_doc.get_status() == self.CREATED_STATUS
        assert asset_doc.get_id() == self.UUID
        assert asset_doc.get_upload_url() == self.URL
        assert type(asset_doc.get_db_dict()) == dict
        assert type(asset_doc.get_api_dict()) == dict

    def test_update_url(self):
        mock_mongo_client = self.mock_mongo_client
        test_asset_dao = AssetDocDao(mongo_client=mock_mongo_client, asset_doc_id=self.UUID)
        UPDATE_URL = "URL_UPDATE"
        test_asset_dao.update_upload_url(UPDATE_URL)


        asset_doc = test_asset_dao.get_asset_doc()
        assert asset_doc.get_status() == self.CREATED_STATUS
        assert asset_doc.get_id() == self.UUID
        assert asset_doc.get_upload_url() == UPDATE_URL
        assert type(asset_doc.get_db_dict()) == dict
        assert type(asset_doc.get_api_dict()) == dict

    def test_update_status(self):
        mock_mongo_client = self.mock_mongo_client
        test_asset_dao = AssetDocDao(mongo_client=mock_mongo_client, asset_doc_id=self.UUID)
        test_asset_dao.update_status_uploaded()

        asset_doc = test_asset_dao.get_asset_doc()
        assert asset_doc.get_status() == self.UPLOADED_STATUS
        assert asset_doc.get_id() == self.UUID
        assert asset_doc.get_upload_url() == self.URL
        assert type(asset_doc.get_db_dict()) == dict
        assert type(asset_doc.get_api_dict()) == dict