import requests
from unittest import TestCase

from ppp_datamodel.communication import Response
from example_ppp_module import requesthandler

class FlowerTestCase(TestCase):
    def testFlowerAnswers(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "en", "trace": [], "measures": {}, "tree": {"type": "triple", "subject": {"type": "resource", "value": "you"}, "object": {"type": "missing"}, "predicate": {"type": "resource", "value": "identity"}}}').json()
        r = list(map(Response.from_dict, r))
        self.assertGreaterEqual(len(r), 1, r)
        got_actual_answer = False
        for o in r:
            if o.tree.type == 'resource':
                if o.tree.value in requesthandler.YOU_ARE:
                    got_actual_answer = True
        self.assertTrue(got_actual_answer, r)
