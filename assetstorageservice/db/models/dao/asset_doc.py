import json
import uuid
import pymongo
from assetstorageservice.db.models.asset_model import AssetDoc
from assetstorageservice.db.config.db_configs import MONGO_URI
from assetstorageservice.db.db_operations.mongo_read_write import MongoReadWriteClient
from assetstorageservice.utils.utility_functions import default_date_now
from assetstorageservice.utils.utility_functions import get_utc_ms_time
from assetstorageservice.constants import status_constants

class AssetDocDao():

    def __init__(self,mongo_client=MongoReadWriteClient(MONGO_URI),asset_doc_id=None):
        self.mongo_client = mongo_client
        self.db_read_func = mongo_client.read_from_db
        self.db_write_func = mongo_client.write_to_db
        self.asset_doc = None
        if asset_doc_id:
            self.asset_doc = self.__get_doc_by_id(asset_doc_id)
        else:
            self.asset_doc = AssetDoc()

    def get_asset_doc(self):
        return self.asset_doc

    def __get_doc_by_id(self,asset_doc_id):
        '''
        Public Method
        :return: AssetDoc
        '''
        document = self.db_read_func(asset_doc_id)
        asset_doc = AssetDoc()
        asset_doc.initialize_from_db_dict(document)
        return asset_doc

    def create_or_update_asset_doc(self):
        '''
        Generic Interface to Update in DB to set updated/created dates correctly
        :return: AssetDoc Object
        '''
        current_date = get_utc_ms_time(default_date_now())

        if not self.asset_doc.get_id():
            self.asset_doc.set_id(str(uuid.uuid4()))
            self.asset_doc.set_created_on(current_date)

        self.asset_doc.set_updated_on(current_date)

        self.db_write_func(self.asset_doc.get_id(),self.asset_doc.get_db_dict())

        return self.asset_doc

    def update_upload_url(self,upload_url):
        self.asset_doc.set_upload_url(upload_url)
        self.asset_doc.set_status(status_constants.CREATED)
        self.create_or_update_asset_doc()

    def update_status_uploaded(self):
        self.asset_doc.set_status(status_constants.UPLOADED)
        self.create_or_update_asset_doc()


if __name__ == '__main__':
    asset_doc_dao = AssetDocDao()
    asset_doc_dao.update_upload_url("URL")
    print (asset_doc_dao.asset_doc)
    asset_doc_dao.update_status_uploaded()
    print (asset_doc_dao.asset_doc)

    id = asset_doc_dao.asset_doc.get_id()

    asset_doc_dao = AssetDocDao(asset_doc_id=id)
    print (asset_doc_dao.asset_doc)

