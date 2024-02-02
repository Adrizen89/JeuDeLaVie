from auth import create_user
from database import initialize_db

def main():
    """ Point d'entrée de l'application. """
    initialize_db()

if __name__ == "__main__":
    main()
