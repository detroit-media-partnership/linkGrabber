""" Module that scrapes a web page for hyperlinks """
try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen
from bs4 import BeautifulSoup

class Links(object):
    """Grabs links from a web page
    based upon a URL, filters, and limits"""
    def __init__(self, href):
        if not href.startswith('http'):
            raise Exception("URL must contain http:// or https://")
        self._href = href
        self._soup = None
        self._page()

    def __repr__(self):
        return "<Links {0}>".format(self._href)

    def _page(self):
        """ Stores page content as a BeautifulSoup object"""
        page = urlopen(self._href)
        self._soup = BeautifulSoup(page)
        return self._soup

    def find(self, filters=None, limit=None,
            reverse=False, sort=None):
        """ Using filters and sorts, this finds all hyperlinks
        on a web page """
        if filters is not None:
            search = self._soup.findAll('a', **filters)
        else:
            search = self._soup.findAll('a')

        if sort is not None:
            search = sorted(search, key=sort, reverse=reverse)

        if reverse and sort is None:
            search.reverse()

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
            links.append({
                "text": link_text,
                "href": link_href,
                "seo": link_seo
            })
            if limit is not None and len(links) >= limit:
                break

        return links
