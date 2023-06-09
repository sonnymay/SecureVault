from cryptography.fernet import Fernet
import os


def generate_key():
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named `secret.key`
    """
    return open("secret.key", "rb").read()


def encrypt_file(filename, key):
    """
    Encrypts a file
    """
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    """
    Decrypts an encrypted file
    """
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    import sys
    
    action = input("Do you wish to encrypt or decrypt a file? (e/d): ").lower()
    filename = input("Enter the filename: ").strip()

    # generate a key if it doesn't exist
    if not os.path.exists("secret.key"):
        generate_key()

    # load the key
    key = load_key()

    if action == 'e':
        encrypt_file(filename, key)
        print(f"The file '{filename}' has been encrypted.")
    elif action == 'd':
        decrypt_file(filename, key)
        print(f"The file '{filename}' has been decrypted.")
    else:
        print("Invalid option. Use 'e' for encryption or 'd' for decryption.")
