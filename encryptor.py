from cryptography.fernet import Fernet

# key=Fernet.generate_key()
# with open("secret.key", "wb") as key_file:
#     key_file.write(key)

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)



def encrypt_file(file_name):
    """Encrypt the log file."""
    with open(file_name, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"File {file_name} has been encrypted.")




def decrypt_file(file_name, decypted_file_name):
    """Decrypt the log file."""
    with open(file_name, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(decypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted)
    print(f"File {file_name} has been decrypted.")
