from abc import ABCMeta, abstractmethod


class AbstractDataset(metaclass=ABCMeta):

    @classmethod
    def datalake_path(cls):
        return 'https://github.com/recohut/recodata'

    @classmethod
    @abstractmethod
    def code(cls):
        pass

    @classmethod
    @abstractmethod
    def all_raw_file_names(cls):
        pass

    @abstractmethod
    def ingest():
        pass