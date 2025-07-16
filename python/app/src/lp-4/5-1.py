import sys
import ctypes
from typing import List, Any

def get_list_allocated(lst: List[Any]) -> int:
    """Return the actual capacity of a Python list (CPython-specific)."""
    class PyListObject(ctypes.Structure):
        _fields_ = [
                ("ob_refcnt", ctypes.c_ssize_t),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_ssize_t),
                ("ob_items", ctypes.c_void_p),
                ("allocated", ctypes.c_ssize_t),
                ]

    ptr = ctypes.cast(id(lst), ctypes.POINTER(PyListObject))
    return int(ptr.contents.allocated)

data: List[None] = []
n = 100

print(f"{'':3}Size of None is {sys.getsizeof(None)}")

for k in range(n):
    length = len(data)
    capacity = get_list_allocated(data)
    size_in_bytes = sys.getsizeof(data)
    print(f"{k+1:3}: Length={length:3} | Allocated={capacity:3} | Size={size_in_bytes:4} bytes")
    data.append(None)
