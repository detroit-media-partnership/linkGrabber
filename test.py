import re
import linkGrabber as lg

if __name__ == '__main__':
    links = lg.Links("http://www.detroitnews.com/section/NLETTER04")
    print links.find(href=re.compile("www.detroitnews.com/article"), limit=5, exclude={"text":re.compile("Read More")})
