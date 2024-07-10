class Location:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def equals(self, other_location):
        if isinstance(other_location, Location):
            return self.__x == other_location.get_x() and self.__y == other_location.get_y()
        return False

    def __str__(self):
        return f"Location(x={self.__x}, y={self.__y})"