import redis
import sys
from flask import current_app

class Publisher():

    def __init__(self):
        self. r = redis.Redis(host='redis', port=6379, db=0)

    def publish_message(self, channel, message):
        self.r.publish(channel, message)
