class Links:
    """Object that will hold link data"""
    def __init__(self, text, href, seo):
        self.text = text
        self.href = href
        self.seo = seo

    def __repr__(self):
        return "<Links text=%r, href=%r>" % (self.text, self.href)

    def __str__(self):
        return str(self.__repr__)
