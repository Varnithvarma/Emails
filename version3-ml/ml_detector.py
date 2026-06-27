import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "phishing_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")


def ml_model_exists():
    return os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH)


def get_ml_verdict(phishing_confidence):
    if phishing_confidence >= 70:
        return "Likely Phishing"
    elif phishing_confidence >= 50:
        return "Suspicious"
    else:
        return "Likely Safe"


def predict_email_ml(email_text):
    if not ml_model_exists():
        return {
            "available": False,
            "verdict": "ML model not trained",
            "phishing_confidence": 0
        }

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    email_vector = vectorizer.transform([email_text])
    probabilities = model.predict_proba(email_vector)[0]
    classes = model.classes_

    phishing_confidence = 0

    for class_name, probability in zip(classes, probabilities):
        if class_name == "phishing":
            phishing_confidence = round(probability * 100, 2)

    verdict = get_ml_verdict(phishing_confidence)

    return {
        "available": True,
        "verdict": verdict,
        "phishing_confidence": phishing_confidence
    }