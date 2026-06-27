# PhishGuard — AI-Based Phishing Email Detection Tool

PhishGuard is a cybersecurity tool that analyzes email text and detects phishing indicators using both rule-based logic and a machine learning classifier. The tool checks for suspicious words, risky links, shortened URLs, and common scam patterns, then generates a risk score and verdict from two independent detection engines.

---

## Project Overview

Phishing emails are one of the most common ways attackers steal passwords, personal information, and financial data. PhishGuard helps users identify suspicious emails by analyzing the content and links inside the message.

The goal of this project is to combine cybersecurity, Python programming, machine learning, and web development into one practical tool.

---

## Current Version

**Version 3 — Machine Learning Classifier**

Version 3 adds a trained ML model alongside the existing rule-based engine. Both engines analyze every email independently and their results are displayed side by side on the results page.

---

## Features

- Detects suspicious phishing-related keywords
- Extracts links from email text
- Flags shortened URLs such as `bit.ly`, `tinyurl.com`, and `t.co`
- Detects IP-based links
- Flags unusually long domains
- Flags domains with suspicious formatting
- Calculates a phishing risk score (rule-based)
- Classifies emails using a trained ML model
- Displays ML confidence score as a percentage
- Shows ML signal breakdown (if available)
- Gives a verdict from each engine:
  - Likely Safe
  - Suspicious
  - Likely Phishing
- Provides explanations for why an email may be risky
- Clean, simple web interface

---

## Screenshots

### Homepage

![Homepage Screenshot](images/homepage.png)

### Analysis Result Page

![Result Screenshot](images/results.png)

### Terminal Version

![Terminal Scanner Screenshot](images/terminal-version.png)

```text
phishguard/
│
├── images/
│   ├── homepage.png
│   ├── results.png
│   └── terminal-version.png
```

---

## Version History

---

## Version 3 — Machine Learning Classifier

Version 3 adds a second detection engine powered by machine learning. Both the rule-based engine and the ML classifier run on every submitted email, and their results are shown side by side.

### What Changed in Version 3

- Added `ml_detector.py` with a trained ML classifier
- Results page now shows both rule-based and ML verdicts
- ML confidence score displayed as a progress bar
- ML signal breakdown section (if the model returns feature details)
- Updated Flask routes in `app.py` to call both engines and pass `ml_result` to the template

### Version 3 Web App Flow

```text
User pastes email
        ↓
Flask sends text to detector.py (rule-based)
Flask sends text to ml_detector.py (ML model)
        ↓
Rule engine: scans keywords, links, patterns → risk score + verdict
ML engine:   classifies email → label + confidence score
        ↓
Both results displayed on results page
```

### Version 3 Features

- All Version 2 features
- ML verdict (label + confidence %)
- ML signal breakdown (if available from model)
- Side-by-side rule-based and ML analysis

---

## Version 2 — Flask Web Application

Version 2 upgraded the project from a terminal-based Python scanner into a web application using Flask.

### What Changed in Version 2

- Added a web interface using HTML and CSS
- Created a homepage where users can paste email text
- Added a results page to display the phishing analysis report
- Separated the detection logic into a cleaner `detector.py` file
- Used Flask routes to handle form submissions
- Improved the project structure using `templates/` and `static/` folders
- Made the tool easier for non-technical users to use
- Added clearer explanations for why an email may be suspicious

### Version 2 Web App Flow

```text
User pastes email
        ↓
Flask sends text to detector.py
        ↓
PhishGuard scans content and links
        ↓
Risk score and verdict are generated
        ↓
Results are shown on the website
```

---

## Version 1 — Python Terminal Scanner

Version 1 was the first version of PhishGuard. It was a command-line Python program that analyzed email text directly in the terminal.

### What Version 1 Did

- Allowed users to paste email text into the terminal
- Scanned the email for suspicious phishing-related keywords
- Extracted links from the email
- Checked links for suspicious patterns
- Calculated a phishing risk score
- Printed a phishing analysis report in the terminal

### Version 1 Example Output

```text
=== Phishing Analysis Report ===

Verdict: Suspicious
Risk Score: 41/100

Suspicious Words Found:
- urgent
- verify
- password
- account suspended

Links Found:
- http://bit.ly/fake-login

Suspicious Links:
- http://bit.ly/fake-login: shortened link
```

---

## Main Changes Across Versions

