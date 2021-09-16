from .ml_100k import ML100KDataset
# from .ml_1m import ML1MDataset


DATASETS = {
    ML100KDataset.code(): ML100KDataset,
    # ML1MDataset.code(): ML1MDataset,
}


class IngestionFactory:
    """
    This is a wrapper class to assist in data ingestion process
    """
    @classmethod
    def available_datasets(cls):
        return list(DATASETS.keys())

    @classmethod
    def info(cls, dataset_code):
        return DATASETS[dataset_code].__repr__()

    @classmethod
    def ingest(cls, dataset_code, path):
        DATASETS[dataset_code].ingest(path)