# Prodigy_CS_03
# 🔐 Password Complexity Checker

A simple yet powerful **Python-based Password Strength Checker** that evaluates the security of a password based on multiple criteria and provides helpful feedback and suggestions.

---

## 📌 Project Description

This project analyzes a user-entered password and determines its **strength level (Weak, Medium, Strong)** based on:

* Length of the password
* Use of uppercase and lowercase letters
* Inclusion of numbers
* Presence of special characters
* Detection of weak patterns

It also gives **real-time feedback** and **improvement suggestions** to help users create stronger passwords.

---

## 🚀 Features

* 🔒 Hidden password input using `getpass`
* 📊 Password strength scoring system
* ✅ Detailed validation checks
* 💡 Suggestions for improving weak passwords
* ⚠️ Detection of common patterns (e.g., `123`, `abc`, `qwerty`)
* 🔁 Continuous checking until user exits

---

## 🛠️ Technologies Used

* Python 3
* Built-in modules:

  * `re` (Regular Expressions)
  * `sys`
  * `getpass`

---

## 📂 How It Works

1. User enters a password (input is hidden).
2. The program evaluates the password using predefined rules.
3. A score is generated out of 7.
4. Password strength is classified as:

   * **Strong 💪**
   * **Medium ⚠️**
   * **Weak ❌**
5. Feedback and suggestions are displayed.

---

---

## 🧪 Example Output

```
========================================
   🔐 Password Complexity Checker
========================================
Type 'exit' to quit

Enter password:

📊 RESULT
------------------------------
Strength: Medium ⚠️ (4/7)

✔ Checks:
  ✓ Good length (8+ characters)
  ✓ Contains Lowercase
  ✗ Missing Uppercase
  ✓ Contains Numbers
  ✗ Missing Special characters

💡 Suggestions:
  Add Uppercase
  Add Special characters
```

---

## 📏 Password Evaluation Criteria

| Criteria           | Score |
| ------------------ | ----- |
| Length ≥ 12        | +3    |
| Length ≥ 8         | +2    |
| Uppercase Letters  | +1    |
| Lowercase Letters  | +1    |
| Numbers            | +1    |
| Special Characters | +1    |

---




## 👨‍💻 Author

**Sushmita Suryakant Sangle**
Task 3 : Password Complexity Checker - Completed

---


