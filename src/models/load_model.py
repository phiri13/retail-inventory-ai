import json
import pickle
from pathlib import Path


class ModelNotFoundError(Exception):
    pass


class InvalidModelMetadataError(Exception):
    pass


def load_model(store_id: str, product_id: str):
    base_path = Path("src/models/registry")
    model_path = base_path / f"store={store_id}" / f"product={product_id}"

    model_file = model_path / "model.pkl"
    metadata_file = model_path / "metadata.json"

    if not model_file.exists():
        raise ModelNotFoundError("Model file not found")

    if not metadata_file.exists():
        raise InvalidModelMetadataError("Metadata file not found")

    with open(metadata_file) as f:
        metadata = json.load(f)

    with open(model_file, "rb") as f:
        model = pickle.load(f)

    return model, metadata

