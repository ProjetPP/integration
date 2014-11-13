import requests
from unittest import TestCase

class FlowerTestCase(TestCase):
    def testFlowerAnswers(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "triple", "subject": {"type": "resource", "value": "you"}, "object": {"type": "missing"}, "predicate": {"type": "resource", "value": "be"}}}').json()
