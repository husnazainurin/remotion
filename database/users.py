from sqlalchemy import text
from database.connection import get_session


def get_user_by_username(username):
    '''Fetch account from database using username'''

    with get_session() as session:

        result = session.execute(
            text("""
                SELECT user_id, username,
                       password, role_id
                FROM users
                WHERE username = :username
            """),
            {"username": username}
        )

        user = result.mappings().first()

        return dict(user) if user else None

def register_patient(username, password, referral_code):
    '''Create new entry in the database from sign up form'''

    with get_session() as session:
        # Register new account into database
        session.execute(
            text(
                """
                INSERT INTO users (username, password, role_id, referral_code) 
                VALUES (:username, :password, :role_id, :referral_code);
            """
            ),
            {
                "username": username,
                "password": password,
                "role_id": 2,
                "referral_code": referral_code,
            },
        )
        session.commit()
