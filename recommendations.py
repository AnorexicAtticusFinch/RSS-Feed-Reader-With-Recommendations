from class_definitions import *

def dist_between_vectors(vec1 : "list of floats", vec2 : "list of floats") -> float:

    dist_vec = []
    for i in range(len(vec1)):

        dist_vec.append((vec1[i] - vec2[i]) ** 2)
    
    return sum(dist_vec)



class Predefined_Sources:

    def __init__(self):

        self.list_of_sources = []
        file = open("list_of_sources.txt", "r")
        count = 1
        for source in file:

            if source[-1] == "\n":

                source = source[ : -1]
            
            self.list_of_sources.append(Feed_Source(str(count), source))
            count += 1

        file.close()

    def find_best_fits(self, given_source : Feed_Source) -> "list of Feed_Sources":

        if given_source in self.list_of_sources:

            self.list_of_sources.remove(given_source)

        min_distance_0 = None
        min_distance_1 = None

        sources = [None, None]

        for source in self.list_of_sources:

            current_distance = dist_between_vectors(given_source.feature_vector, source.feature_vector)

            if min_distance_0 is None and min_distance_1 is None:

                min_distance_0 = current_distance
                sources[0] = source
            
            elif (min_distance_1 is None or current_distance < min_distance_1) and not current_distance < min_distance_0 :

                min_distance_1 = current_distance
                sources[1] = source

            elif current_distance < min_distance_0:

                min_distance_1 = min_distance_0
                min_distance_0 = current_distance
                sources[1] = sources[0]
                sources[0] = source
   
        return sources
