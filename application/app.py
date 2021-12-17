from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine

app = Flask(__name__)

# Connect to database
engine = create_engine(
    "mysql+pymysql://admin:KuraLabs#123@database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com:3306/final",
)


def list_tables():
    list_of_tables = engine.table_names()
    return list_of_tables


print(list_tables())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
