from abc import ABCMeta, abstractmethod


class PasswordGeneratorInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasscheck__(self, subclass):
        return (
                hasattr(subclass, 'generate_password') and
                callable(subclass.generate_password)
        )

    @abstractmethod
    def generate_password(self) -> str:
        """
        Generates a password string
        """
        pass

