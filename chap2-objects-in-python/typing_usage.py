from typing import Dict

class User:
    def __init__(self, name):
        self.name = name

users: Dict[int, User] = {
    1: User("Serdar"),
    2: User("Davis")
}

def inspect_user(user:User) -> None:
    print (user.name)

user1 = users[1]
inspect_user(user1)