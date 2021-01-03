import sqlite3


# get dictory by result
def dic_factory(cur, row):
    d = {}
    for ind, col in enumerate(cur.description):
        d[col[0]] = row[ind]
    return d


# CONNECT WITH DB
db = sqlite3.connect("test_db.sqlite")
db.row_factory = dic_factory
cursor = db.cursor()

# WORK WITH DB
# # create new table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE
#     )
# """)

# # insert to db
# cursor.execute("""
# INSERT INTO users(
#     name,
#     email
#     )
#     VALUES (
#         "Иванов Иван",
#         "ivanov@gmail.com"
#     )
# """)

# cursor.executescript("""
#     INSERT INTO users(name,email)VALUES ("Иванов 1", "ivanov1@gmail.com");
#     INSERT INTO users(name,email)VALUES ("Иванов 12", "ivanov2@gmail.com");
#     INSERT INTO users(name,email)VALUES ("Иванов 123", "ivanov3@gmail.com");
# """)
# users = [ [f'User {i}', f"user{i}@mail.com"] for i in range(10) ]
# cursor.executemany('INSERT INTO users(name,email)VALUES (?, ?)', users)
# db.commit()

# get from db
email = "user11@mail.com"
# cursor.execute(f"SELECT * FROM users WHERE email == '{email}'")
# cursor.execute("SELECT * FROM users WHERE email == :email OR name == :name", {'email': email, "name": "User 5"})
cursor.execute("SELECT * FROM users")
res = cursor.fetchall()
print(res)

for user in res:
    print(user['name'], user['email'])


# CLOSE DB
db.close()
