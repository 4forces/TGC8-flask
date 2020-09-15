from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__) # tthis is a constructore Double underscore  ==> magical fxn in python

@app.route('/')
def hello():
    return render_template('home.template.html') # this is not standard html, but jinja2 language

@app.route('/author/<author_name>')
def search_by_author(author_name):
    return render_template('author_search.template.html', aname-author_name) # (template file name, variable name)


# "magic code" -- boilerplate -- # everything must go before this code
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), # this line starts the flask server
            port=int(os.environ.get('PORT')), # this step is to read OS Environment Variables
            debug=True)