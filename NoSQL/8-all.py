#!/usr/bin/env python3

def list_all(mongo_collection):
        """
        Lists all documents in a MongoDB collection.

        Args:
                mongo_collection: pymongo collection object

        Returns:
                List of documents in the collection
        """
        return list(mongo_collection.find())

