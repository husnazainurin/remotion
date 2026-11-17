from database.connection import init_connection


def get_user_by_username(username):
    '''Fetch account from database using username'''
    conn = init_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT user_id, username, passkey, role_id
            FROM dbo.users
            WHERE username = ?
            """,
            (username,)
        )

        user = cursor.fetchone()

        if user:
            return {
                "user_id": user[0],
                "username": user[1],
                "passkey": user[2],
                "role_id": user[3]
            }

        return None

    finally:
        cursor.close()


def register_patient(username, password):
    '''Create new entry in the database from sign up form'''

    conn = init_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO dbo.users (username, passkey, role_id)
            VALUES (?, ?, ?)
            """,
            (username, password, 2)
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()


def get_list_users():
    '''Return a list of all existing usernames'''
    conn = init_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT username FROM dbo.users
            """
        )

        usernames = cursor.fetchall()

        return [user[0] for user in usernames]

    finally:
        cursor.close()

