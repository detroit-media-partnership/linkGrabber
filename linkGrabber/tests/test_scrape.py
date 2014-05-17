from __future__ import print_function
import unittest
import bs4
from linkGrabber import ScrapeLinks

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.url = "http://www.google.com"
        self.bad_url = "www.google.com"

    def test_url(self):
        self.assertRaises(Exception, ScrapeLinks, self.bad_url)

    def test_grab_page(self):
        seek = ScrapeLinks(self.url)
        self.assertIsInstance(seek._get_page(), bs4.BeautifulSoup)

    def test_find_links(self):
        seek = ScrapeLinks(self.url)
        self.assertRaises(Exception, seek.find_links, limit="hi")
        self.assertRaises(Exception, seek.find_links, filters=['href', 'style'])
        self.assertRaises(Exception, seek.find_links, filters=25)
        self.assertEqual(len(seek.find_links(limit=5)), 5)
        self.assertEqual(len(seek.find_links(limit=1)), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
