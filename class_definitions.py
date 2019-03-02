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
    
    
    def get_instances(self, num: int, tag: str) -> "list of strs": #NEEDS TO BE TESTED

        """
        Obtains "num" instances from the saved xml file by searching for the instance tag
        Returns a list of "num" instances
        """

        start_tag = "<" + tag + ">"
        end_tag = "</" + tag + ">"

        file = self.open_file()
        instances = []
        num_instances = 0
        flag = False
        instance = ""

        for line in file:
            while num_instances <= num:
                if flag:
                    if end_tag in line:
                        instance += line[ : line.find(end_tag)]
                        instances.append(instance)
                        flag = False
                        num_instances += 1
                        instance = ""
                    else:
                        instance += line

                if start_tag in line:
                    flag = True
                    if end_tag in line:
                        instance += line[line.find(start_tag) + len(start_tag) : line.find(end_tag)]
                        instances.append(instance)
                        flag = False
                        num_instances += 1
                        instance = ""
        
        self.close_file(file)
        return instances
   

    def get_articles(self, num: int) -> "list of articles": #NEEDS TO BE TESTED

        """
        Obtains "num" articles from the saved xml file using get_titles(), get_links() and get_description()
        Returns a list of "num" articles
        """

        titles = self.get_instances(num, "title")
        num = len(titles)
        descs = self.get_instances(num, "description")
        links = self.get_instances(num, "link")

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
        new_titles = self.get_instances(10, "title")
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
