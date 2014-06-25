import re

from linkGrabber import Links


links = Links("http://www.detroitnews.com/section/NLETTER04")
links.find(limit=2, duplicates=False, pretty=True,
			href=re.compile("www.detroitnews.com/article"),
			exclude=[{"href":re.compile("99999999")}])