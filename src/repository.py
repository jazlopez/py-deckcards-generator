class Repository(object):

    class Item(object):

        term = None

        definition = None

    path = None

    def __init__(self, path=None):

        self.path = path

    def load(self):

        elements = list()

        elements.append(Repository.Item())

        return elements
