# Chapter 3: Inheritance # 

## 1. 

## 2. 

## OTHER NOTICES
### __repr__ method
#### without `__repr__`
code
```
class Contact:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
```
script
```
>>> c1 = Contact("duke", "duke@email.com")
>>> print(c1)
<__main__.Contact object at 0x7f8ee95a2990>
```

#### with `__repr__`
code
```
class Contact:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.email})"
```
script
```
>>> c1 = Contact("duke", "duke@email.com")
>>> print(c1)
Contact("duke", "duke@email.com")
```