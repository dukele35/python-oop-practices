from basis import Contact
from typing import Protocol


class Emailable(Protocol):
    """
    Protocol enforces children of Emailable has to have email attribute
    Emailable containing Protocol could not be initiated
    Example
    -------
    >>> sample_1 = Emailable("something")
    Traceback (most recent call last):
        ...
    TypeError: Protocols cannot be instantiated
    """

    email: str


class MailSender(Emailable):
    """
    MailSender is the children class of Emailable.
    However, Mailsender does not have email attribute.
    Therefore, it will raise error if MailSender's method, send_email, is used alone.
    Example
    -------
    >>> sample_2 = MailSender("something")
    >>> sample_2.send_email(message = "go to school")
    Traceback (most recent call last):
        ...
    AttributeError: 'MailSender' object has no attribute 'email'
    """

    def send_email(self, message: str) -> None:
        print(f"sending email to {self.email}")


class EmailableContact(Contact, MailSender):
    """
    EmailableContact is an example of multiple inheritance.
    EmailableContact is the children of both Contact and MailSender such that
    EmailableContact has all attributes and methods from its parents.
    Example
    -------
    >>> sample_3 = EmailableContact(name="Diana", email="diana@email.com")
    >>> Contact.all_contacts
    [EmailableContact(Diana, diana@email.com)]
    >>> sample_3.send_email(message="Hello world")
    sending email to diana@email.com

    NB
    ------
    This example shows that EmailableContact has email attribute from Contact
    but it satisfies the condition from MailSender requiring email attribute
    in the children class
    """

    pass
