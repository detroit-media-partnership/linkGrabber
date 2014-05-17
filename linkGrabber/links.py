class Links(object):
    """Object that will hold link data"""
    def __init__(self, text, href, seo):
        self.text = text
        self.href = href
        self.seo = seo

    def __repr__(self):
        return "<Links text={0}, href={1}>".format(self.text, self.href)

    def __str__(self):
        return str(self.__repr__)
