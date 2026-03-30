import re
import sys
from getpass import getpass

def check_password(password):
    if not password:
        raise ValueError("Password cannot be empty!")

    score = 0
    feedback = []
    suggestions = []

    
    if len(password) >= 12:
        score += 3
        feedback.append("✓ Strong length (12+ characters)")
    elif len(password) >= 8:
        score += 2
        feedback.append("✓ Good length (8+ characters)")
    else:
        feedback.append("✗ Too short (min 8 characters)")
        suggestions.append("Increase password length")

    
    patterns = {
        "Uppercase": r"[A-Z]",
        "Lowercase": r"[a-z]",
        "Numbers": r"[0-9]",
        "Special characters": r"[!@#$%^&*(),.?\":{}|<>]"
    }

    for label, pattern in patterns.items():
        if re.search(pattern, password):
            score += 1
            feedback.append(f"✓ Contains {label}")
        else:
            feedback.append(f"✗ Missing {label}")
            suggestions.append(f"Add {label}")

    
    if re.search(r"(.)\1{2,}", password):
        suggestions.append("Avoid repeated characters (e.g., aaa)")

    if re.search(r"(123|abc|password|qwerty)", password.lower()):
        suggestions.append("Avoid common patterns (123, abc, qwerty)")

    if password.isdigit() or password.isalpha():
        suggestions.append("Use a mix of characters")

    
    if score >= 6:
        strength = "Strong 💪"
    elif score >= 4:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    return score, strength, feedback, suggestions


def main():
    print("=" * 40)
    print("   🔐 Password Complexity Checker")
    print("=" * 40)
    print("Type 'exit' to quit\n")

    while True:
        try:
            password = getpass("Enter password: ")

            if password.lower() == "exit":
                print("\n👋 Exiting program...")
                break

            score, strength, feedback, suggestions = check_password(password)

            print("\n📊 RESULT")
            print("-" * 30)
            print(f"Strength: {strength} ({score}/7)\n")

            print("✔ Checks:")
            for item in feedback:
                print(" ", item)

            if suggestions:
                print("\n💡 Suggestions:")
                for s in suggestions:
                    print(" ", s)

            print("\n" + "=" * 40 + "\n")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            sys.exit(0)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()