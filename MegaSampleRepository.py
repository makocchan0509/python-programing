from typing import Union, Dict
import ISampleRepository


class MegaSampleRepository(ISampleRepository.ISampleRepository):
    def __init__(self):
        print('init mega sample repo')

    def get(self, document_name: str, key: str) -> Union[Dict, None]:
        print('get document at MegaSampleRepository')
        return {'result': 'mega'}

    def update(self, update_field: dict):
        print('update document at MegaSampleRepository')

    def insert(self, document_name: str, key: str, insert_field: dict):
        print('insert document at MegaSampleRepository')
