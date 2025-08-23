import abc

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def all_exercises(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def match_exercise(self, entry: dict) -> list:
        raise NotImplementedError