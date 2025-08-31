# ----------------------------------------------------------
# CipherLock - Password Analyzer
# Developed by: Tayyab Akhtar
# Description: Simple password tool to:
# - Check password strength
# - Generate random passwords
# - Encrypt passwords (basic hashing)
# Requirements: Python 3.10
# Dependencies: re,random,string,hashlib,time (all standard libraries)
# ----------------------------------------------------------

import string
import random
import hashlib
import time

def show_logo():
    logo = r"""
   _____ _       _               _            _     
  / ____(_)     | |             | |          | |    
 | |     _ _ __ | |__   ___ _ __| | ___   ___| | __ 
 | |    | | '_ \| '_ \ / _ \ '__| |/ _ \ / __| |/ / 
 | |____| | |_) | | | |  __/ |  | | (_) | (__|   <  
  \_____|_| .__/|_| |_|\___|_|  |_|\___/ \___|_|\_\ 
          | |                                       
          |_|                                       

                CipherLock - Password Analyzer
                Developed by: Tayyab Akhtar
    """
    print(logo)
    print("=" * 75)
    time.sleep(2)

# Password strength evaluation 
def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    value = 0
    if length >= 8:
        value += 1
    if length >= 12:
        value += 1
    if has_upper:
        value += 1
    if has_lower:
        value += 1
    if has_digit:
        value += 1
    if has_special:
        value += 1

    if value <= 2:
        return "Weak"
    elif value <= 4:
        return "Normal"
    else:
        return "Strong"

# Generate random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Simple breach check
def check_breach(password):
    fake_breached = ["password", "123456", "qwerty"]
    return password.lower() in fake_breached

# Encrypt password 
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    while True:
        show_logo()
        print("Choose an option:")
        print("1) Enter your own password")
        print("2) Auto-generate a password")
        print("3) Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '3':
            print("Exiting the tool. Goodbye!")
            break

        if choice == '1':
            pwd = input("Enter your password: ")
        elif choice == '2':
            pwd = generate_password()
            print(f"Generated Password: {pwd}")
        else:
            print("Invalid choice. Try again.\n")
            continue

        print("What would you like to do with the password?")
        print("1) Encrypt your password")
        print("2) Nothing (use as it is)")
        action = input("Enter choice (1/2): ")

        if action == '1':
            pwd = encrypt_password(pwd)
            print(f"Encrypted Password (SHA-256): {pwd}")
        else:
            print("Password unchanged.\n")

        strength = password_strength(pwd)
        breached = check_breach(pwd)

        print(f"Strength: {strength}\n")
        if breached:
            print("[Warning] This password has appeared in known breaches!")
        else:
            print("No known breach detected for this password.")

        cont = input("\nDo you want to analyze another password? (y/n): ")
        if cont.lower() != 'y':
            print("Exiting the tool. Goodbye!")
            break
