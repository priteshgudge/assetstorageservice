import pymongo


def read_document_from_db(collection_cursor,doc_id):
    '''
    Read Document From DB
    :param collection_cursor:
    :param doc_id:
    :return: Document Dict if Found else returns None
    '''
    try:
        document = collection_cursor.find_one({'_id':doc_id})
        return document
    except pymongo.errors.ConnectionFailure as ce:
        raise ce

    return None


def write_document_to_db(collection_cursor,doc_id,document):
    '''
    Write Document to DB
    :param collection_cursor:
    :param doc_id:
    :param document:
    :return:
    '''
    try:
        result = collection_cursor.find_one_and_replace({'_id':doc_id},document,upsert=True)
        return result
    except pymongo.errors.ConnectionFailure as ce:
        raise ce

    return None


class MongoReadWriteClient():
    def __init__(self,MONGO_URI):
        client = pymongo.MongoClient(MONGO_URI)
        self.cursor = client.assets.assetdocs

    def read_from_db(self,doc_id):
        return read_document_from_db(self.cursor,doc_id)

    def write_to_db(self,doc_id,document):
        return write_document_to_db(self.cursor,doc_id,document)