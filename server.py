from flask import Flask, render_template

import os
from supabase import create_client, Client

app = Flask(__name__)

@app.route('/')
def hello():

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table('Test').select("*").execute()

    print(response)

    return render_template('index.html', data=response)