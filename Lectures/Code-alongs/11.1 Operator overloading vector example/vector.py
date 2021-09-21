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
        return self._numbers

    # (2,3) + (1,1,1) not okay
    # (2,3) + (1,1) = (3,4)
    def __add__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a+b for a,b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    # len() function
    def __len__(self) -> int:
        """Returns number of components in a Vector not the Euclidean length"""
        return len(self.numbers)

    def validate_vectors(self, other: "Vector") -> bool:
        """ validate that two vectors have same dimensions """
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


# v1 = (1,1), v2=(1,1,14,5,252,56,2,7)
