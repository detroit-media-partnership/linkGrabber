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
        self._soup = None

    def __repr__(self):
        return "<ScrapeLinks %r>" % self._href

    def _add_link(self, text, href, seo):
        self._links.append(Links(text, href, seo))

    def _get_page(self):
        page = urllib2.urlopen(self._href)
        self._soup = BeautifulSoup(page)
        return self._soup

    def find_links(self, filters=None, limit=None):
        if self._soup is None:
            self._get_page()
        if filters is not None:
            search = self._soup.findAll('a', **filters)
        else:
            search = self._soup.findAll('a')
        for anchor in search:
            link_href = anchor['href']
            last_slash = anchor['href'].rfind('/')
            link_seo = anchor['href'][last_slash+1:] \
                        .replace('-', ' ') \
                        .replace('  ', ' ')
            try:
                link_text = anchor.string
            except:
                link_text = link_seo
            self._add_link(link_text, link_href, link_seo)
            if limit is not None and len(self._links) >= limit:
                break
        return self._links

if __name__ == '__main__':
    seek = ScrapeLinks("http://www.freep.com/section/NLETTER10")
    print(seek.find_links({ "href": re.compile("www.freep.com/article"), "style": re.compile("11px") }, 5))
