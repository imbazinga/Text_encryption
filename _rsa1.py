from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    generate_key()
    key = load_key()

    while True:
        choice = input("Choose an option: \n1. Encrypt a message \n2. Decrypt a message \n3. Exit\n---------------------\n")
        
        if choice == '1':
            print('------------------------------')
            original_message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(original_message, key)
            print("Encrypted message:", encrypted_message)
            print('-------------------------------------')
        
        elif choice == '2':
            print("------------------------------")
            encrypted_message = input("Enter the message to decrypt:")
            try:
                decrypted_message = decrypt_message(encrypted_message, key)
                print("Decrypted message:", decrypted_message)
            except Exception as e:
                print("An error occurred during decryption:", e)
                print('---------------------------------------')
        
        elif choice == '3':
            break
        
        else:
            print("option doesnt exist. ")
