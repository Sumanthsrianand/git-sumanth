# Import the necessary libraries
from cryptography.fernet import Fernet


def generate_key():
    """
    Generate a key for encryption and decryption.
    """
    key = Fernet.generate_key()
    return key


def encrypt_data(data, key):
    """
    Encrypt the given data using the provided key.

    Args:
        data (str): The data to be encrypted.
        key (bytes): The encryption key.

    Returns:
        bytes: The encrypted data.
    """
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text


def decrypt_data(cipher_text, key):
    """
    Decrypt the given cipher text using the provided key.

    Args:
        cipher_text (bytes): The cipher text to be decrypted.
        key (bytes): The decryption key.

    Returns:
        str: The decrypted data.
    """
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text


# Example usage
if __name__ == "__main__":
    key = generate_key()
    print("Generated Key:", key)

    data = "This is some secret data."
    print("Original Data:", data)

    encrypted_data = encrypt_data(data, key)
    print("Encrypted Data:", encrypted_data)

    decrypted_data = decrypt_data(encrypted_data, key)
    print("Decrypted Data:", decrypted_data)# Import the necessary libraries
from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a key for encryption and decryption.
    """
    key = Fernet.generate_key()
    return key

def encrypt_data(data, key):
    """
    Encrypt the given data using the provided key.

    Args:
        data (str): The data to be encrypted.
        key (bytes): The encryption key.

    Returns:
        bytes: The encrypted data.
    """
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

def decrypt_data(cipher_text, key):
    """
    Decrypt the given cipher text using the provided key.

    Args:
        cipher_text (bytes): The cipher text to be decrypted.
        key (bytes): The decryption key.

    Returns:
        str: The decrypted data.
    """
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text

# Example usage
if __name__ == "__main__":
    key = generate_key()
    print("Generated Key:", key)

    data = "This is some secret data."
    print("Original Data:", data)

    encrypted_data = encrypt_data(data, key)
    print("Encrypted Data:", encrypted_data)

    decrypted_data = decrypt_data(encrypted_data, key)
    print("Decrypted Data:", decrypted_data)