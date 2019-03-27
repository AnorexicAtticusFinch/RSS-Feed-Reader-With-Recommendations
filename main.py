from class_definitions import *
from recommendations import *

sl = Predefined_Sources()
#gs = Feed_Source("test", "http://feeds.feedburner.com/ndtvsports-cricket")
gs = Feed_Source("test", "http://feeds.feedburner.com/ndtvnews-top-stories")

for source in sl.list_of_sources:
    print(source.feature_vector)

print(gs.feature_vector)

lst = sl.find_best_fits(gs)

for source in lst:
    print(source.link)
