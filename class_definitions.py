class article:

    def __init__(self):
        #title
        #description
        #link
        pass

    def __eq__(self, article_2):
        pass
    
    def __str__(self):
        pass

    def open_link(self):
        #using selenium
        pass
        
class feed_source:

    def __init__(self):
        #rss link
        #list of articles - 10 - list
        #category
        #xml code obtained - boolean
        #xml code saved path
        pass

    def __eq__(self, source_2):
        pass

    def __str__(self):
        pass
    
    def update_xml_code(self):
        pass
    
    def get_titles(self, num, file):
        pass

    def get_links(self, num, file):
        pass

    def get_descriptions(self, num, file):
        pass
    
    def get_articles(self, file):
        pass
    
    def update_articles(self):
        pass
