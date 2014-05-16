import unittest
from ..linkGrabber import ScrapeLinks

class TestScrape(unittest.TestCase):

    def setUp(self):
        pass

    def test_grab_page(self):
        url = "http://www.google.com"
        seek = ScrapeLinks(url)
        self.assertIsInstance(seek._grab_page(), Soup)

    def test_find_links(self):
        url = "http://www.google.com"
        seek = ScrapeLinks(url)
        self.assertEqual(len(seek.find_links(limit=5)), 5)
        self.assertEqual(len(seek.find_links(limit=1)), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
