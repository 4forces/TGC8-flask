from flask import Flask, render_template, request, redirect, url_for

import json
import os
import random

app = Flask(__name__)

database = []
with open('data.json', 'r') as fpt:
    database = json.load(fpt)

@app.route("/")
def home():
    return "Home page"

@app.route("/books")
def show_books():
    return render_template('books.template.html', database=database)

@app.route('/books/create')
def create_book():
    return render_template('create_book.template.html')

@app.route('/books/create', methods=["POST"])
def process_create_book():
    new_book = {
        "id": random.randint(10000,99999),
        "title": request.form.get("title"),
        "author": request.form.get("author")
        }
    database.append(new_book)

    with open('data.json', 'w') as fp:
        json.dump(database, fp)

    # return "form received"

    return redirect(url_for('show_books'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
