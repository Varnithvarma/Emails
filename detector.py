import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = [
    "urgent", "verify", "password", "login", "account suspended",
    "click here", "act now", "limited time", "confirm your account",
    "payment failed", "security alert", "unusual activity",
    "reset your password", "gift card", "winner", "free prize",
    "verify your identity", "update your information", "account locked",
    "suspicious activity", "unauthorized access", "verify your account now",
    "your account has been compromised", "click the link below",
    "respond immediately", "final notice", "immediate action required",
    "you have won", "congratulations you've been selected", "claim your reward",
    "claim your prize", "exclusive offer", "act immediately", "expires today",
    "this offer expires", "your account will be closed",
    "your account will be terminated", "billing problem", "payment declined",
    "invoice attached", "outstanding balance", "tax refund", "irs notice",
    "social security number", "ssn", "bank account", "credit card number",
    "update payment details", "confirm your identity", "verify now",
    "validate your account", "unusual login attempt", "new sign-in detected",
    "we noticed a login", "someone tried to access your account",
    "your password will expire", "your subscription has expired",
    "renew your subscription", "failed delivery", "package held",
    "delivery failed", "shipping problem", "track your package",
    "courier service", "customs fee", "release your package",
    "wire transfer", "western union", "bitcoin", "cryptocurrency payment",
    "send payment immediately", "urgent wire transfer needed",
    "ceo request", "confidential request", "do not tell anyone",
    "keep this confidential", "this is not a scam", "no obligation",
    "risk free", "guaranteed", "100% free", "no credit card required",
    "act fast", "don't miss out", "last chance", "hurry",
    "time sensitive", "response required within 24 hours",
    "your account is under review", "we detected unusual activity",
    "click to unsubscribe", "click to update", "click to confirm",
    "verify your billing information", "your payment method failed",
    "update your billing info", "security breach", "data breach notification",
    "your information has been compromised", "reset link", "click below to reset",
    "claim now", "redeem your reward", "you've been chosen", "lucky winner",
    "free gift", "no purchase necessary", "lottery winner", "inheritance",
    "next of kin", "beneficiary", "millions of dollars", "investment opportunity"
]


SHORT_URLS = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly", "is.gd"]


def extract_links(text):
    return re.findall(r"https?://[^\s]+|www\.[^\s]+", text)


def find_suspicious_words(text):
    text = text.lower()
    found = []

    for word in SUSPICIOUS_WORDS:
        if word in text:
            found.append(word)

    return found


def check_links(links):
    suspicious = []

    for link in links:
        fixed_link = link if link.startswith("http") else "http://" + link
        domain = urlparse(fixed_link).netloc.lower()

        reasons = []

        if domain in SHORT_URLS:
            reasons.append("shortened link")

        if re.search(r"\d+\.\d+\.\d+\.\d+", domain):
            reasons.append("uses IP address instead of normal domain")

        if len(domain) > 35:
            reasons.append("very long domain")

        if domain.count("-") >= 2:
            reasons.append("many hyphens in domain")

        if reasons:
            suspicious.append({
                "link": link,
                "reasons": reasons
            })

    return suspicious


def calculate_score(words, suspicious_links):
    score = 0
    score += len(words) * 7
    score += len(suspicious_links) * 20

    return min(score, 100)


def get_verdict(score):
    if score >= 70:
        return "Likely Phishing"
    elif score >= 35:
        return "Suspicious"
    else:
        return "Likely Safe"


def explain_result(verdict, words, suspicious_links):
    explanations = []

    if words:
        explanations.append(
            "The email contains suspicious language often used in scams, such as urgency, account warnings, or requests for personal information."
        )

    if suspicious_links:
        explanations.append(
            "The email includes suspicious links, such as shortened URLs, unusually long domains, IP-based links, or domains with strange formatting."
        )

    if verdict == "Likely Safe" and not explanations:
        explanations.append(
            "No major phishing indicators were found by the scanner. Still, users should verify the sender before clicking links."
        )

    return explanations


def analyze_email(email_text):
    words = find_suspicious_words(email_text)
    links = extract_links(email_text)
    suspicious_links = check_links(links)
    score = calculate_score(words, suspicious_links)
    verdict = get_verdict(score)
    explanations = explain_result(verdict, words, suspicious_links)

    return {
        "verdict": verdict,
        "score": score,
        "words": words,
        "links": links,
        "suspicious_links": suspicious_links,
        "explanations": explanations
    }