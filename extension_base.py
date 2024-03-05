class ExtensionBase:
    """
    Base class to implement the extension
    Implement all required methods
    """

    def get_home_page(self):
        """
        Required
        Get the home page of the site
        :return: return a list of audiobooks
        :rtype: List[AudioBook]
        """
        raise Exception('Implement this method.')

    def get_book_details(self, url: str):
        """
        Required
        Get specific book details using the url
        :param url: url of the book
        :type url: str
        :return: return Audiobook
        :rtype: AudioBook
        """
        raise Exception('Implement this method.')

    def search_book(self, search_term: str):
        """
        Required
        Search the site
        :param search_term:
        :type search_term:str
        :return: return a list of audiobooks
        :rtype: List[AudioBook]
        """
        raise Exception('Implement this method.')
