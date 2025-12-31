import hashlib

USERNAME = "alice"
PASSWORD = b"password123"
SALT = b"static_salt"

def compute_response(password, salt, challenge):
    password_hash = hashlib.sha256(password + salt).digest()
    return hashlib.sha256(password_hash + challenge).digest()

def main():
    challenge_hex = input("Enter challenge from server: ")
    challenge = bytes.fromhex(challenge_hex)

    response = compute_response(PASSWORD, SALT, challenge)
    print(response.hex())

if __name__ == "__main__":
    main()
