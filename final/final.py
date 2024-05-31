from abc import ABC, abstractmethod


class Final(ABC):
    @classmethod
    @abstractmethod
    def get_final(self,game_data:str):
        pass


    @classmethod
    @abstractmethod
    def get_character_final(self,game_data:str,character_id:int):
        pass
