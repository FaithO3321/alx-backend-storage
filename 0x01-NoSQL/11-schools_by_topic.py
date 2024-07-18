#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Provides a function to find schools by topic in a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (string): The topic to search for.

    Returns:
        A list of schools having the specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
