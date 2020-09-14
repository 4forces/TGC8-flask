
# Steps to initialise flask backend/server

## Step 1 install flask: 

```
pip3 install flask
```

## Step 2: copy paste Boiler plate code from Paul below to working file:

```
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), # this step is to read OS Environment Variables
            debug=True)
```

# Images, JS, CSS etc,
Any kind of static files must be in a folder named `static` and in the same directory as `app.py` file.