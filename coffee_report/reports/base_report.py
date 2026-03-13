from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def generate(self, records):
        raise NotImplementedError