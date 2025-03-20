import base64
import hashlib
import os
from cryptography.fernet import Fernet

class SecurityModule:
    def __init__(self):
        """ Initializes encryption system. """
        self.key = base64.urlsafe_b64encode(hashlib.sha256(os.urandom(32)).digest())
        self.fernet = Fernet(self.key)

    def encrypt_code(self, code: str) -> str:
        """ Encrypts AI-generated solutions. """
        return self.fernet.encrypt(code.encode()).decode()

    def decrypt_code(self, encrypted_code: str) -> str:
        """ Decrypts AI-generated solutions. """
        return self.fernet.decrypt(encrypted_code.encode()).decode()

# Example Usage
if __name__ == "__main__":
    security = SecurityModule()
    sample_code = "def solve_problem(arr):\n    return max(arr)\n"
    
    encrypted = security.encrypt_code(sample_code)
    print("Encrypted Code:", encrypted)
    
    decrypted = security.decrypt_code(encrypted)
    print("Decrypted Code:\n", decrypted)
