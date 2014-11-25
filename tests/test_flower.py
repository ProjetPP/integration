import requests
from unittest import TestCase

from ppp_datamodel.communication import Response
from example_ppp_module import requesthandler

class FlowerTestCase(TestCase):
    def testFlowerAnswers(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "triple", "subject": {"type": "resource", "value": "you"}, "object": {"type": "missing"}, "predicate": {"type": "resource", "value": "identity"}}}').json()
        r = list(map(Response.from_dict, r))
        self.assertEqual(len(r), 1, r)
        o = r[0]
        self.assertEqual(o.tree.type, 'resource')
        self.assertIn(o.tree.value, requesthandler.YOU_ARE)
