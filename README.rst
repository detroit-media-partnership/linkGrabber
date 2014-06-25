=====
Link Grabber
=====

Link Grabber provides a quick and easy way to grab links from
a single web page.  This python package is a simple wrapper 
around `BeautifulSoup <http://www.crummy.com/software/BeautifulSoup/>`_, focusing on grabbing HTML's 
hyperlink tag, "a." 

Dependecies:

*  BeautifulSoup
*  Requests

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

    links = linkGrabber.Links("http://www.google.com")
    links.find()
    # limit the number of "a" tags to 5
    links.find(limit=5)
    # filter the "a" tag href attribute
    links.find(href=re.compile("plus.google.com"))

Documentation
=============

find
----------

Parameters: 
 *  filters (dict): Beautiful Soup's filters as a dictionary
 *  limit (int):  Limit the number of links in sequential order
 *  reverse (bool): Reverses how the list of <a> tags are sorted
 *  sort (function):  Accepts a function that accepts which key to sort upon
    within the List class

Find all links that have a style containing "11px"

.. code:: python

    import re
    from linkGrabber import Links

    links = Links("http://www.google.com")
    links.find(style=re.compile("11px"), limit=5)

Reverse the sort before limiting links:

.. code:: python

    from linkGrabber import Links

    links = Links("http://www.google.com")
    links.find(limit=2, reverse=True)

Sort by a link's  attribute:

.. code:: python

    from linkGrabber import Links

    links = Links("http://www.google.com")
    links.find(limit=3, sort=lambda key: key['text'])

Exclude text:

.. code:: python

    import re

    from linkGrabber import Links

    links = Links("http://www.google.com")
    links.find(exclude=[{ "text": re.compile("Read More") }])

Remove duplicate URLs and make the output pretty:

.. code:: python

    from linkGrabber import Links

    links = Links("http://www.google.com")
    links.find(duplicates=False, pretty=True)

Link Dictionary
---------------

All attrs from BeautifulSoup's Tag object are available in the dictionary
as well as a few extras:

*  text (text inbetween the <a></a> tag)
*  seo (parse all text after last "/" in URL and attempt to make it human readable)
