from database.connection import init_connection

# def update_patient_referral_code(user_id, referral_code):
#     """Link a patient account to a therapist's referral code."""
#     with get_session() as session:
#         session.execute(
#             text("""
#                 UPDATE users
#                 SET referral_code = :referral_code
#                 WHERE user_id = :user_id
#             """),
#             {"referral_code": referral_code.strip(), "user_id": user_id},
#         )
#         session.commit()



# def register_patient(username, password, referral_code):
#     '''Create new entry in the database from sign up form'''

#     conn = init_connection()

#     try:
#         cursor = conn.cursor()

#         cursor.execute(
#             """
#             INSERT INTO dbo.users (username, passkey, role_id)
#             VALUES (?, ?, ?)
#             """,
#             (username, password, 2)
#         )

#         conn.commit()

#     except Exception:
#         conn.rollback()
#         raise

#     finally:
#         cursor.close()


