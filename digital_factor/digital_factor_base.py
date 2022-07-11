from abc import ABC, abstractclassmethod


class DigitalFactor:
    """
    base class for Digital factors
    """
    
    required_class_info = {}
    
    @abstractclassmethod
    def fill_info(self, info: dict) -> None:
        """
        fill the info dictionary with the necessary information
        """
        pass
    
    @abstractclassmethod
    def get_info(self) -> dict:
        """
        return the info dictionary
        """
        return self.info