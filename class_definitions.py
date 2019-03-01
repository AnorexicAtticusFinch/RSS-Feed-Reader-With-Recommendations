class article:

    def __init__(self, title: str, description: str, link: str):

        """
        Takes initial values from the parameter and gives them to the data members
        """

        self.title = title
        self.description = description
        self.link = link

    def __eq__(self, article_2: article) -> bool:

        """
        Operator overloading for ==
        Should return true or false
        Compares links
        """

        return self.link == article_2.link
    
    def __str__(self) -> str:

        """
        Defines behavior for str() and print()
        Returns a string
        """

        return self.title + "\n" + self.description + "\n"

    def open_link(self): #NEEDS TO BE TESTED

        """
        Opens browser window and opens the article page using the selenium package
        """

        from selenium import webdriver

        browser = webdriver.Chrome()
        browser.get(self.link)
        
class feed_source:

    def __init__(self, name: str, link: str, description: str = ""):

        """
        Takes initial values from the parameter and gives them to the data members
        Downloads xml file by calling get_xml_file()  and saves it as a .txt file
        Obtains atmost 10 articles from the saved xml file
        """

        self.name = name
        self.link = link
        self.description = description
        self.get_xml_file()
        self.articles = self.get_articles(10)


    def __eq__(self, source_2: feed_source) -> bool:

        """
        Operator overloading for ==
        Should return true or false
        Compares rss links
        """

        return self.link == source_2.link

    def __str__(self) -> str:

        """
        Defines behavior for str() and print()
        Returns a string
        """

        if self.description != "":
            return self.name + "\n" + self.description + "\n"
        else:
            return self.name + "\n"

    def open_file(self): #TO DO
        pass

    def close_file(self, file): #TO DO
        pass
    
    def get_xml_file(self): #TO DO

        """
        Downloads xml file from the rss link
        Saves the entire xml file as source_name.txt
        """

        pass
    
    def get_titles(self, num: int) -> "list of strs": #TO DO

        """
        Obtains "num" titles from the saved xml file by searching for the title tag
        Returns a list of "num" titles
        """

        pass

    def get_links(self, num: int) -> "list of strs": #TO DO
        
        """
        Obtains "num" links from the saved xml file by searching for the link tag
        Returns a list of "num" links
        """

        pass

    def get_descriptions(self, num: int) -> "list of strs": #TO DO
        
        """
        Obtains "num" descriptions from the saved xml file by searching for the description tag
        Returns a list of "num" descriptions
        """

        pass
    
    def get_articles(self, num: int) -> "list of articles": #TO DO

        """
        Obtains "num" articles from the saved xml file using get_titles(), get_links() and get_description()
        Returns a list of "num" articles
        """

        pass
    
    def update_articles(self): #TO DO

        """
        Checks for any new articles by comparing the list returned by get_titles() and the titles in the saved list of articles and
        determines how many new articles are present
        Calls get_articles() using the number of new articles and updates the saved list of articles
        """

        pass
