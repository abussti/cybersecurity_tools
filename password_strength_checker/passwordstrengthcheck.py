import stdiomask
import re
import hashlib

stored_passwords = []


def is_strong(pw):
    return (len(pw) > 5 and
            re.search(r"[0-9]", pw) and
            re.search(r"[!@*&]", pw) and
            re.search(r"[a-z]", pw) and
            re.search(r"[A-Z]", pw))


def strong_password():
    pw = stdiomask.getpass("Enter your password: ")

    if is_strong(pw):
        print("Your password is strong enough, storing...")
        hashed_pw = hashlib.sha256(pw.encode()).hexdigest()
        stored_passwords.append(hashed_pw)
        print("Stored (hashed) passwords:", stored_passwords)
    else:
        print("Password is too weak! Make sure it has:")
        print("- At least 6 characters")
        print("- At least one digit [0-9]")
        print("- At least one uppercase letter [A-Z]")
        print("- At least one lowercase letter [a-z]")
        print("- At least one special character (!,@,*,&)")


# Run the checker once
strong_password()