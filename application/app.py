from flask import Flask, request, jsonify, render_template
import MySQLdb

app = Flask(__name__)

# connection
db = MySQLdb.connect(
    host="database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com",  # your host, usually localhost
    user="admin",  # your username
    passwd="KuraLabs#123",  # your password
    db="final",
)  # name of the data base


def list_tables(db_table):
    cur = db.cursor()
    cur.execute(f"SHOW TABLES FROM {db_table};")
    result = cur.fetchall()
    return result


def create_table(new_name):
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {new_name} (quiz_id VARCHAR(20) NOT NULL, question_number INT NOT NULL, choice_a TEXT NOT NULL, choice_b TEXT NOT NULL, choice_c TEXT NOT NULL, choice_d TEXT NOT NULL);"
    )

    result = cur.fetchall()
    return print(f"The table '{new_name}' was successfully created!")


def delete_table(target):
    cur = db.cursor()
    cur.execute(f"DROP TABLE {target};")
    result = cur.fetchall()
    return print(f"The table '{target}' was successfully deleted!")


# This list all the tables inside the database final
print(f"Original List: {list_tables(db_table = 'final')}\n")

# This creates a table named <var>
create_table(new_name="testing_purpose")
print(f"New List: {list_tables(db_table = 'final')}\n")

# This deletes a table named <var>
delete_table(target="testing_purpose")
print(f"New List: {list_tables(db_table = 'final')}\n")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
