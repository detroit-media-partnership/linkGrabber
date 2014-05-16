from __future__ import print_function
import re
import urllib2
from BeautifulSoup import BeautifulSoup
from .links import Links


class ScrapeLinks:
    """Grabs links from a web page
    based upon a URL, filters, and limits"""
    def __init__(self, href):
        self._href = href
        self._links = []

    def __repr__(self):
        return "<ScrapeLinks %r>" % self._href

    def _add_link(self, text, href):
        self._links.append(Links(text, href))

    def find_links(self, filters=None, limit=None):
        page = urllib2.urlopen(self._href)
        soup = BeautifulSoup(page)
        if filters is not None:
            search = soup.findAll('a', **filters)
        else:
            search = soup.findAll('a')
        for anchor in search:
            link_href = anchor['href']
            last_slash = anchor['href'].rfind('/')
            link_text = anchor['href'][last_slash+1:] \
                        .replace('-', ' ') \
                        .replace('  ', ' ')
            self._add_link(link_text, link_href)
            if limit is not None and len(self._links) >= limit:
                break
        return self._links

if __name__ == '__main__':
    seek = ScrapeLinks("http://www.freep.com/section/NLETTER10")
    print(seek.find_links({ "href": re.compile("www.freep.com/article"), "style": re.compile("11px") }, 5))
