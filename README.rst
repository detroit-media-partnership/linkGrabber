=====
Link Grabber
=====

Link Grabber provides a quick and easy way to grab links from
a single web page.  This python package is a simple wrapper 
around BeautifulSoup_, specifically focusing on grabbing HTML's 
hyperlink tag, "a."  It essentially wraps around find_all_ specifically
for the "a" tag and opens all the filters that you can apply in 
Beautiful Soup into linkGrabber's filter parameter.

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/

.. _find_all: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all

pypi_

.. _pypi: https://pypi.python.org/pypi/linkGrabber/

GitHub_

.. _GitHub: https://github.com/detroit-media-partnership/link-grabber

Dependecies:

*  BeautifulSoup

How-To
======

.. code:: bash

    $ python setup.py install

OR

.. code:: bash

    $ pip install linkGrabber

Quickie
=======

.. code:: python

    import re
    import linkGrabber

    seek = linkGrabber.ScrapeLinks("http://www.google.com")
    seek.find_links()
    # limit the number of "a" tags to 5
    seek.find_links(limit=5)
    # filter the "a" tag href attribute
    seek.find_links({ "href": re.compile("plus.google.com") })

Documentation
=============

find_links
----------

Parameters: 
 *  filters: Beautiful Soup's filters as a dictionary
 *  limit:  Limit the number of links in sequential order
 *  limit_reverse: Reverses how the list of <a> tags are sorted
 *  limit_sort:  Accepts a function that accepts which key to sort upon
    within the List class

Find all links that have a style containing "11px"

.. code:: python

    import re
    from linkGrabber import ScrapeLinks

    seek = ScrapeLinks("http://www.google.com")
    seek.find_links({ "style": re.compile("11px")  }, 5)

Reverse the sort before limiting links:

.. code:: python

    from linkGrabber import ScrapeLinks

    seek = ScrapeLinks("http://www.google.com")
    seek.find_links(limit=2, limit_reverse=True)

Sort by Links property:

.. code:: python

    from linkGrabber import ScrapeLinks

    seek = ScrapeLinks("http://www.google.com")
    seek.find_link(limit=3, limit_sort=lambda key: key.text)


