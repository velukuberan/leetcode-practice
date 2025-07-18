from typing import Any, Optional

"""A dynamic array class akin to a simplified Python list"""
class DynamicArray:

    def __init__(self) -> None:
        """Create empty array"""
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2
    
    """Insert n in the last position of the array"""
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    """Resize the capacity into double the previous length"""
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        """Copy old elements to new array"""
        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    """Remove last element in the array"""
    def pop(self) -> None:
        if self.length > 0:
            self.length -= 1

    """Get value at the index """
    def get(self, index: int) -> Optional[Any]:
        if index < self.length:
            return self.arr[index]
    
        return None

    """Insert a value at the index i"""
    def insert(self, index: int, value: int) -> None:
        if index < self.length:
            self.arr[index] = value
            return

    """Print the values"""
    def print(self) -> None:
        for i in range(self.length):
            print(self.arr[i])
        print()

