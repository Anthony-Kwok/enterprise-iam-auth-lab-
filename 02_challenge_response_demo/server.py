import hashlib
import os

# Simulated user database
USERS = {
    "alice": {
        "salt": b"static_salt",
        "password_hash": hashlib.sha256(b"password123" + b"static_salt").digest()
    }
}

def generate_challenge():
    return os.urandom(16)

def verify_response(username, challenge, response):
    user = USERS.get(username)
    if not user:
        return False

    expected = hashlib.sha256(
        user["password_hash"] + challenge
    ).digest()

    return expected == response

def main():
    username = input("Username: ")

    challenge = generate_challenge()
    print(f"Challenge sent to client: {challenge.hex()}")

    response_hex = input("Client response: ")
    response = bytes.fromhex(response_hex)

    if verify_response(username, challenge, response):
        print("Authentication successful")
    else:
        print("Authentication failed")

if __name__ == "__main__":
    main()
