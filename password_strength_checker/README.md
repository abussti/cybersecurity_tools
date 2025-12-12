4️⃣ Password Strength Checker
# Password Strength Checker (Python)

A simple Python script that checks whether a password meets strong security requirements.  
Designed as a beginner-friendly cybersecurity tool to practice Python, regular expressions, and secure password handling.

---

## 🔍 Password Requirements
The password is considered strong if it meets all of the following criteria:

- At least 6 characters long  
- Contains at least one uppercase letter [A-Z]  
- Contains at least one lowercase letter [a-z]  
- Contains at least one number [0-9]  
- Contains at least one special character (!, @, *, &)

---

## 🚀 Features
- Securely hides password input while typing (works in system terminals)  
- Provides clear feedback if the password is too weak  
- Stores passwords in memory (can be extended to store hashes)  
- Beginner-friendly and easy to extend

---

## ▶ How to Run
Run the script in your terminal:
bash
python password_checker.py

Enter a password when prompted. 
Example:

   Enter your password: 
   Password is strong enough, storing...
   Stored (hashed) passwords: ['5e884898da28047151d0e56f8dc6292773603d0d6aabbddc8b5...']

      ⚠ Note: Hidden input works only in terminal/command prompt. Some IDE consoles (like PyCharm Run) may show typed characters.


🛡️ Security Notes

   For learning purposes only; in a real application, always hash and salt passwords before storing.

   Never store plaintext passwords in production environments.

🎓 Author

Ahmad Bussti
Cybersecurity Student — Euclea Business School (Graduating 2027)
