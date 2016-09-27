from mongoengine import *
import os

connect('simple_tasklist', host=os.environ['DB_PORT_27017_TCP_ADDR'])


class Task(Document):
    name = StringField()
