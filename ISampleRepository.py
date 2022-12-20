import abc
from typing import Union, Dict


class ISampleRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, document_name: str, key: str) -> Union[Dict, None]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, update_field: dict):
        raise NotImplementedError()

    @abc.abstractmethod
    def insert(self, document_name: str, key: str, insert_field: dict):
        raise NotImplementedError()
