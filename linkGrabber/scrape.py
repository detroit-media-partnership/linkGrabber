""" Module that scrapes a web page for hyperlinks """

# You might want to replace urllib* with the `requests` library;
# it's well-written, well-documented, and heavily used.
# If you find yourself writing a lot of HTTP client 
# code, you will thank youself for the effort.
# Additionally, since requests works on py2 and 3, you
# won't find yourself needing this type of hack.
try:
    from urllib.request import urlopen
# Be specific with your exception classes, if possible
#except:
except ImportError:
    from urllib2 import urlopen
import re

# Generally should separate your stdlib imports
# from your third-partly lib imports with a blank line.
# It sounds nitpicky, but at scale the benefit is clear.
# http://legacy.python.org/dev/peps/pep-0008/#imports
from bs4 import BeautifulSoup


class Links(object):
    """Grabs links from a web page
    based upon a URL, filters, and limits"""
    def __init__(self, href):
        if not href.startswith('http'):
            # ValueError is appropriate for 'hey you didnt pass the 
            # right type of arg'.
            #raise Exception("URL must contain http:// or https://")
            raise ValueError("URL must contain http:// or https://")
        self._href = href
        self._soup = None
        self._page()

    def __repr__(self):
        return "<Links {0}>".format(self._href)

    def _page(self):
        """ Stores page content as a BeautifulSoup object"""
        # Not sure why you decided to abstract this out of __init__,
        # but it shows that your mind is in the right place.
        # I have seen too many 400-line functions that make my eyes bleed.
        page = urlopen(self._href)
        self._soup = BeautifulSoup(page)
        return self._soup

    def find(self, filters=None, limit=None,
            reverse=False, sort=None):
        """ Using filters and sorts, this finds all hyperlinks
        on a web page """
        # You could replace this if/else block with:
        #   if filters is None:
        #       filters = {}
        #   search = self._soup.findAll('a', **filters)
        if filters is not None:
            search = self._soup.findAll('a', **filters)
        else:
            search = self._soup.findAll('a')

        if sort is not None:
            search = sorted(search, key=sort, reverse=reverse)

        # You could probably get away with:
        #   elif reverse:
        #       search.reverse()
        # here, but that's less explicit (though it's "clever-er",
        # which does not always equal "better").
        if reverse and sort is None:
            search.reverse()

        links = []
        for anchor in search:
            link_href = anchor['href']
            # Abstract out useful functionality into another
            # function.  Perhaps you will reuse this.
            #last_slash = anchor['href'].rfind('/')
            #link_seo = anchor['href'][last_slash+1:] \
            #            .replace('-', ' ') \
            #            .replace('  ', ' ')
            link_seo = seoify_hyperlink(anchor['href'])
            
            # Condense if/else block into one-liner
            #if anchor.string is None:
            #    link_text = link_seo
            #else:
            #    link_text = anchor.string
            link_text = anchor.string or link_seo

            links.append({
                "text": link_text,
                "href": link_href,
                "seo": link_seo
            })
            
            # No need to check for '>=', since '==' would suffice.
            # I didn't change it, since it really doesn't matter.
            if limit is not None and len(links) >= limit:

        return links


def seoify_hyperlink(hyperlink):
    """Modify a hyperlink to make it SEO-friendly by replacing
    hyphens with spaces and trimming multiple spaces."""
    last_slash = hyperlink.rfind('/')
    # use the `re` module instead of multiple calls to `string.replace`.
    #link_seo = hyperlink[last_slash+1:] \
    #            .replace('-', ' ') \
    #            .replace('  ', ' ')
    return re.sub(r' +|-', ' '. [last_slash+1:])
