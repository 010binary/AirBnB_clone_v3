#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    func for status route that returns the status
    """
    if request.method == 'GET':
        res = {"status": "OK"}
        return jsonify(res)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    func to return the count of all class objects
    """
    if request.method == 'GET':
        res = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            res[value] = storage.count(key)
        return jsonify(res)
