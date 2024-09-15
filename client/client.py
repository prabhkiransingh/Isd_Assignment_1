"""
Description: {Classes, Encapsulation and Unit Test Planning}
Author: {Prabhkiran Singh}
"""
from email_validator import validate_email, EmailNotValidError


class Client:
    """
    Represents a client with their details.

    Attributes:
        client_number (int): The client's unique identification number.
        first_name (str): The client's first name.
        last_name (str): The client's last name.
        email_address (str): The client's email address.

    Methods:
        __init__(client_number, first_name, last_name, email_address): Initializes a new Client object.
        client_number(): Returns the client's number.
        first_name(): Returns the client's first name.
        last_name(): Returns the client's last name.
        email_address(): Returns the client's email address.
        __str__(): Returns a string representation of the Client object.
    """
    def __init__(self, client_number: int, first_name, last_name, email_address):
        """
        Initializes a new Client object.

        Args:
            client_number (int): The client's unique identification number.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.
        """
        if not isinstance(client_number, int):
            raise ValueError("client_number must be an integer")
        self.__client_number = client_number

        
        if len (first_name.strip()) == 0:
            raise ValueError("first_name cannot be blank")
        else:
            self.__first_name = first_name

        
        if len (last_name.strip()) == 0:
            raise ValueError("last_name cannot be blank")
        else:
            self.__last_name = last_name

        try:
            valid_email = validate_email(email_address).email
            self.__email_address = valid_email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Returns the client's number.

        Returns:
            int: The client's number.
        """
        return self.__client_number

    @property
    def first_name(self):
        """
        Returns the client's first name.

        Returns:
            str: The client's first name.
        """
        return self.__first_name

    @property
    def last_name(self):
        """
        Returns the client's last name.

        Returns:
            str: The client's last name.
        """
        return self.__last_name

    @property
    def email_address(self):
        """
        Returns the client's email address.

        Returns:
            str: The client's email address.
        """
        return self.__email_address 
    
    def __str__(self):
        """
        Returns a string representation of the Client object.

        Returns:
            str: A string representation of the Client object.
        """
        return f"client_number: {self.__client_number}\nfirst_name: {self.__first_name}\nlast_name: {self.__last_name}\nemail_address: {self.__email_address}"