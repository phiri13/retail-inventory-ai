from pathlib import Path
import joblib

MODEL_DIR = Path("models/prophet")

def load_model(store_id: str, product_id: str):
    model_path = MODEL_DIR / f"{store_id}_{product_id}.pkl"

    if not model_path.exists():
        return None

    return joblib.load(model_path)

