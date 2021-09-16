from .base import AbstractDataset

import os.path as osp
import dvc.api


class ML1MDataset(AbstractDataset):
    
    @classmethod
    def code(cls):
        return 'ml-1m'

    @classmethod
    def all_raw_file_names(cls):
        return ['movies.parquet.snappy',
                'ratings.parquet.snappy',
                'users.parquet.snappy']

    @classmethod
    def __repr__(cls):
        return """
        This dataset contains 1,000,209 anonymous ratings of approximately
        3,900 movies made by 6,040 MovieLens users who joined MovieLens in 2000.
        It contains the following raw dataset files: {}
        """.format(cls.all_raw_file_names())