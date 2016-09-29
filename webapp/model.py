from mongoengine import *
import os

connect('simple_tasklist', host='db')


class Task(Document):
    name = StringField()
