from class_definitions import *
from recommendations import *

sl = Predefined_Sources()

#gs = Feed_Source("test", "http://feeds.feedburner.com/ndtvsports-cricket") #CRICKET NDTV
#gs = Feed_Source("test", "http://feeds.feedburner.com/ndtvnews-top-stories") #TOP STORIES NDTV
gs = Feed_Source("test", "https://timesofindia.indiatimes.com/rssfeeds/5880659.cms") #SCI&TECH TOI
#gs = Feed_Source("test", "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms") #ENT TOI
#gs = Feed_Source("test", "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms") #BUS TOI

for source in sl.list_of_sources:
    print(source.feature_vector)

print()
print()
print()

print(gs.feature_vector)

print()
print()
print()

lst = sl.find_best_fits(gs)

for article in gs.articles:
        print(article.title)
print()
print()
print()

for source in lst:
        print(source.link)
        for article in source.articles:
                print(article.title)
        print()
        print()
        print()