from database import engine, SessionLocal, Base
from models import User

Base.metadata.create_all(bind=engine)

session = SessionLocal()

def create_user(name, email):
    existing = session.query(User).filter_by(email=email).first()
    if existing:
        print(f"User with email {email} already exists.")
    else:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print("User created!")


# READ
def read_users():
    users = session.query(User).all()
    for user in users:
        print(user.id, user.name, user.email)

if __name__ == "__main__":
    create_user("Alice", "alice@example.com")
    create_user("Bob", "bob@example.com")
    create_user("virat","virat@example.com")
    create_user("rahul","rahul@example.com")
    
    print("All users:")
    read_users()
