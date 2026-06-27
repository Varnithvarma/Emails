import os
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_PATH = os.path.join(MODEL_DIR, "phishing_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")


data = {
    "email": [
        "urgent your account has been suspended click here to verify your password",
        "verify your login immediately or your bank account will be locked",
        "congratulations you won a free prize click this link now",
        "security alert unusual activity detected reset your password now",
        "payment failed update your billing information immediately",
        "act now your account will be closed unless you confirm your details",
        "you have won a gift card click here to claim your reward",
        "your paypal account is limited verify your identity now",
        "bank notice confirm your account information urgently",
        "your package is held click here to pay a small fee",
        "final notice your account will be terminated unless you login now",
        "unusual login attempt detected validate your account immediately",
        "your password will expire click below to reset your account",
        "we detected suspicious activity confirm your identity now",
        "your payment method failed update your billing information",
        "claim your prize today by entering your credit card number",
        "limited time offer click here to redeem your free gift",
        "irs notice tax refund available verify your social security number",
        "wire transfer required immediately keep this request confidential",
        "your information has been compromised reset your password now",

        "hi alex are we still meeting tomorrow for the project discussion",
        "please review the attached notes from today's class",
        "thank you for volunteering at the event this weekend",
        "the team meeting has been moved to 3 pm on friday",
        "can you send me the homework when you get a chance",
        "your appointment is confirmed for next monday afternoon",
        "here is the agenda for our next club meeting",
        "thanks for your help with the presentation yesterday",
        "let me know if you are available to study after school",
        "the document has been shared with you for review",
        "good morning the schedule for tomorrow has been updated",
        "please bring your notebook to class tomorrow",
        "the library volunteer meeting starts at 4 pm today",
        "your project draft looks good and I added comments",
        "are you coming to track practice after school today",
        "the teacher posted the assignment in google classroom",
        "please check the calendar for the updated meeting time",
        "thanks for helping with the computer club project",
        "we will discuss the presentation during class tomorrow",
        "the notes from yesterday are attached for your review"
    ],
    "label": [
        "phishing", "phishing", "phishing", "phishing", "phishing",
        "phishing", "phishing", "phishing", "phishing", "phishing",
        "phishing", "phishing", "phishing", "phishing", "phishing",
        "phishing", "phishing", "phishing", "phishing", "phishing",

        "safe", "safe", "safe", "safe", "safe",
        "safe", "safe", "safe", "safe", "safe",
        "safe", "safe", "safe", "safe", "safe",
        "safe", "safe", "safe", "safe", "safe"
    ]
}


df = pd.DataFrame(data)

X = df["email"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model trained successfully.")
print(f"Accuracy: {accuracy * 100:.2f}%")
print()
print("Classification Report:")
print(classification_report(y_test, predictions))

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)

print()
print(f"Saved model to: {MODEL_PATH}")
print(f"Saved vectorizer to: {VECTORIZER_PATH}")