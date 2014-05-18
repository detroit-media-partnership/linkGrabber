""" Unit test ScrapeLinks functionality"""
import os.path
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

    def test_soup_property(self):
        """ Getting the web page yields correct response"""
        seek = Links(self.url)
        self.assertIsInstance(seek._soup, bs4.BeautifulSoup)

    def test_find_bad_filter_param(self):
        """ Bad filter param inputs """
        seek = Links(self.url)
        self.assertRaises(Exception, seek.find, filters=25)
        self.assertRaises(Exception, seek.find, filters=['href', 'style'])

    def test_find_limit_param(self):
        """ How does find() handle the limit property """
        seek = Links(self.url)
        self.assertEqual(len(seek.find(limit=5)), 5)
        self.assertEqual(len(seek.find(limit=1)), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
