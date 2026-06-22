email = input('Please Paste the Email you recevied:\n')
words = [
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
    "social security number", "ssn", "bank account", "ire transfer", "western union", "bitcoin", "cryptocurrency payment",
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
    "next of kin", "beneficiary", "millions of dollars", "investment opportunity"credit card number",
    "update payment details", "confirm your identity", "verify now",
    "validate your account", "unusual login attempt", "new sign-in detected",
    "we noticed a login", "someone tried to access your account",
    "your password will expire", "your subscription has expired",
    "renew your subscription", "failed delivery", "package held",
    "delivery failed", "shipping problem", "track your package",
    "courier service", "customs fee", "release your package",
    "w
]

email_lower = email.lower()
found = []
for phrase in words:
    if phrase in email_lower:
        found.append(phrase)

if found:
    print(f"SCAM EMAIL PLEASE IGNORE ({len(found)}):")
    for phrase in found:
        print(f" - {phrase}")

else:
    print("No suspicious phrases found.")
