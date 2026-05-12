import secrets
import string
from datetime import datetime


def generate_public_id() -> str:
    """Generate a unique 11-character public id"""
    return secrets.token_urlsafe(nbytes=8)


def generate_transaction_id(length: int = 12) -> str:
    """Generate a secure random alphanumeric transaction ID"""
    alphabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def generate_otp_token() -> str:
    """Generate an OTP token"""
    return f"{secrets.randbelow(1000000):06d}"


def strip_tz(dt: datetime | None = None) -> datetime | None:
    if dt is not None and dt.tzinfo is not None:
        return dt.replace(tzinfo=None)
    return dt
