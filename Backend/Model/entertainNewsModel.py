import pymongo
import json
from mongoengine import connect
from mongoengine.fields import StringField
connect("mydatabase")


class news(DynamicDocument):
    title = StringField()
    content = StringField()
    meta = {
        "indexes": ["titles"],
        "ordering": ["date"]
    }
