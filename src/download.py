from numerapi import NumerAPI

NAPI = NumerAPI()

def download_all():
    # NAPI.download_dataset("v4/train.parquet", "../data/train.parquet")
    NAPI.download_dataset("v4/validation.parquet", "../data/validation.parquet")
    NAPI.download_dataset("v4/live.parquet", "../data/live.parquet")
    NAPI.download_dataset("v4/live_example_preds.parquet", "../data/live_example_preds.parquet")
    NAPI.download_dataset("v4/validation_example_preds.parquet", "../data/validation_example_preds.parquet")
    NAPI.download_dataset("v4/features.json", "../data/features.json")