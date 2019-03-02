class Article:

    def __init__(self, title: str, description: str, link: str):

        """
        Takes initial values from the parameter and gives them to the data members
        """

        self.title = title
        self.description = description
        self.link = link


    def __eq__(self, article_2: Article) -> bool:

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
        


class Feed_Source:

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


    def __eq__(self, source_2: Feed_Source) -> bool:

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


    def open_file(self):

        """
        Opens source_name.txt in read only mode
        Returns the file object
        """
        
        file = open(self.name + ".txt", "r")
        return file


    def close_file(self, file):
        
        file.close()
    

    def get_xml_file(self): #TO DO

        """
        Downloads xml file from the rss link
        Saves the entire xml file as source_name.txt
        """

        pass
    

    def get_titles(self, num: int) -> "list of strs": #NEEDS TO BE TESTED

        """
        Obtains "num" titles from the saved xml file by searching for the title tag
        Returns a list of "num" titles
        """

        file = self.open_file()
        titles = []
        num_titles = 0
        flag = False
        title = ""

        for line in file:
            while num_titles <= num:
                if flag:
                    if "</title>" in line:
                        title += line[ : line.find("</title>")]
                        titles.append(title)
                        flag = False
                        num_titles += 1
                        title = ""
                    else:
                        title += line

                if "<title>" in line:
                    flag = True
                    if "</title>" in line:
                        title += line[line.find("<title>") + len("<title>") : line.find("</title>")]
                        titles.append(title)
                        flag = False
                        num_titles += 1
                        title = ""
        
        self.close_file(file)
        return titles


    def get_links(self, num: int) -> "list of strs": #NEEDS TO BE TESTED
        
        """
        Obtains "num" links from the saved xml file by searching for the link tag
        Returns a list of "num" links
        """

        file = self.open_file()
        links = []
        num_links = 0
        flag = False
        link = ""

        for line in file:
            while num_links <= num:
                if flag:
                    if "</link>" in line:
                        link += line[ : line.find("</link>")]
                        links.append(link)
                        flag = False
                        num_links += 1
                        link = ""
                    else:
                        link += line

                if "<link>" in line:
                    flag = True
                    if "</link>" in line:
                        link += line[line.find("<link>") + len("<link>") : line.find("</link>")]
                        links.append(link)
                        flag = False
                        num_links += 1
                        link = ""
        
        self.close_file(file)
        return links


    def get_descriptions(self, num: int) -> "list of strs": #NEEDS TO BE TESTED
        
        """
        Obtains "num" descriptions from the saved xml file by searching for the description tag
        Returns a list of "num" descriptions
        """

        file = self.open_file()
        descs = []
        num_descs = 0
        flag = False
        desc = ""

        for line in file:
            while num_descs <= num:
                if flag:
                    if "</description>" in line:
                        desc += line[ : line.find("</desc>")]
                        descs.append(desc)
                        flag = False
                        num_descs += 1
                        desc = ""
                    else:
                        desc += line

                if "<desc>" in line:
                    flag = True
                    if "</desc>" in line:
                        desc += line[line.find("<description>") + len("<description>") : line.find("</description>")]
                        descs.append(desc)
                        flag = False
                        num_descs += 1
                        desc = ""
        
        self.close_file(file)
        return descs
    

    def get_articles(self, num: int) -> "list of articles": #NEEDS TO BE TESTED

        """
        Obtains "num" articles from the saved xml file using get_titles(), get_links() and get_description()
        Returns a list of "num" articles
        """

        titles = self.get_titles(num)
        num = len(titles)
        descs = self.get_descriptions(num)
        links = self.get_links(num)

        articles = []
        for _ in range(num):
            articles.append(Article(titles[_], descs[_], links[_]))
        
        return articles
    

    def update_articles(self): #NEEDS TO BE TESTED

        """
        Checks for any new articles by comparing the list returned by get_titles() and the titles in the saved list of articles and
        determines how many new articles are present
        Calls get_articles() using the number of new articles and updates the saved list of articles
        """

        self.get_xml_file()
        new_titles = self.get_titles(10)
        new_articles_num = 0

        for _ in range(10):
            if new_titles[_] == self.articles[_].title:
                break
            else:
                new_articles_num += 1
            
        if new_articles_num == 0:
            return

        new_articles = self.get_articles(new_articles_num)

        for article in new_articles:
            self.articles.pop()
            self.articles.insert(0, article)
