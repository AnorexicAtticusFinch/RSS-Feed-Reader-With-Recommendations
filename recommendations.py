from class_definitions import *

def dist_between_vectors(vec1 : "list of floats", vec2 : "list of floats") -> float:

    dist_vec = []
    for i in range(len(vec1)):

        dist_vec.append((vec1[i] - vec2[i]) ** 2)
    
    return sum(dist_vec)



class Predefined_Sources:

    def __init__(self):

        self.list_of_sources = []
        file = open("list_of_sources", "r")
        for source in file:
            
            self.list_of_sources.append(Feed_Source(source, source))
        file.close()

    def find_best_fits(self, given_source : Feed_Source) -> "list of Feed_Sources":

        least_distance = None
        sources = []

        for source in self.list_of_sources:

            current_distance = dist_between_vectors(given_source.feature_vector, source.feature_vector)

            if least_distance is None:

                least_distance = current_distance
                sources.append(source)

            elif current_distance < least_distance:
                
                least_distance = current_distance
                sources = []
                sources.append(source)
            
            elif current_distance == least_distance:

                sources.append(source)
        
        return sources