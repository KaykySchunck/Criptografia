from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Gerando a chave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Obtendo a chave pública
public_key = private_key.public_key()

# Mensagem a ser criptografada
mensagem = "Está mensagem é secreta.".encode('utf-8')

# Criptografando a mensagem com a chave pública
mensagem_criptografada = public_key.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Mensagem criptografada:", mensagem_criptografada)

# Descriptografando a mensagem com a chave privada
mensagem_descriptografada = private_key.decrypt(
    mensagem_criptografada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Mensagem descriptografada:", mensagem_descriptografada.decode())
