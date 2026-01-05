import json
import pickle
from pathlib import Path


class ModelNotFoundError(Exception):
    pass


class InvalidModelMetadataError(Exception):
    pass


BASE_REGISTRY = Path("src/models/registry")


def load_model(store_id: str, product_id: str):
    model_dir = BASE_REGISTRY / f"store={store_id}" / f"product={product_id}"

    if not model_dir.exists():
        raise ModelNotFoundError(f"Model directory not found: {model_dir}")

    model_path = model_dir / "model.pkl"
    metadata_path = model_dir / "metadata.json"

    if not model_path.exists():
        raise ModelNotFoundError("model.pkl missing")

    if not metadata_path.exists():
        raise InvalidModelMetadataError("metadata.json missing")

    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    required_keys = {"model_name", "version", "framework", "horizon_days"}
    if not required_keys.issubset(metadata):
        raise InvalidModelMetadataError(
            f"Missing metadata fields: {required_keys - set(metadata.keys())}"
        )

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model, metadata

