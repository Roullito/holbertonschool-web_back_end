#!/usr/bin/env python3
"""
Module to update the topics of a school document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list): list of topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
