from flask import Flask, render_template, request
from detector import analyze_email
from ml_detector import predict_email_ml

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    email_text = request.form.get("email_text", "")

    if not email_text.strip():
        return render_template(
            "index.html",
            error="Please paste an email before analyzing."
        )

    rule_result = analyze_email(email_text)
    ml_result = predict_email_ml(email_text)

    return render_template(
        "result.html",
        email_text=email_text,
        result=rule_result,
        ml_result=ml_result
    )


if __name__ == "__main__":
    app.run(debug=True)