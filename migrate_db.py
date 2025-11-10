from app import app, db
from sqlalchemy import text

def migrate_database():
    with app.app_context():
        # Create the profile_pic column if it doesn't exist
        try:
            # Try to add the column using SQLAlchemy text()
            with db.engine.connect() as connection:
                connection.execute(text('ALTER TABLE user ADD COLUMN profile_pic VARCHAR(200)'))
                connection.commit()
            print("Successfully added profile_pic column to user table")
        except Exception as e:
            print(f"Error during migration: {e}")
            print("This might be because the column already exists or another error occurred.")

if __name__ == '__main__':
    migrate_database()
