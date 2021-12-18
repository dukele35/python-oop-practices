import math

class Point:
    """
    A class used to represent a point
    ...
    Attributes
    ----------
    x (float): a float x-coordinate 
    y (float): a float y-coordinate 

    Methods
    ----------
    move(x,y): 
        Move a point to a given coordinates of x & y
    reset(): 
        Reset a point's coordinates to x = 0 & y = 0.
    calculate_distance(Point(x,y)): 
        Calculate Euclidean distance between the current point with
        another point as a parameter.

    Examples
    ---------
    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    """

    def __init__(self,x:float=0,y:float=0) -> None:
        """
        Assign x coordinate and y coordinate for one sinple point.
        Parameters:
            x (float): a float x-coordinate 
            y (float): a float y-coordinate
        """
        self.move(x,y)

    def move(self,x:float,y:float) -> None:
        """
        Move a point to a given coordinates of x & y.
        Parameters:
            x (float): a float x-coordinate 
            y (float): a float y-coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset a point's coordinates to x = 0 & y = 0.
        """
        self.move(0,0)

    def calculate_distance(self, other: "Point") -> float:
        """
        Calculate Euclidean distance between the current point with
        another point as a parameter. 
        Parameters:
            other: a Point instance
        Returns:
            an Euclidean distance (float)
        """
        return math.hypot(self.x - other.x, self.y - other.y)

def main() -> None:
    """
    >>> main()
    5.0
    """
    point1 = Point()
    point2 = Point(3,4)
    print(f"{point1.calculate_distance(point2)}")

if __name__ == "__main__":
    main()