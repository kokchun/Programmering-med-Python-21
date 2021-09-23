from plotter import PlotVectors

class Vector: 
    """ A class to represent a Euclidean vector with magnitude and direction"""

    def __init__(self, *numbers: float) -> None:
        #print(numbers)
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} must be a float or int not {type(number)}")

        if len(numbers) <= 0:
            raise ValueError("Vectors can't be empty")

        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self) -> tuple:
        """Read only property that returns the numbers"""
        return self._numbers

    # (2,3) + (1,1,1) not okay
    # (2,3) + (1,1) = (3,4)
    def __add__(self, other: "Vector") -> "Vector": # overloads the + operator
        """Adds two vectors of same dimensions using + operator"""
        if self.validate_vectors(other):
            numbers = (a+b for a,b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __sub__(self, other: "Vector") -> "Vector":
        """Adds two vectors of same dimensions using + operator"""
        if self.validate_vectors(other):
            numbers = (a-b for a,b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __mul__(self, value: float) -> "Vector":
        print("__mul__ called ...")
        if not isinstance(value, (float, int)):
            raise TypeError(f"Value must be float or int not {type(value)}")
        
        numbers = (value*a for a in self.numbers)
        return Vector(*numbers)

    def __rmul__(self, value: float) -> "Vector":
        print("__rmul__ called")
        return self*value

    # len() function
    def __len__(self) -> int:
        """Returns number of components in a Vector not the Euclidean length"""
        return len(self.numbers)

    def validate_vectors(self, other: "Vector") -> bool:
        """ Validate that two vectors have same dimensions """
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("Both must be Vector and same length")
        return len(self) == len(other)

    def __repr__(self) -> str:
        return f"Vector{self.numbers}"
    
    def __str__(self) -> str:
        return f"{self.numbers}"

    # [] operator
    def __getitem__(self, item: int) -> float:
        return self.numbers[item]

    def __eq__(self, other) -> bool:
        if not self.validate_vectors(other):
            return False
        
        for num1, num2 in zip(self.numbers, other.numbers):
            if num1 != num2:
                return False
        
        return True

    def plot(self, *others: "Vector") -> None:
        # TODO: error checking

        # composition -> Vector has a PlotVectors object
        plot_vector = PlotVectors(self, *others)
        
        plot_vector.plot()



# v1 = (1,1), v2=(1,1,14,5,252,56,2,7)
