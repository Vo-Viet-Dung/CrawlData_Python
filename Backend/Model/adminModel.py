from mongoengine import
from mongoengine import mongodb_support
import pymongo
from pymongo import MongoClient
from mongoengine.fields import BinaryField, StringField
from mongoengine import connect
import json
import os
from mongoengine.base import document

connect("mydatabase")


class admin(Document):
    name = StringField(unique=True, required=True)
    username = StringField(unique=True, required=True)
    password = BinaryField(unique=True, required=True)

    def json(self):
        userdict = {
            "name": self.name,
            "username": self.username,
            "password": self.password
        }
        return json.dumps(userdict)

    meta = {
        "indexes": ["name", "username"]

    }


user = admin(
    name="Vo Viet Dung",
    username="dungvv117",
    password=os.urandom(16)
).save()
