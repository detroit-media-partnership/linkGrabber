class Links(object):
    """Object that will hold link data"""
    def __init__(self, text, href, seo):
        self.text = text.encode('utf-8')
        self.href = href.encode('utf-8')
        self.seo = seo.encode('utf-8')

    def __repr__(self):
        return "<Links text={0}, href={1}>".format(self.text, self.href)

    def __str__(self):
        return str(self.__repr__)
