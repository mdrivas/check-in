from app import app, db  # Import your app and User model
from app.models import User

def update_user_statuses():
    with app.app_context():  # Create an application context
        users = User.query.all()
        for user in users:
            print(f"Updating user: {user.username}, Old status: {user.status}")
            user.status = False
            print(f"New status: {user.status}")
        
        db.session.commit()

if __name__ == '__main__':
    update_user_statuses()
    print("User statuses updated successfully.")
