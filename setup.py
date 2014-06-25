try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='linkGrabber',
    version='0.2.6',
    author='Eric Bower',
    author_email='neurosnap@gmail.com',
    packages=['linkGrabber', 'linkGrabber.tests'],
    scripts=[],
    url='https://github.com/detroit-media-partnership/linkGrabber',
    license=read('LICENSE.txt'),
    description='Scrape links from a single web page',
    long_description=read('README.rst') + '\n\n' + read('CHANGES.rst'),
    install_requires=["requests", "beautifulsoup4"],
    tests_require=['nosetest', 'vcrpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License'
    ],
    keywords=['linkgrabber', 'beautifulsoup', 'scraper',
                'html', 'parser', 'hyperlinks']
)
