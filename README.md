# PhishGuard — Phishing Email Scanner

PhishGuard is a cybersecurity web app that analyzes email text and identifies possible phishing indicators. It scans for suspicious keywords, risky links, shortened URLs, unusual domain patterns, and common scam language. The app then generates a risk score, verdict, and explanation to help users understand why an email may be unsafe.

This project was built to explore email security, phishing detection, Python programming, Flask web development, and cybersecurity analysis.

## Features

* Paste suspicious email text into a web interface
* Detect suspicious phishing-related keywords
* Extract and analyze links from emails
* Flag shortened URLs such as `bit.ly`, `tinyurl.com`, and `t.co`
* Detect suspicious domain patterns, including:

  * IP-based links
  * Very long domains
  * Domains with multiple hyphens
* Generate a phishing risk score from 0 to 100
* Classify emails as:

  * Likely Safe
  * Suspicious
  * Likely Phishing
* Provide plain-English explanations for the result
* Display a clean analysis report in the browser

## Project Purpose

Phishing is one of the most common cybersecurity threats. Attackers often use urgent language, fake login pages, suspicious links, and social engineering to trick users into giving away personal information.

The goal of PhishGuard is to create a beginner-friendly but practical tool that demonstrates how phishing indicators can be detected using programming logic and cybersecurity rules.

## Tech Stack

* Python
* Flask
* HTML
* CSS
* Regular Expressions
* URL Parsing

## How It Works

PhishGuard analyzes an email in multiple steps:

1. The user pastes email text into the website.
2. The app searches the email for suspicious words and phrases.
3. The app extracts all links from the email.
4. Each link is checked for risky patterns.
5. A risk score is calculated based on the number and severity of suspicious indicators.
6. The app returns a verdict and explanation.

## Example Test Email

```text
URGENT! Your account has been suspended.
Click here to verify your password now:
http://bit.ly/fake-login
```

## Example Output

```text
Verdict: Suspicious
Risk Score: 55/100

Suspicious Words Found:
- urgent
- account suspended
- click here
- verify
- password

Suspicious Links:
- http://bit.ly/fake-login — shortened link
```

## Folder Structure

```text
phishguard/
│
├── app.py
├── detector.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/phishguard.git
cd phishguard
```

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Open the local website in your browser:

```text
http://127.0.0.1:5000
```

## Files Explained

### `app.py`

Runs the Flask web server and handles website routes.

### `detector.py`

Contains the phishing detection logic, including keyword detection, link extraction, suspicious link analysis, risk scoring, and result explanations.

### `templates/index.html`

The homepage where users paste email text.

### `templates/result.html`

The results page that displays the analysis report.

### `static/style.css`

Styles the website layout, forms, buttons, and result cards.

## Current Detection Methods

PhishGuard currently uses rule-based detection. It checks for common phishing indicators such as:

* Urgent or threatening language
* Requests for passwords or login verification
* Suspicious links
* Shortened URLs
* Long or strange domains
* Links that use IP addresses instead of normal domain names

## Limitations

PhishGuard is an educational cybersecurity project and should not be used as a professional security tool. It may produce false positives or false negatives. A real-world phishing detection system would need more advanced techniques, larger datasets, machine learning models, email header analysis, domain reputation checks, and continuous updates.

## Future Improvements

Planned upgrades include:

* Add a machine learning model using TF-IDF and Logistic Regression
* Train the model on labeled phishing and safe email datasets
* Add email header analysis
* Add sender domain reputation checks
* Add AI-generated explanations
* Add PDF report generation
* Deploy the website online
* Add user-friendly risk categories and charts

## What I Learned

While building this project, I learned how phishing emails use social engineering, suspicious links, and urgent wording to trick users. I also learned how to build a Flask web app, process text input, extract URLs with regular expressions, analyze domain patterns, and generate cybersecurity-style reports.

## Disclaimer

This project is for educational purposes only. It is designed to help demonstrate phishing detection concepts and should not be relied on as the only method for determining whether an email is safe.
