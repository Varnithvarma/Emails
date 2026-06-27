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


def scan_email(email):
    email_lower = email.lower()
    found = []

    for phrase in words:
        if phrase in email_lower:
            found.append(phrase)

    print("\n===== PHISHGUARD RESULT =====")

    if found:
        print(f"SCAM EMAIL WARNING: {len(found)} suspicious phrase(s) found.")
        print("\nSuspicious phrases:")
        for phrase in found:
            print(f" - {phrase}")
    else:
        print("No suspicious phrases found.")

    print("=============================\n")


def main():
    print("====================================")
    print("       PHISHGUARD EMAIL SCANNER      ")
    print("====================================")
    print("Paste an email to scan it for scam/phishing phrases.")
    print("Type 'quit' anytime to close the program.\n")

    while True:
        email = input("Please paste the email you received:\n\n")

        if email.lower().strip() in ["quit", "exit", "q"]:
            print("\nClosing PhishGuard...")
            break

        if not email.strip():
            print("\nYou did not paste anything. Try again.\n")
            continue

        scan_email(email)

        again = input("Scan another email? (y/n): ").lower().strip()

        if again not in ["y", "yes"]:
            print("\nThanks for using PhishGuard.")
            break

        print("\n")


if __name__ == "__main__":
    main()
    input("\nPress Enter to close...")