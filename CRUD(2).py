from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Read method to implement the R in CRUD.
    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            #for document in data:
                #print(document)
            
        else:
            data = self.database.animals.find({},{"_id": False})
        
        return data
    
#Update method to implement the U in CRUD
    def update(self, inputData, newData):
        if inputData is not None:
            count = 0
            for instance in inputData:
                count += 1
                result = self.database.animals.update_many(inputData, {"$set": newData})
            return count
        else:
            raise Exception("Check data input and try again")
        return result
    
#Delete method to implement D in CRUD
    def delete(self, removeData):
        if removeData is not None:
            count = 0
            for instance in removeData:
                count += 1
                data = self.database.animals.delete_many(removeData)
            return count
        else:
            raise Exception("Check data input and try again")
            