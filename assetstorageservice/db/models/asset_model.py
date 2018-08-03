import pytz
from datetime import datetime
from assetstorageservice.utils.utility_functions import get_utc_ms_time


class AssetDoc():
    """
    Basic Asset Structure to store in Persistent DataStore
    """
    def __init__(self):
        self.uuid = None        # Asset IdentificationID
        self.created_on = None  # UTC MS(UTC Millisecond timestamp as
                                # standard as it allows timezone independent storage)
        self.updated_on = None  # UTC MS
        self.upload_url = None  # Upload Link
        self.status = None      # Status of AssetDocument
        self.request_ip = None  # IP Address of Upload Request for basic tracking

    def set_upload_url(self,upload_url):
        self.upload_url = upload_url

    def set_updated_on(self,updated_on):
        self.updated_on = updated_on

    def set_created_on(self,created_on):
        self.created_on = created_on

    def set_id(self,uuid):
        self.uuid = uuid

    def set_request_ip(self,request_ip):
        self.request_ip = request_ip

    def set_status(self,status):
        self.status = status

    def get_id(self):
        return self.uuid
    def get_db_dict(self):
        '''
        Returns Structure to store in DB
        :return:
        '''
        db_dict = dict(_id=self.uuid,
                       createdOn=self.created_on,
                       updatedOn=self.updated_on,
                       uploadURL=self.upload_url,
                       status=self.status,
                       requestIP=self.request_ip)
        return db_dict

    def initialize_from_db_dict(self,bson_dict):
        '''
        Sets the object with appropriate values
        :param bson_dict:
        :return:
        '''
        self.uuid = bson_dict.get('_id')
        self.created_on = bson_dict.get('createdOn')
        self.updated_on = bson_dict.get('updatedOn')
        self.upload_url = bson_dict.get('uploadURL')
        self.status = bson_dict.get('status')
        self.request_ip = bson_dict.get('requestIP')

    def get_api_dict(self):
        '''
        Returns structure for API response
        :return:
        '''
        api_dict = dict(id=self.uuid,
                        uploadURL=self.upload_url
                        )
        return api_dict

    def __repr__(self):
        repr_string = "<AssetDoc: {} {} {} {} {} {}>".format(
            self.uuid,
            self.created_on,
            self.updated_on,
            self.upload_url,
            self.status,
            self.request_ip
        )
        return repr_string

    def __str__(self):
        return self.__repr__()

class DownloadAssetDoc():
    def __init__(self):
        pass