class Vector:

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.dim = len(coordinates)

    def __str__(self):
        return str(self.coordinates)

    def __add__(self, other):
        vector_set = self.same_dim(other)
        vector = []
        vector_1 = vector_set[0]
        vector_2 = vector_set[1]
        for i in range(len(vector_1)):
            vector.append(vector_1[i] + vector_2[i])
        result = Vector(vector)
        return result

    def scale(self, number):
        vector = [coordinate * number for coordinate in self.coordinates]
        return Vector(vector)


    def __mul__(self, other):
        vector_set = self.same_dim(other)
        product = 0
        vector_1 = vector_set[0]
        vector_2 = vector_set[1]
        for i in range(len(vector_1)):
            product += vector_1[i] * vector_2[i]
        return product




    # Helper methods:

    def same_dim(self, other):
        vectors = [self.coordinates, other.coordinates]
        if len(vectors[0]) == len(vectors[1]):
            return vectors
        else:
            if len(vectors[0]) != len(vectors[1]):
                while len(vectors[0]) > len(vectors[1]):
                    vectors[1].append(0)
                while len(vectors[1]) > len(vectors[0]):
                    vectors[0].append(0)
            return vectors




# Test code:

