import joblib
import os

MODEL_DIR = "models/prophet"

_models = {}

def load_models():
    for file in os.listdir(MODEL_DIR):
        if file.endswith(".pkl"):
            key = file.replace(".pkl", "")
            _models[key] = joblib.load(os.path.join(MODEL_DIR, file))

    return _models
