from abc import ABCMeta, abstractmethod
import os.path as osp
import dvc.api


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

    @classmethod
    def ingest(cls, path, only=None):
        ingest_file_list = only if only else cls.all_raw_file_names()
        for filename in ingest_file_list:
            save_path = osp.join(path, filename)
            if not osp.exists(save_path):
                lake_path = osp.join(cls.code().replace('-',''), filename)
                lake_root = cls.datalake_path()
                print(save_path, lake_path, lake_root)
                local_handle = open(save_path, "wb")
                with dvc.api.open(
                    path=lake_path,
                    repo=lake_root,
                    mode='rb') as remote_handle:
                    local_handle.write(remote_handle.read())
                remote_handle.close()
                local_handle.close()