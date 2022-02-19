from typing import List


class Contact:
    """
    >>> c1 = Contact("duke", "duke@email.com")
    >>> c2 = Contact("mike", "mike@email.com")
    >>> print(Contact.all_contacts)
    [Contact(duke, duke@email.com), Contact(mike, mike@email.com)]
    """

    all_contacts: List["Contact"] = []  # global list

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.email})"


class Supplier(Contact):
    """
    Supplier class inherits all of attributes and methods from Contact class.
    Thus, initiating a new object under Supplier class is similar to Contact class.
    >>> s1 = Supplier("sup1", "sup1@email.com")
    >>> s2 = Supplier("sup2", "sup2@email.com")
    >>> print (Supplier.all_contacts)
    [Contact(duke, duke@email.com), Contact(mike, mike@email.com), Supplier(sup1, sup1@email.com), Supplier(sup2, sup2@email.com)]
    """

    def order(self, order: "Order") -> None:
        print("If this were a real system we would send " f"'{order}' order to '{self.name}'")
