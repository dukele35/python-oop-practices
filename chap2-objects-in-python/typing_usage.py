from typing import List, Dict, Set, Optional, Any, Sequence, Callable, TypeVar, Union

####################
# 1 - List
####################
x1: List[int] = [1, 2, 3]  # valid
x2: List[int, str] = [1, 2, 3, "a"]  # invalid --> only expecting one argument
x3: List[Union[int, str]] = [1, 2, 3, "a"]  # valid
x4: List[List[int]] = [[1, 2, 3], [3, 4], [9]]  # valid


####################
# 2 - Dict
####################
y1: Dict[str, str] = {"a": "b"}  # valid
y2: Dict[str, str, int] = {"a": "b"}  # invalid --> only expecting two arguments
y3: Dict[str, int] = {"a": 3}  # valid
y4: Dict[int, str] = {"a": 3}  # invalid --> incompatible types


###################
# 3 - Set
###################
z1: Set[str] = {"a", "b"}  # valid
z2: Set[str, int] = {"a", 3}  # invalid --> only expecting one argument
z3: Set[Union[str, int]] = {"a", 3}  # valid


######################################################
# 4 - Custom type by defining a new datatype
######################################################
# NB. this is very useful for
# defining complicated datatype scenario
Vector = List[float]  # valid


def func1(v: Vector) -> Vector:  # valid
    return [i / 4 for i in v]


print(func1([1, 2, 3]))  # valid


########################
# 5 - Optional
########################
def func2(xyz: Optional[bool] = False) -> int:  # valid
    return 3


print(func2(False))  # valid
print(func2())  # valid
print(func2("abc"))  # invalid --> parameter should be Boolean or None


###################
# 6 - Any
###################
def func3(abc: Any) -> str:  # valid
    return "this accepts any types"


print(func3(False))  # valid
print(func3(456))  # valid
print(func3("love this"))  # valid


########################
# 7 - Sequence
########################
def func4(seq: Sequence[str]) -> None:  # valid
    pass


func4(["a", "b", "c"])  # valid
func4(("a", "b", "c"))  # valid
func4("a, b, c")  # valid
func4({"a", "b", "c"})  # invalid -> the input can't be indexed


########################
# 8 - Callable
########################
def add(x: int, y: int) -> int:  # valid
    return x + y


def func5(inp: Callable[[int, int], int]) -> int:  # valid
    return inp(3, 5)


print(func5(add))


#######################
# 9 - TypeVar
#######################
T = TypeVar("T")  # Declare type variable       # valid


def first(la: Sequence[T]) -> T:  # valid
    # l: Sequence[T] means that
    # the sequence must have the same type
    # T in this case is like a placeholder
    return la[0]


print(first([1, 2, 3]))
