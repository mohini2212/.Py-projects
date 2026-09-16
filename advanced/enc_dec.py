from cryptography.fernet import Fernet

def generate_key():
    """Generate a key and save it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

def load_key():
    """Load the previously generated key."""
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(filename, key):
    """Encrypt a file and save it as a new file."""
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    encrypted_filename = filename + ".encrypted"
    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    print(f"File encrypted and saved as {encrypted_filename}")

def decrypt_file(filename, key):
    """Decrypt a file and save it back to its original form."""
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_filename = filename.replace(".encrypted", ".decrypted")
    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"File decrypted and saved as {decrypted_filename}")

def main():
    print("=== File Encryption/Decryption Tool ===")
    print("1. Generate a new key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")

    choice = input("Enter your choice (1/2/3): ")

    match choice:
        case "1":
            generate_key()

        case "2":
            filename = input("Enter the filename to encrypt: ")
            key = load_key()
            encrypt_file(filename, key)

        case "3":
            filename = input("Enter the filename to decrypt: ")
            key = load_key()
            decrypt_file(filename, key)

        case _:
            print("Invalid choice.")

if __name__ == "__main__":
    main()