| Area | Version 1 | Version 2 | Version 3 |
|---|---|---|---|
| Interface | Terminal | Flask website | Flask website |
| User input | Command line | Web form | Web form |
| Output | Terminal text | Results page | Results page (dual engines) |
| Detection | Rule-based | Rule-based | Rule-based + ML classifier |
| ML support | None | None | Label + confidence + breakdown |
| Design | No design | Clean styled interface | Clean styled interface |
| Code structure | One Python file | `app.py`, `detector.py`, HTML, CSS | + `ml_detector.py` |
| Usability | Developers | General users | General users |

---

## Project Structure

```text
phishguard/
│
├── app.py
├── detector.py
├── ml_detector.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── images/
│   ├── homepage.png
│   ├── results.png
│   └── terminal-version.png
│
└── README.md
```

---

## How It Works

PhishGuard uses two independent detection engines.

### Rule-Based Engine (`detector.py`)

Checks for:

1. Suspicious words
2. Suspicious links
3. Shortened URLs
4. IP-based URLs
5. Very long domains
6. Domains with unusual formatting

Then calculates a risk score and gives a verdict.

### ML Engine (`ml_detector.py`)

- Classifies the email using a trained machine learning model
- Returns a label (`Phishing`, `Suspicious`, `Safe`, etc.)
- Returns a confidence score between 0.0 and 1.0
- Optionally returns a list of signal details explaining the classification

The ML result is passed to the template as `ml_result` with the structure:

```python
{
  "label":      "Phishing",   # verdict string
  "confidence": 0.92,         # float 0.0–1.0
  "details":    ["..."]       # optional list of explanation strings
}
```

---

## Risk Score System (Rule-Based)

PhishGuard assigns points based on suspicious indicators. The final score is capped at 100.

### Verdict Levels

| Score Range | Verdict |
|---|---|
| 0–34 | Likely Safe |
| 35–69 | Suspicious |
| 70–100 | Likely Phishing |

---

## Example Test Email

```text
URGENT! Your account has been suspended.
Click here to verify your password now:
http://bit.ly/fake-login
```

Expected result:

```text
Rule-Based Verdict: Suspicious
Risk Score: Medium/High
Reason: Urgent language and shortened link detected

ML Verdict: Phishing
Confidence: ~90%
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/phishguard.git
cd phishguard
```

### 2. Install Dependencies

```bash
pip install flask scikit-learn
```

### 3. Run the App

```bash
python app.py
```

### 4. Open in Browser

```text
http://127.0.0.1:5000
```

---

## Files Explained

### `app.py`

Runs the Flask web application. Handles the homepage route and the `/analyze` POST route. Calls both `detector.py` and `ml_detector.py` and passes both results to `result.html`.

### `detector.py`

Rule-based phishing detection logic. Scans the email text, extracts links, calculates the risk score, and returns a result dict.

### `ml_detector.py`

Machine learning classifier. Takes the raw email text and returns a label, confidence score, and optional signal details.

### `templates/index.html`

Homepage where users paste the email text.

### `templates/result.html`

Results page. Displays the rule-based verdict (score ring, flagged words, suspicious links) and the ML verdict (confidence bar, signal breakdown) side by side.

### `static/style.css`

Styles the website. Keeps the interface clean and readable with a light background and clear card-based layout.

---

## Technologies Used

- Python
- Flask
- scikit-learn (ML classifier)
- HTML / CSS
- Regular Expressions
- URL Parsing

---

## Cybersecurity Concepts Used

- Phishing detection
- Email security
- Suspicious link analysis
- Social engineering indicators
- Risk scoring
- Threat detection logic
- URL analysis
- Machine learning classification

---

## Version Roadmap

| Version | Description | Status |
|---|---|---|
| Version 1 | Python terminal phishing scanner | Complete |
| Version 2 | Flask web application | Complete |
| Version 3 | Machine learning email classifier | Complete |
| Version 4 | AI explanation system | Planned |
| Version 5 | Online deployment | Planned |

---

## Future Improvements

- Add AI-generated explanations for ML predictions
- Add PDF report generation
- Improve sender email analysis
- Improve domain reputation checks
- Add file upload support for `.eml` files
- Deploy the website online
- Add a browser extension version

---

## What I Learned

Through this project, I learned how to build a cybersecurity tool from the ground up — starting with a basic Python terminal scanner, upgrading it into a Flask web app, and then adding a machine learning classifier as a second detection engine.

I learned how phishing emails use urgency, suspicious links, and social engineering to trick users. I also learned how to organize a multi-file Python project, build Flask routes, integrate an ML model into a web app, and pass multiple result objects to Jinja2 templates.

---

## Disclaimer

PhishGuard is an educational cybersecurity project. It is not a replacement for professional email security software. Users should still be careful when opening links or attachments from unknown senders.
