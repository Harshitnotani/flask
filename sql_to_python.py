import mysql.connector

from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = '9829115035'

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='9829115035',
    database='e-commerce'
)

@app.route('/')
def sql_table():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM user;"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return render_template('sql-data.html', result=result)

if __name__ == '__main__':
    app.run()
