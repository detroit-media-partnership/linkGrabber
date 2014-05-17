from __future__ import print_function
import urllib2
from BeautifulSoup import BeautifulSoup
from .links import Links

class ScrapeLinks:
    """Grabs links from a web page
    based upon a URL, filters, and limits"""
    def __init__(self, href):
        if 'http://' not in href and 'https://' not in href:
            raise Exception("URL must contain http:// or https://")
        self._href = href
        self._soup = None
        self._get_page()

    def __repr__(self):
        return "<ScrapeLinks %r>" % self._href

    def _get_page(self):
        page = urllib2.urlopen(self._href)
        self._soup = BeautifulSoup(page)
        return self._soup

    def find_links(self, filters=None, limit=None, sort_reverse=False, sort=None):
        if filters is not None and not isinstance(filters, dict):
            raise Exception("filters parameter must be a dictionary")
        if limit is not None and not isinstance(limit, int):
            raise Exception("limit parameter must be an integer")
        if sort is not None and not hasattr(sort, "__call__"):
            raise Exception("sort parameter must be a function")

        if filters is not None:
            search = self._soup.findAll('a', **filters)
        else:
            search = self._soup.findAll('a')

        if sort is not None:
            search = sorted(search, key=sort, reverse=sort_reverse)

        if sort_reverse is not None and sort is None:
            search = sorted(search, reverse=sort_reverse)

        links = []
        for anchor in search:
            link_href = anchor['href']
            last_slash = anchor['href'].rfind('/')
            link_seo = anchor['href'][last_slash+1:] \
                        .replace('-', ' ') \
                        .replace('  ', ' ')
            if anchor.string is None:
                link_text = link_seo
            else:
                link_text = anchor.string
            links.append(Links(link_text, link_href, link_seo))
            if limit is not None and len(links) >= limit:
                break
        return links
