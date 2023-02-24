import math

class Point:
    dimension : int # dimension
    coordinates : list # list of coordinates in each dimension. coordinates[0] -> dimension 0 (e.g x)
    """
    Construct an object in Point class

    Args:
        dimension : the dimension of the point

    """
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.coordinates = []

    def get_coordinates(self):
        """
        Inputs coordinates
        """
        for i in range (self.dimension):
            temp = int(input("Enter the coordinate on the point in dimension "+str(i)+ ": "))
            self.coordinates.append(temp)
    
    def distance(self, other):
        """
        Find the distance between two points

        Args:
            other: the other point

        """
        if self.dimension != other.dimension:
            raise ValueError("Points are not of the same dimension")

        # Calculate the sum of squared differences in each dimension
        return math.sqrt(sum([(self.coordinates[i] - other.coordinates[i])**2 for i in range(self.dimension)]))
    
    def print(self):
        """
        Prints coordinates of the point
        """
        print("(",end="")
        for i in range (self.dimension):
            print(self.coordinates[i],end="")
            if (i!= self.dimension - 1):
                print(", ",end="")
        print(")",end="")