from typing import List

class Contact:
    all_contacts: List["Contact"] = [] # global list
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
       
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.email})"

class Supplier(Contact):
   def order(self, order: "Order") -> None:
       print(
           "If this were a real system we would send "
           f"'{order}' order to '{self.name}'"
       )