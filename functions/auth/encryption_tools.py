from cryptography.fernet import Fernet


# Functions included in this file:
# # generate_new_key
# # encrypt_message
# # decrypt_message


def generate_new_key(enc='utf-8'):
    """Returns the new key as a plaintext string
    Used to generate a unique INI_KEY that's stored as an environmental variable
    Shuffle INI_KEY on a regular basis
    """
    return Fernet.generate_key().decode(enc)


def encrypt_message(message: str, ini_key: str, enc='utf-8'):
    """Given a plaintext message,
    returns an encrypted plaintext string
    
    Use this to generate encrypted keys in the .ini file
    """
    return Fernet(ini_key).encrypt(str.encode(message, enc)).decode(enc)


def decrypt_message(message: str, ini_key: str, enc='utf-8'):
    """Given an encrypted message from a .ini file,
    returns the unencrypted plaintext string
    """
    return Fernet(ini_key).decrypt(str.encode(message, enc)).decode(enc)
