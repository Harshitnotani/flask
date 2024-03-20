from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = '9829115035'

@app.route('/')
def sql_table():
    flash('This is a flash message')
    return render_template('sql-data.html')

if __name__ == '__main__':
    app.run()
