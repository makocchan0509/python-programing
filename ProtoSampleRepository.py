from typing import Union, Dict
import ISampleRepository


class ProtoSampleRepository(ISampleRepository.ISampleRepository):
    def __init__(self):
        print('init proto sample repo')

    def get(self, document_name: str, key: str) -> Union[Dict, None]:
        print('get document at ProtoSampleRepository')
        return {'result': 'proto'}

    def update(self, update_field: dict):
        print('update document at ProtoSampleRepository')

    def insert(self, document_name: str, key: str, insert_field: dict):
        print('insert document at ProtoSampleRepository')
