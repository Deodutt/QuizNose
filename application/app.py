from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql.sqltypes import VARCHAR

app = Flask(__name__)
metadata = MetaData()
# db = SQLAlchemy()


# Connect to database
engine = create_engine(
    "mysql+pymysql://admin:KuraLabs#123@database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com:3306/final",
)


def list_tables():
    list_of_tables = engine.table_names()
    return list_of_tables


def create_table():
    # checking the table list
    list_of_tables = engine.table_names()
    table_name = "user_info"

    if table_name in list_of_tables:
        print(f"The table '{table_name}' is inside the database!")

    else:
        user_info = Table(
            table_name,
            metadata,
            Column("username", VARCHAR(20), primary_key=True),
            Column("password", VARCHAR(20)),
            Column("email", VARCHAR(20)),
        )
        metadata.create_all(engine)
        print(f"The table '{table_name}' was successfully created!")
    return


# def delete_table():
#     # checking the table list
#     list_of_tables = engine.table_names()
#     table_name = "users"

#     if table_name in list_of_tables:
#         print(f"The table '{table_name}'  was deleted from the database!")

#     else:
#         print(f"The table '{table_name}'  is not inside the database!")

#     return


print(f"Original List: {list_tables()}\n")
create_table()
print(f"New List: {list_tables()}\n")
# delete_table()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
