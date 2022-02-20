from basis import Contact


class Friend(Contact):
    """
    >>> f1 = Friend("duke", "duke@email.com", "12345")
    >>> Friend.all_contacts
    [Friend(duke, duke@email.com)]

    >>> Contact.all_contacts
    [Friend(duke, duke@email.com)]
    """

    def __init__(self, name: str, email: str, phone: str) -> None:
        # super() allows the object as it was actually an instance
        # of the parent class Contact
        super().__init__(name, email)
        self.phone = phone
