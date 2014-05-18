""" Module that scrapes a web page for hyperlinks """
import re
import requests
from bs4 import BeautifulSoup


class Links(object):
    """Grabs links from a web page
    based upon a URL, filters, and limits"""
    def __init__(self, href=None, text=None):
        if href is not None and not href.startswith('http'):
            raise ValueError("URL must contain http:// or https://")
        elif href is not None:
            self._href = href
            page = requests.get(self._href)
            self._text = page.text
        elif href is None and text is not None:
            self._text = text
        else:
            raise ValueError("Either href or text must not be empty")

        self._soup = BeautifulSoup(self._text)

    def __repr__(self):
        return "<Links {0}>".format(self._href or self._text[:15] + '...')

    def find(self, filters=None, limit=None,
            reverse=False, sort=None):
        """ Using filters and sorts, this finds all hyperlinks
        on a web page """
        if filters is None:
            filters = {}
        search = self._soup.findAll('a', **filters)

        if sort is not None:
            search = sorted(search, key=sort, reverse=reverse)
        elif reverse:
            search.reverse()

        links = []
        for anchor in search:
            html = str(anchor)
            #build_link = { "html": html }
            build_link = {}
            try:
                build_link['href'] = anchor['href']
                build_link['seo'] = seoify_hyperlink(anchor['href'])
            except KeyError:
                pass

            try:
                build_link['text'] = anchor.string or build_link['seo']
            except KeyError:
                pass

            links.append(build_link)
            
            if limit is not None and len(links) == limit:
                break

        return links


def seoify_hyperlink(hyperlink):
    """Modify a hyperlink to make it SEO-friendly by replacing
    hyphens with spaces and trimming multiple spaces."""
    last_slash = hyperlink.rfind('/')
    return re.sub(r' +|-', ' ', hyperlink[last_slash+1:])
