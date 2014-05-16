=====
Link Grabber
=====

Link Grabber provides a quick and easy way to grab links from
a single web page.

pypi_

.. _pypi: https://pypi.python.org/pypi/linkGrabber/

How-To
======

.. code:: bash

    $ python setup.py install

OR

.. code:: bash

    $ pip install linkGrabber

Quick
====

.. code:: python

    import linkGrabber

    seek = linkGrabber.ScrapeLinks("http://www.google.com")
    seek.find_links()
    # limit the number of "a" tags to 5
    seek.find_links(limit=5)
    # filter the "a" tag href attribute
    seek.find_links({ "href": re.compile("plus.google.com") })
