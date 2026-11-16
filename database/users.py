from sqlalchemy import text
from database.connection import get_session


def get_user_by_username(username):
    '''Fetch account from database using username'''

    with get_session() as session:

        result = session.execute(
            text("""
                SELECT user_id, username,
                       password, role_id, referral_code
                FROM users
                WHERE username = :username
            """),
            {"username": username}
        )

        user = result.mappings().first()

        return dict(user) if user else None

def get_therapist_for_patient(user_id):
    """Join users and Therapist on referral_code using the logged-in patient's user_id."""
    with get_session() as session:
        result = session.execute(
            text("""
                SELECT t.referral_code, t.username AS therapist_name
                FROM users u
                INNER JOIN Therapist t
                    ON TRIM(u.referral_code) = TRIM(t.referral_code)
                WHERE u.user_id = :user_id
            """),
            {"user_id": user_id},
        )
        row = result.mappings().first()
        return dict(row) if row else None

def update_patient_referral_code(user_id, referral_code):
    """Link a patient account to a therapist's referral code."""
    with get_session() as session:
        session.execute(
            text("""
                UPDATE users
                SET referral_code = :referral_code
                WHERE user_id = :user_id
            """),
            {"referral_code": referral_code.strip(), "user_id": user_id},
        )
        session.commit()

def get_therapist_by_referral_code(referral_code):
    """Verify if a referral code exists in the Therapist table."""
    if not referral_code:
        return None

    with get_session() as session:
        result = session.execute(
            text("""
                SELECT referral_code, username AS therapist_name
                FROM Therapist
                WHERE TRIM(referral_code) = :referral_code
            """),
            {"referral_code": referral_code.strip()},
        )
        row = result.mappings().first()
        return dict(row) if row else None

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
