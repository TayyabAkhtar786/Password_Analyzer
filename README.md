#  CipherLock - Password Analyzer

##  Overview
CipherLock is a Python-based password utility designed to **analyze, generate, and secure passwords**.  
It helps users understand password strength, generate strong random passwords, and apply SHA-256 hashing for secure storage.  
The tool also flags common weak passwords to raise awareness of unsafe practices.  

 **Note:** This project is for educational and security awareness purposes only.  

---

##  Features
-  **Password Strength Check** – rates passwords as Weak, Normal, or Strong  
-  **Random Password Generator** – creates strong passwords with custom length  
-  **SHA-256 Hashing** – demonstrates secure password encryption  
-  **Breach Awareness** – detects if passwords match a small list of common unsafe passwords  
-  **Interactive CLI Menu** – user-friendly design with ASCII banner  

---

##  Installation & Usage
### Requirements
- Python 3.10 or later  
- Standard libraries: `string`, `random`, `hashlib`, `time`

### Run the tool
bash
git clone https://github.com/tayyabakhtar786/Password_Analyzer.git
- cd cipherlock
- python3 cipherlock.py

Choose an option:
1) Enter your own password
2) Auto-generate a password
3) Exit

Enter your password: MyPassword123!
-Strength: Strong

Generated Password: 9$FwP@lRz!2b
-Encrypted Password (SHA-256): e3afed0047b08059d0fada10f400c1e5...



