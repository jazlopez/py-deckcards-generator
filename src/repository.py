class Repository(object):

    class Item(object):

        term = None

        definition = None

    MAGIC_SEP = "->"

    path = None

    def __init__(self, path=None):

        self.path = path

        self.cards = list()

    def read(self):

        """
        read repository file
        :return:
        """

        with open(self.path, "r") as source:

            content = source.readlines()

        return content

    def parse(self, content):

        """
        parse content
        :param content:
        :return:
        """
        flush = False
        body_term = ""
        body_definition = ""

        for statement in content:

            extract = statement.split(self.MAGIC_SEP)

            if len(extract) > 1:
                if flush:
                    self.persist(term=body_term, definition=body_definition)

                body_term = extract[0]
                body_definition = "\n>>\t" + "".join(extract[1:])
                flush = True
                continue

            body_definition += "\t" + statement.strip(" ")

        if flush:
            self.persist(term=body_term, definition=body_definition)

    def persist(self, term=None, definition=None):

        """
        store term definition pair of values into memory
        :param term:
        :param definition:
        :return:
        """

        item = Repository.Item()
        item.term = term
        item.definition = definition

        self.cards.append(item)

    def load(self):

        """
        load term definitions into memory
        :return:
        """
        self.parse(self.read())

        return self.cards
