import bcrypt
from database import create_connection

def hash_password(password):
    """ Hash un mot de passe. """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def create_user(username, password):
    """ Crée un nouvel utilisateur dans la base de données. """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                   (username, hash_password(password)))
    conn.commit()
    conn.close()
    
def verify_user(username, password):
    """ Vérifie si les identifiants de l'utilisateur sont corrects. """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    stored_password_hash = cursor.fetchone()
    
    if stored_password_hash is None:
        return False
    
    return bcrypt.checkpw(password.encode(), stored_password_hash[0])
