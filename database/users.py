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
