""" Module that scrapes a web page for hyperlinks """
import re
import requests
import collections
import pprint

from bs4 import BeautifulSoup

class Links(object):
    """Grabs links from a web page
    based upon a URL and filters"""
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

    def find(self, limit=None, reverse=False, sort=None,
            exclude=None, duplicates=True, pretty=False, **filters):
        """ Using filters and sorts, this finds all hyperlinks
        on a web page

        :param limit: Crop results down to limit specified
        :param reverse: Reverse the list of links, useful for before limiting
        :param exclude: Remove links from list
        :param duplicates: Determines if identical URLs should be displayed
        :param pretty: Quick and pretty formatting using pprint
        :param filters: All the links to search for """
        if exclude is None:
            exclude = []

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

            ignore_link = False
            for nixd in exclude:
                for key, value in iteritems(nixd):
                    if key in build_link:
                        if isinstance(build_link[key], collections.Iterable):
                            for item in build_link[key]:
                                ignore_link = exclude_match(value, item)
                        else:
                            ignore_link = exclude_match(value, build_link[key])

            if not duplicates:
                for link in links:
                    if link['href'] == anchor['href']:
                        ignore_link = True

            if not ignore_link:
                links.append(build_link)

            if limit is not None and len(links) == limit:
                break

        if sort is not None:
            links = sorted(links, key=sort, reverse=reverse)

        if pretty:
            pp = pprint.PrettyPrinter(indent=4)
            return pp.pprint(links)
        else:
            return links

def exclude_match(exclude, link_value):
    """ Check excluded value against the link's current value """
    if hasattr(exclude, "search") and exclude.search(link_value):
        return True

    if exclude == link_value:
        return True

    return False

def seoify_hyperlink(hyperlink):
    """Modify a hyperlink to make it SEO-friendly by replacing
    hyphens with spaces and trimming multiple spaces.

    :param hyperlink: URL to attempt to grab SEO from """
    last_slash = hyperlink.rfind('/')
    return re.sub(r' +|-', ' ', hyperlink[last_slash+1:])

def iteritems(d):
    """ Factor-out Py2-to-3 differences in dictionary item
    iterator methods """
    try:
         return d.iteritems()
    except AttributeError:
         return d.items()