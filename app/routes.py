from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from app import app
import hashlib

url = ''
client = MongoClient('mongodb://localhost:27017')
db = client.urls
host = 'http://localhost:80/'
table = db.links

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form.get('url')
        if table.find_one({'long-url': data}):
            result = table.find_one({'long-url': data})
            return render_template('index.html', short_url=host + result["hash"])
        elif data.split(':')[0] == 'https' or data.split(':')[0] == 'http':
            hash = hashlib.md5(data.encode()).hexdigest()
            post_data = {
                'long-url': data,
                'hash': hash[:5]
            }
            table.insert_one(post_data)
            return render_template('index.html', short_url=host + hash[:5])
        elif not data:
            return render_template('index.html')
        else:
            if table.find_one({'hash': data}):
                result = table.find_one({'hash': data})
                return render_template('index.html', short_url=result["long-url"])
            else:
                return render_template('index.html', 'Hash is not in the DB')
    return render_template('index.html')


@app.route('/<short_url>')
def redirect_short_url(short_url):
    print(short_url)
    result = table.find_one({'hash': short_url})
    print(result)
    long_url = result["long-url"]
    return redirect(long_url)

