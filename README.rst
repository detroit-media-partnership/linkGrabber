=====
Link Grabber
=====

Link Grabber provides a quick and easy way to grab links from
a single web page.

How-To
======

.. code:: bash

    $ pip install linkGrabber

Quick
====

.. code:: python

    import linkGrabber

    seek = linkGrabber.ScrapeLinks("http://www.google.com")
    print(seek.find_links())
    print(seek.find_links(limit=5))
    print(seek.find_links({ "href": re.compile("plus.google.com") }))
