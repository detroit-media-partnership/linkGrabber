try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='linkGrabber',
    version='0.2.1',
    author='Eric Bower',
    author_email='neurosnap@gmail.com',
    packages=['linkGrabber', 'linkGrabber.tests'],
    scripts=[],
    url='https://github.com/detroit-media-partnership/linkGrabber',
    license='LICENSE.rst',
    description='Scrape links from a single web site',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
)
