""" Module that scrapes a web page for hyperlinks """
import re
import requests
from bs4 import BeautifulSoup

class Links(object):
    """Grabs links from a web page
    based upon a URL, filters, and limits"""
    def __init__(self, href=None, text=None):
        """ Create instance of Links class

        :param href: URL to download links from
        :param text: Search through text for links instead of URL
        """
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

    def find(self, limit=None,
            reverse=False, sort=None, exclude=None, **filters):
        """ Using filters and sorts, this finds all hyperlinks
        on a web page 

        :param limit: Crop results down to limit specified 
        :param reverse: Reverse the list of links, useful for before limiting 
        :param exclude: Remove links from list 
        :param filters: All the links to search for """
        if filters is None:
            filters = {}
        search = self._soup.findAll('a', **filters)

        if reverse:
            search.reverse()

        links = []
        for anchor in search:
            build_link = anchor.attrs
            try:
                build_link[u'seo'] = seoify_hyperlink(anchor['href'])
            except KeyError:
                pass

            try:
                build_link[u'text'] = anchor.string or build_link['seo']
            except KeyError:
                pass

            links.append(build_link)

            if limit is not None and len(links) == limit:
                break

        if exclude:
            pop_elem = []
            for key, value in exclude.iteritems():
                for item in links:
                    if key in item and (value == item[key] or value.search(item[key])):
                        links.remove(item)

        if sort is not None:
            links = sorted(links, key=sort, reverse=reverse)

        return links


def seoify_hyperlink(hyperlink):
    """Modify a hyperlink to make it SEO-friendly by replacing
    hyphens with spaces and trimming multiple spaces.

    :param hyperlink: URL to attempt to grab SEO from """
    last_slash = hyperlink.rfind('/')
    return re.sub(r' +|-', ' ', hyperlink[last_slash+1:])
