from .base import AbstractDataset

import os.path as osp
import dvc.api


class ML100KDataset(AbstractDataset):
    def __init__(self):
        pass
        
    @classmethod
    def code(cls):
        return 'ml-100k'

    @classmethod
    def all_raw_file_names(cls):
        return ['movies.parquet.snappy',
                'ratings.parquet.snappy',
                'users.parquet.snappy']

    def ingest(self, path, only=None):
        ingest_file_list = only if only else self.all_raw_file_names()
        for filename in ingest_file_list:
            save_path = osp.join(path, filename)
            if not osp.exists(save_path):
                lake_path = osp.join(self.code().replace('-',''), filename)
                lake_root = self.datalake_path()
                print(save_path, lake_path, lake_root)
                local_handle = open(save_path, "wb")
                with dvc.api.open(
                    path=lake_path,
                    repo=lake_root,
                    mode='rb') as remote_handle:
                    local_handle.write(remote_handle.read())
                local_handle.close()

    def __repr__(self):
        return """
        This dataset contains 1,000,209 anonymous ratings of approximately
        3,900 movies made by 6,040 MovieLens users who joined MovieLens in 2000.
        It contains the following raw dataset files: {}
        """.format(self.all_raw_file_names())