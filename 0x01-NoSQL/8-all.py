#!/usr/bin/env python3
"""
Module 8-all
Provides a function to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection, or an empty list if no documents are found.
    """
    return list(mongo_collection.find())
