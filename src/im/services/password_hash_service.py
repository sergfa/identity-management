import hashlib


class PasswordHashingService:
    def hash_password(self, password: str) -> str:
        hashed_str: str = None
        if password:
            encoded_password = password.encode()
            hashed = hashlib.sha256(encoded_password)
            hashed_str = hashed.hexdigest()
        return hashed_str
