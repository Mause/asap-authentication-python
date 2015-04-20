from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def get_new_rsa_private_key_in_pem_format():
    """ returns a new rsa key in pem format. """
    private_key = rsa.generate_private_key(
        key_size=2048, backend=default_backend(), public_exponent=65537)
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
