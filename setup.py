try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='linkGrabber',
    version='0.2.3',
    author='Eric Bower',
    author_email='neurosnap@gmail.com',
    packages=['linkGrabber', 'linkGrabber.tests'],
    scripts=[],
    url='https://github.com/detroit-media-partnership/linkGrabber',
    license='LICENSE.txt',
    description='Scrape links from a single web site',
    long_description=open('README.rst').read(),
    install_requires=["requests", "beautifulsoup4"],
    tests_require=['unittest', 'vcrpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License'
    ]
)
