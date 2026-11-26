# from database.connection import init_connection

# def get_therapist_for_patient(user_id):
#     """Join users and Therapist on referral_code using the logged-in patient's user_id."""
#     with get_session() as session:
#         result = session.execute(
#             text("""
#                 SELECT t.referral_code, t.username AS therapist_name
#                 FROM users u
#                 INNER JOIN Therapist t
#                     ON TRIM(u.referral_code) = TRIM(t.referral_code)
#                 WHERE u.user_id = :user_id
#             """),
#             {"user_id": user_id},
#         )
#         row = result.mappings().first()
#         return dict(row) if row else None

# def get_therapist_by_referral_code(referral_code):
#     """Verify if a referral code exists in the Therapist table."""
#     if not referral_code:
#         return None

#     with get_session() as session:
#         result = session.execute(
#             text("""
#                 SELECT referral_code, username AS therapist_name
#                 FROM Therapist
#                 WHERE TRIM(referral_code) = :referral_code
#             """),
#             {"referral_code": referral_code.strip()},
#         )
#         row = result.mappings().first()
#         return dict(row) if row else None