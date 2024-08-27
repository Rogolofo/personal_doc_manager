from pydantic import BaseModel


class Person(BaseModel):
    """
    Represents a person with a name.

    Attributes:
        name (str): The name of the person.
    """

    name: str
