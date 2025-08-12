#!/usr/bin/env python3
"""Insert a document in a MongoDB collection based on kwargs.
"""

def insert_school(mongo_collection, **kwargs):
    """Insert a document in mongo_collection from kwargs and return its _id."""
    res = mongo_collection.insert_one(kwargs)

    return res.inserted_id
