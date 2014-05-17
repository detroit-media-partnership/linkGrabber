""" Unit test ScrapeLinks functionality"""
from __future__ import print_function
import unittest
import bs4
from linkGrabber import ScrapeLinks

class TestScrape(unittest.TestCase):
    """ A set of unit tests for ScrapeLinks """
    def setUp(self):
        """ Activated on start up of class """
        self.url = "http://www.google.com"
        self.bad_url = "www.google.com"

    def test_url(self):
        """ Validate URL on instance instantiation """
        self.assertRaises(Exception, ScrapeLinks, self.bad_url)

    def test_grab_page(self):
        """ Getting the web page yields correct response"""
        seek = ScrapeLinks(self.url)
        self.assertIsInstance(seek._get_page(), bs4.BeautifulSoup)

    def test_find_links(self):
        """ Test how grabbing the hyperlinks are aggregated """
        seek = ScrapeLinks(self.url)
        self.assertRaises(Exception, seek.find_links, limit="hi")
        self.assertRaises(Exception, seek.find_links, filters=['href', 'style'])
        self.assertRaises(Exception, seek.find_links, filters=25)
        self.assertEqual(len(seek.find_links(limit=5)), 5)
        self.assertEqual(len(seek.find_links(limit=1)), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
