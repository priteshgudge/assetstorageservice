import os

MONGO_URI = os.getenv("MONGO_URI","mongodb://localhost:27017")

print ("*******MONGO URI: {}******".format(MONGO_URI))
