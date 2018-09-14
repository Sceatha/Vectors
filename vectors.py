class Vector:

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.dim = len(coordinates) + 1


    def __add__(self, other):
        vector_set = self.same_dim([self, other])
        vector = []
        vector_1 = vector_set[0]
        vector_2 = vector_set[1]
        for i in range(vector_1.dim - 1):
            vector.append(vector_1.coordinates[i] + vector_2.coordinates[i])
        return vector

    def same_dim(self, vector_set):
        if vector_set[0].dim == vector_set[1].dim:
            return vector_set
        else:
            while vector_set[0].dim > vector_set[1].dim:
                vector_set[1].coordinates.append(0)
            while vector_set[1].dim > vector_set[0].dim:
                vector_set[0].coordinates.append(0)
            return vector_set


# Test code:

a = Vector