from flask import Flask, render_template

import os
from supabase import create_client, Client

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    response: Client = create_client(url, key)

    data = response['data']  # Accessing the 'data' attribute

    print("Data:", data)
    count = len(data)

    return render_template('index.html', data=data, count=count)