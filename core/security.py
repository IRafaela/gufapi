import bcrypt
from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto', bcrypt__deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correta, comparando a senha em texto puro, informada pelo usuário, e o hash da senha que estará saldo no banco de dados durante a criação da conta.
    """
    try:
      return CRIPTO.verify(senha, hash_senha)
    except Exception:
       return False 

def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera e retorna o hash da senha
    """
    senha_bytes = senha.encode('utf-8')
    
    salt = bcrypt.gensalt()

    hash_bytes = bcrypt.hashpw(senha_bytes, salt)
    
    return hash_bytes.decode('utf-8')