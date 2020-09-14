from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.template.html')

@app.route('/about-me')
def about_me():
    return render_template('about.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), # this step is to read OS Environment Variables
            debug=True)