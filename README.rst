=====
Link Grabber
=====

Link Grabber provides a quick and easy way to grab links from
a single web page.

How-To
======

    $ pip install linkGrabber

Quick
====

    import linkGrabber

    seek = linkGrabber.ScrapeLinks("www.google.com")
    print(seek.find_links())
