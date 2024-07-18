#!/usr/bin/env python3
"""
Module 9-insert_schoolg
Provides a function to insert a new document in a MongoDB collection.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs to be inserted as a new document.

    Returns:
        The _id of the new document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
