#!/usr/bin/env python3
"""
Module 10-update_topics
Provides a function to update topics of a school document in a MongoDB collection.
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name (string): The school name to update.
        topics (list of strings): The list of topics approached in the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
