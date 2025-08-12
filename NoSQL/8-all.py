#!/usr/bin/env python3

def list_all(mongo_collection):
    result = []
    if mongo_collection is None:
        return result
    else:
        return list(mongo_collection.find())

