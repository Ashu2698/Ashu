from cryptography.fernet import Fernet
import json

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.key = self.generate_key(master_password)

    def generate_key(self, master_password):
        return Fernet.generate_key()

    def encrypt_data(self, data):
        cipher_suite = Fernet(self.key)
        return cipher_suite.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        cipher_suite = Fernet(self.key)
        try:
            return cipher_suite.decrypt(encrypted_data).decode()
        except Exception as e:
            print("Decryption failed:", e)
            return None

    def save_password(self, account_name, username, password):
        data = {'username': username, 'password': password}
        encrypted_data = self.encrypt_data(json.dumps(data))
        if encrypted_data:
            # In a real-world scenario, you would save the encrypted data securely, such as in a database or file system
            print(f"Saved password for {account_name}.")
        else:
            print("Failed to encrypt password data.")

    def retrieve_password(self, account_name, encrypted_data):
        decrypted_data = self.decrypt_data(encrypted_data)
        if decrypted_data:
            data = json.loads(decrypted_data)
            return data.get('username'), data.get('password')
        else:
            print("Failed to retrieve password.")
            return None, None

def main():
    master_password = input("Enter master password: ")
    password_manager = PasswordManager(master_password)

    # Save passwords
    account_name = "example.com"
    username = "user123"
    password = "password123"
    encrypted_data = password_manager.save_password(account_name, username, password)

    # Retrieve passwords
    if encrypted_data:
        username, password = password_manager.retrieve_password(account_name, encrypted_data)
        if username and password:
            print(f"Retrieved username: {username}, password: {password}")

if __name__ == "__main__":
    main()
