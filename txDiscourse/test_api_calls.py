from twisted.trial import unittest
import time
import logging
from dc_client import DiscourseClient
import os

from twisted.internet.base import DelayedCall
DelayedCall.debug = True

logger = logging.getLogger("TEST_DiscourseAPI")


class TestTopic(unittest.TestCase):

    def setUp(self):
        host = os.environ.get('DC_HOST')
        api_key = os.environ.get('DC_API_KEY')
        username = os.environ.get('DC_USERNAME')
        self.client = DiscourseClient(host, api_key, username)
        self.topic_id = 1

    def test_create_topic(self):
        topic_title = "Title: {}".format(time.time())
        topic_body = "With even mmore text {}".format(time.time())
        return self.client.create_topic(topic_title, topic_body)

    def test_latest(self):
        return self.client.latest_topics()

    def test_new_topics(self):
        return self.client.new_topics()

    def test_rename_topic(self):
         #Make sure topic with this id exists
        title = "We updated the title {}".format(time.time)
        return self.client.rename_topic(self.topic_id, title)

    def test_recategorize_topic(self):
        category_id = 22
        return self.client.recategorize_topic(self.topic_id, category_id)

    def test_get_topic(self):
        return self.client.get_topic(self.topic_id)

    def test_delete_topic(self):
        del_topic_id = 99
        return self.client.delete_topic(del_topic_id)




