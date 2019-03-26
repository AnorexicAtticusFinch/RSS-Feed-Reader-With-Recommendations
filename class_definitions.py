def update_feature_vector(xml_file : str) -> "list of floats": #NEEDS TO BE TESTED

    xml_file = xml_file.lower()
    file_categories = open("list_of_categories.txt", "r")
    vector = []

    for category in file_categories:
            
        vector.append(0)
        file_keywords = open(category + ".txt", "r")

        for keyword in file_keywords:

            vector[-1] += xml_file.count(keyword)
        
        file_keywords.close()
    
    file_categories.close()
    total_count = sum(vector)
    vector = [element / total_count for element in vector]
    return vector



class Article:

    def __init__(self, title: str, description: str, link: str):

        """
        Takes initial values from the parameter and gives them to the data members
        """

        self.title = self.parse(title)
        self.description = self.parse(description)
        self.link = link


    def __eq__(self, article_2) -> bool:

        """
        Operator overloading for ==
        Should return true or false
        Compares links
        """

        return self.link == article_2.link
    

    def __str__(self) -> str: #NEEDS TO BE TESTED

        """
        Defines behavior for str() and print()
        Returns a string
        """

        return self.title + "\n" + self.description + "\n"


    def open_link(self):

        """
        Opens browser window and opens the article page using the selenium package
        """

        from selenium import webdriver

        browser = webdriver.Chrome()
        browser.get(self.link)
        #input() #NEEDS TO BE TESTED AT THE END

    
    def parse(self, text: str) -> str:

        return text.replace("\\", "").replace("amp;", "").replace("<![CDATA[", "").replace("]]>", "").replace("xe2x80x99", "'").replace("xe2x80x94", "-").replace("xe2x80x98", "'")           
        


class Feed_Source:

    def __init__(self, name: str, link: str):

        """
        Takes initial values from the parameter and gives them to the data members
        Downloads xml file by calling get_xml_file()  and saves it as a .txt file
        Obtains atmost 10 articles from the saved xml file
        """

        self.name = name
        self.link = link
        self.get_xml_file()
        self.title = self.get_title()
        self.description = self.get_description()
        self.articles = self.get_articles(10)
        file = self.open_file()
        #self.feature_vector = update_feature_vector(file.read())
        self.close_file(file)


    def __eq__(self, source_2) -> bool:

        """
        Operator overloading for ==
        Should return true or false
        Compares rss links
        """

        return self.link == source_2.link


    def __str__(self) -> str: #NEEDS TO BE TESTED

        """
        Defines behavior for str() and print()
        Returns a string
        """

        if self.description != "":

            return self.name + "\n" + self.description + "\n"
        else:

            return self.name + "\n"


    def open_file(self, mode: str = "r"):

        """
        Opens source_name.txt in read only mode
        Returns the file object
        """
        
        file = open(self.name + ".txt", mode)
        return file


    def close_file(self, file):
        
        file.close()
    

    def get_xml_file(self):

        """
        Downloads xml file from the rss link
        Saves the entire xml file as source_name.txt
        """

        import urllib3
        import certifi

        xml_file = urllib3.PoolManager(cert_reqs = "CERT_REQUIRED", ca_certs = certifi.where()).request("get", self.link)
        file = self.open_file("w")
        file.write(str(xml_file.data))
        self.close_file(file)
    
    
    def get_instances(self, num: int, tag: str) -> "list of strs":

        """
        Obtains "num" instances from the saved xml file by searching for the instance tag
        Returns a list of "num" instances
        """

        start_tag = "<" + tag + ">"
        end_tag = "</" + tag + ">"

        file = self.open_file()
        instances = []
        num_instances = 0
        line = file.read()

        while num_instances < num:

            if start_tag in line:
                
                instance = line[line.find(start_tag) + len(start_tag) : line.find(end_tag)]
                line = line[line.find(end_tag) + len(end_tag) : ]
                instances.append(instance)
                num_instances += 1
            
            else:

                break
        
        if len(instances) == 0:

            instances.append("")

        self.close_file(file)
        return instances
   

    def get_instances_from_items(self, items: "list of str", tag: str) -> "list of str":

        start_tag = "<" + tag + ">"
        does_not_exist_tag = "<" + tag + "/>"
        end_tag = "</" + tag + ">"

        instances = []

        for item in items:

            if does_not_exist_tag in item:

                instances.append("")

            elif start_tag in item:

                instance = item[item.find(start_tag) + len(start_tag) : item.find(end_tag)]
                instances.append(instance)
            
            else:

                instances.append("")

        if len(instances) == 0:

            instances.append("")
                            
        return instances


    def get_articles(self, num: int) -> "list of articles":

        """
        Obtains "num" articles from the saved xml file using get_titles(), get_links() and get_description()
        Returns a list of "num" articles
        """

        items = self.get_instances(num, "item")
        titles = self.get_instances_from_items(items, "title")
        descs = self.get_instances_from_items(items, "description")
        links = self.get_instances_from_items(items, "link")

        for _ in range(len(descs)):
            
            if descs[_].find("/a&gt;") != -1:

                descs[_] = descs[_][descs[_].find("/a&gt;") + 6 : ]

            if descs[_].find("&lt;img") != -1:

                descs[_] = descs[_][ : descs[_].find("&lt;img") ]
            
            if descs[_].startswith("rn") and descs[_].endswith("rn"):
               
                descs[_] = descs[_][3 : -2]

        articles = []
        for _ in range(len(items)):

            articles.append(Article(titles[_], descs[_], links[_]))
        
        return articles
    

    def update_articles(self):

        """
        Checks for any new articles by comparing the list returned by get_titles() and the titles in the saved list of articles and
        determines how many new articles are present
        Calls get_articles() using the number of new articles and updates the saved list of articles
        """

        self.get_xml_file()
        new_titles = self.get_instances(12, "title")
        new_articles_num = 0

        if(len(new_titles) > len(self.articles)):

            self.articles = self.get_articles(len(new_titles))
            return

        for _ in range(2, len(new_titles)):

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
            
        file = self.open_file()
        #self.feature_vector = update_feature_vector(file.read())
        self.close_file(file)

    
    def get_description(self) -> str:

        return self.get_instances(1, "description")


    def get_title(self) -> str:

        return self.get_instances(1, "title")
