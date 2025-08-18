import pymongo
import logging
import os 


logger = logging.getLogger(__name__)


class DataLoader:
    @staticmethod
    def connect_to_db():
        """
        Establish a connection to the mongo database.
        Return a mongodb connection object.
        """
        try:
            client = pymongo.MongoClient(
                host=os.getenv("MONGO_HOST", "mongodb-community-server"),
                port=int(os.getenv("MONGO_PORT", 27017)),
                username=os.getenv("MONGO_USER", "user"),
                password=os.getenv("MONGO_PASSWORD", "pwd"))
            db = client[os.getenv("MONGO_DATABASE", "mongodb")]
            logger.info("Successfully connected to MongoDB")
            return db
        except Exception as e:
            logger.error(f"Error connecting to MongoDB: {e}")
            return None
        
        

    @staticmethod
    def load_data():
        """
        Load data from the collection in the mongo database.
        Return all the collection.
        If an error occurs, return None.
        """
        db = DataLoader.connect_to_db()
        try:
            collection = db[os.getenv("MONGO_COLLECTION", "students")]
            data = list(collection.find({}, {"_id": 0}))  
            logger.info(f"Data loaded successfully from {collection.name} collection.")
            return data
        except Exception as e:
            logger.error(e)
            return None
        finally:
            db.client.close() if db else None
            logger.info("Database connection closed.")    