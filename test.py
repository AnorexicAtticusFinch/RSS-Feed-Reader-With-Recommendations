from class_definitions import *
from recommendations import *

sl = Predefined_Sources()
#gs = Feed_Source("test", "http://feeds.feedburner.com/ndtvsports-cricket")
gs = Feed_Source("test", "http://feeds.feedburner.com/ndtvnews-top-stories")

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
    for article in source.articles:
        print(article.title)
    print()
    print()
    print()
