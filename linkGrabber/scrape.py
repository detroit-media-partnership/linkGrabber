""" Module that scrapes a web page for hyperlinks """
import re
import requests
from bs4 import BeautifulSoup


class Links(object):
    """Grabs links from a web page
    based upon a URL, filters, and limits"""
    def __init__(self, href=None):
        if href is not None and not href.startswith('http'):
            raise ValueError("URL must contain http:// or https://")
        self._href = href
        page = requests.get(self._href)
        self._soup = BeautifulSoup(page.text)

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
            link_href = anchor['href']
            link_seo = seoify_hyperlink(anchor['href'])
            link_text = anchor.string or link_seo

            links.append({
                "text": link_text,
                "href": link_href,
                "seo": link_seo
            })
            
            if limit is not None and len(links) == limit:
                break

        return links


def seoify_hyperlink(hyperlink):
    """Modify a hyperlink to make it SEO-friendly by replacing
    hyphens with spaces and trimming multiple spaces."""
    last_slash = hyperlink.rfind('/')
    return re.sub(r' +|-', ' ', hyperlink[last_slash+1:])
