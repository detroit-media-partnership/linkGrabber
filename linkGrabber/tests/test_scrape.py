""" Unit test ScrapeLinks functionality"""
import unittest
import bs4
from linkGrabber import Links

class TestScrape(unittest.TestCase):
    """ A set of unit tests for ScrapeLinks """
    def setUp(self):
        """ Activated on start up of class """
        self.url = "http://www.google.com"
        self.bad_url = "www.google.com"

    def test_url(self):
        """ Validate URL on instance instantiation """
        self.assertRaises(Exception, Links, self.bad_url)

    def test_page(self):
        """ Getting the web page yields correct response"""
        seek = Links(self.url)
        self.assertIsInstance(seek._page(), bs4.BeautifulSoup)

    def test_find(self):
        """ Test how grabbing the hyperlinks are aggregated """
        seek = Links(self.url) 
        self.assertRaises(Exception, seek.find, filters=['href', 'style'])
        self.assertRaises(Exception, seek.find, filters=25)
        self.assertEqual(len(seek.find(limit=5)), 5)
        self.assertEqual(len(seek.find(limit=1)), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)