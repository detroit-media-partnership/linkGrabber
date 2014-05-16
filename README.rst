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

.. code:: python

    import re
    from linkGrabber import ScrapeLinks

    seek = linkGrabber.ScrapeLinks("http://www.google.com")
    seek.find_links({ "style": re.compile("11px")  }, 5)

