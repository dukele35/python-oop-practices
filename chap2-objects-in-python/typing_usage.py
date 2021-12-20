from typing import  List, Dict, Set, \
                    Optional, Any, Sequence, \
                    Tuple, Callable, TypeVar, Union

####################
##### 1 - List #####
####################
x1 : List[int]              = [1,2,3]               # valid
x2 : List[int,str]          = [1,2,3,"a"]           # invalid --> only expecting one argument
x3 : List[Union[int,str]]   = [1,2,3,"a"]           # valid
x4 : List[List[int]]        = [[1,2,3],[3,4],[9]]   # valid


####################
##### 2 - Dict #####
####################
y1 : Dict[str,str]          = {"a":"b"}             # valid
y2 : Dict[str,str,int]      = {"a":"b"}             # invalid --> only expecting two arguments
y3 : Dict[str,int]          = {"a":3}               # valid
y4 : Dict[int,str]          = {"a":3}               # invalid --> incompatible types



###################
##### 3 - Set #####
###################
z1 : Set[str]               = {"a","b"}             # valid
z2 : Set[str,int]           = {"a",3}               # invalid --> only expecting one argument
z3 : Set[Union[str,int]]    = {"a",3}               # valid


######################################################
##### 4 - Custom type by defining a new datatype #####
######################################################
# NB. this is very useful for 
# defining complicated datatype scenario
Vector = List[float]                                # valid

def f1(v:Vector) -> Vector:                         # valid
    return [i/4 for i in v]

print (f1([1,2,3]))                                 # valid


########################
##### 5 - Optional #####
########################
def f2(xyz: Optional[bool] = False) -> int:         # valid          
    return 3

print (f2(False))                                   # valid
print (f2())                                        # valid


###################
##### 6 - Any #####
###################
def f3(abc: Any) -> str:                            # valid          
    return "this accepts any types"

print (f3(False))                                   # valid
print (f3(456))                                     # valid
print (f3("love this"))                             # valid

# 6 - Sequence

# 7 - Tuple

# 8 - Callable

# 9 - TypeVar