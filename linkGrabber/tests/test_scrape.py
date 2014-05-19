""" Unit test Links functionality"""
import unittest
import requests
import vcr
import bs4

from linkGrabber import Links
from linkGrabber.tests import test_data as td

class TestScrape(unittest.TestCase):
    """ A set of unit tests for Links """
    def setUp(self):
        """ Activated on start up of class """
        self.url = "http://www.google.com"
        self.bad_url = "www.google.com"
        # grab some example html pages to test
        with vcr.use_cassette('fixtures/vcr_cassettes/first_test.yaml'):
            td.pages[0]['text'] = requests.get(td.pages[0]['url']).text

        with vcr.use_cassette('fixtures/vcr_cassettes/second_test.yaml'):
            td.pages[1]['text'] = requests.get(td.pages[1]['url']).text

    def test_url(self):
        """ Validate URL on instance instantiation """
        self.assertRaises(Exception, Links, self.bad_url)

    def test_soup_property(self):
        """ Getting the web page yields correct response"""
        seek = Links(self.url)
        self.assertIsInstance(seek._soup, bs4.BeautifulSoup)

    def test_find_bad_filter_param(self):
        """ Bad filters parameter inputs """
        seek = Links(self.url)
        self.assertRaises(Exception, seek.find, filters=25)
        self.assertRaises(Exception, seek.find, filters=['href', 'style'])

    def test_find_limit_param(self):
        """ How does find() handle the limit property """
        seek = Links(self.url)
        self.assertEqual(len(seek.find(limit=5)), 5)
        self.assertEqual(len(seek.find(limit=1)), 1)

    def test_find_number_of_links(self):
        """ Ensure expected number of links reflects actual number of links """
        for page in td.pages:
            seek = Links(text=page['text'])
            self.assertEqual(len(seek.find()), page['num_links'])

    def test_find_limit(self):
        """ Check that the actual array with a limit matches the test data """
        for page in td.pages:
            seek = Links(text=page['text'])
            actual_list = seek.find(limit=5)
            self.assertEqual(len(actual_list), len(page['limit_find']))
            for i, link in enumerate(actual_list):
                self.assertDictEqual(link, page['limit_find'][i])

    def test_find_reverse_sort(self):
        """ Ensure reverse sort sorts before limiting the # of links """
        for page in td.pages:
            seek = Links(text=page['text'])
            actual_list = seek.find(limit=5, reverse=True)
            self.assertEqual(len(actual_list), len(page['limit_reverse_find']))
            for i, link in enumerate(actual_list):
                self.assertDictEqual(link, page['limit_reverse_find'][i])

    def test_find_sort_by_text(self):
        """ Sorting by text name produces proper results """
        for page in td.pages:
            seek = Links(text=page['text'])
            actual_list = seek.find(limit=5, sort=lambda key: key['text'])
            self.assertEqual(len(actual_list), len(page['limit_sort_text']))
            for i, link in enumerate(actual_list):
                self.assertDictEqual(link, page['limit_sort_text'][i])

    def test_find_sort_by_href(self):
        """ Sorting by href produces proper results """
        for page in td.pages:
            seek = Links(text=page['text'])
            actual_list = seek.find(limit=5, sort=lambda key: key['href'] or "")
            self.assertEqual(len(actual_list), len(page['limit_sort_href']))
            for i, link in enumerate(actual_list):
                self.assertDictEqual(link, page['limit_sort_href'][i])

if __name__ == '__main__':
    unittest.main(verbosity=2)
