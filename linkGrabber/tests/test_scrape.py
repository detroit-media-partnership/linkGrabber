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
        # Each of these assertions should have their own test method.
        self.assertRaises(Exception, seek.find, filters=['href', 'style'])
        # ex: "test_find_hyperlink_bad_filter_param"
        self.assertRaises(Exception, seek.find, filters=25)
        self.assertEqual(len(seek.find(limit=5)), 5)
        self.assertEqual(len(seek.find(limit=1)), 1)

if __name__ == '__main__':
    # You should instead gain experience with a test runner.
    # They will discover your unit tests, and run them.
    # py.test, the latest-and-greatest
    # http://pytest.org/latest/
    # Nose, very popular
    # https://nose.readthedocs.org/en/latest/
    # Also consider tox, if you want to run your tests
    # on both py2 and 3 (which I think you do, judging by scrape.py):
    # http://tox.readthedocs.org/en/latest/
    unittest.main(verbosity=2)
