from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

cursor = db.cursor()

@app.route('/data', methods=['GET'])
def get_data():
    cursor.execute("SELECT * FROM test_table")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
