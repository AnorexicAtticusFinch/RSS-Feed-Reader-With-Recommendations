class article:

    def __init__(self):

        """
        Takes initial values from the parameter and gives them to the data members
        """

        #title
        #description
        #link

        pass

    def __eq__(self, article_2):

        """
        Operator overloading for ==
        Should return true or false
        Compares links
        """

        pass
    
    def __str__(self):

        """
        Defines behavior for str() and print()
        Returns a string
        """

        pass

    def open_link(self):

        """
        Opens browser window and opens the article page using the selenium package
        """

        pass
        
class feed_source:

    def __init__(self):

        """
        Takes initial values from the parameter and gives them to the data members
        Downloads xml file by calling get_xml_file()  and saves it as a .txt file
        Obtains atmost 10 articles from the saved xml file
        """

        #rss link
        #list of articles - 10 - list
        #category
        #xml code saved path

        pass

    def __eq__(self, source_2):

        """
        Operator overloading for ==
        Should return true or false
        Compares rss links
        """

        pass

    def __str__(self):

        """
        Defines behavior for str() and print()
        Returns a string
        """

        pass
    
    def get_xml_file(self):

        """
        Downloads xml file from the rss link
        Returns the entire xml file
        """

        pass
    
    def get_titles(self, num):

        """
        Obtains "num" titles from the saved xml file by searching for the title tag
        Returns a list of "num" titles
        """

        pass

    def get_links(self, num):
        
        """
        Obtains "num" links from the saved xml file by searching for the link tag
        Returns a list of "num" links
        """

        pass

    def get_descriptions(self, num):
        
        """
        Obtains "num" descriptions from the saved xml file by searching for the description tag
        Returns a list of "num" descriptions
        """

        pass
    
    def get_articles(self, num):

        """
        Obtains "num" articles from the saved xml file using get_titles(), get_links() and get_description()
        Returns a list of "num" articles
        """

        pass
    
    def update_articles(self):

        """
        Checks for any new articles by comparing the list returned by get_titles() and the titles in the saved list of articles and
        determines how many new articles are present
        Calls get_articles() using the number of new articles and updates the saved list of articles
        """

        pass
