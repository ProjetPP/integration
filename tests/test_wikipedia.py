import requests
from unittest import TestCase

from ppp_datamodel import Triple
from ppp_datamodel.communication import Response

class WikipediaTestCase(TestCase):
    def testWikipediaAnswers(self):
        r = requests.post('http://ppp.pony.ovh:9000/core/', data='{"id": "", "language": "fr", "trace": [], "measures": {}, "tree": {"type": "triple", "subject": {"type": "resource", "value": "Barcelone"}, "object": {"type": "missing"}, "predicate": {"type": "resource", "value": "identity"}}}').json()
        r = list(filter(lambda x:not isinstance(x.tree, Triple),
                        map(Response.from_dict, r)))
        self.assertGreaterEqual(len(r), 1, r)
        for o in r:
            self.assertEqual(o.tree.type, 'resource')
