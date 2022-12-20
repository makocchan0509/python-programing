import injector
import ISampleRepository
from typing import Union, Dict

from MegaSampleRepository import MegaSampleRepository
from ProtoSampleRepository import ProtoSampleRepository


class AbstractSampleRepository:
    @injector.inject
    def __init__(self, repository: ISampleRepository.ISampleRepository):
        self.repository = repository
        print('init sample repo')

    def get(self, document_name: str, key: str) -> Union[Dict, None]:
        return self.repository.get(document_name, key)

    def update(self, update_field: dict):
        self.repository.update(update_field)

    def insert(self, document_name: str, key: str, insert_field: dict):
        self.repository.insert(document_name, key, insert_field)


class DependencyInjector:
    def __init__(self):
        self.injector = injector.Injector(self.__class__.configure)

    @classmethod
    def configure(self, binder):
        binder.bind(ISampleRepository.ISampleRepository,
                    to=MegaSampleRepository)

    def resolve(self, klass):
        return self.injector.get(klass)
