import bcrypt

def encriptar_contraseña(contraseña: str) -> str:
    """Encripta una contraseña usando bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(contraseña.encode('utf-8'), salt).decode('utf-8')

def verificar_contraseña(contraseña_plana: str, contraseña_hash: str) -> bool:
    """Verifica una contraseña contra su hash bcrypt"""
    return bcrypt.checkpw(contraseña_plana.encode('utf-8'), contraseña_hash.encode('utf-8'))
