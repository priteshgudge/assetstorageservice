import unittest
import datetime
import boto3
import botocore
from unittest.mock import MagicMock
from assetstorageservice.service_api_handlers.asset_handler.get_asset_handler import handle_get_request
from assetstorageservice.constants import status_constants
from assetstorageservice.utils.s3_connection import S3Client
from unittest.mock import patch
import requests
import sys




class TestGetRequest(unittest.TestCase):
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

    def test_get_asset_doc_not_found_error(self):
        s3_client = S3Client()
        url = s3_client.generate_presigned_get_url(self.UUID + str(datetime.datetime.now()),timeout=100)
        #self.assertRaises(botocore.exceptions.ClientError)
