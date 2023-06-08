from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/viewBooks', methods=['GET'])
def viewBooks():
    conn = sqlite3.connect('library.sqlite')
    cursor = conn.cursor()

    get_books = """SELECT * FROM books"""
    cursor.execute(get_books)
    books = cursor.fetchall()
    return render_template('viewBooks.html', books_content=books)


@app.route('/addBooks', methods=['POST'])
def addBooks():
    conn = sqlite3.connect('library.sqlite')
    cursor = conn.cursor()
    request_data = request.get_json()
    sql_query = """INSERT INTO books (title, author, language) VALUES (?, ?, ?)"""

    if type(request_data) == list:
        for i in request_data:
            cursor.execute(sql_query, (i['title'], i['author'], i['language']))
    elif type(request_data) == dict:
        cursor.execute(sql_query, (request_data['title'], request_data['author'], request_data['language']))
    else:
        return "Unable to insert to table", 201

    conn.commit()
    return {"Message": "<a href='http://127.0.0.1:5000/'>Back to Home</a>"}


@app.route('/addBook', methods=['POST', 'GET'])
def addbook():
    if request.method == "GET":
        return render_template('addBook.html')
    elif request.method == 'POST':
        request_data = dict(request.form)
        conn = sqlite3.connect('library.sqlite')
        cursor = conn.cursor()
        insert_book = """INSERT INTO books (title, author, language) VALUES (?, ?, ?)"""
        cursor.execute(insert_book, (request_data['title'], request_data['author'], request_data['language']))
        conn.commit()
        return "Book Added", 200
    else:
        return "Whoops", 201


if __name__ == "__main__":
    app.run(debug=True)
