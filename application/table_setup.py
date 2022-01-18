import SQLCRUD as sql

print("Creating tables")
sql.create_questions_table()
print("Created Questions table")
sql.create_choices_table()
print("Created Choices table")
sql.create_users_table()
print("Created Users table")
sql.create_session_table()
print("Created Session table")
print()
print("All tables created")
