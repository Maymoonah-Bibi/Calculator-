from flask import Flask, request, redirect, url_for

import string
import random

app = Flask(__name__)
url_mapping = {}

def generating_short_url(length=5):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=length))
    return short_url

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>URL Shortener</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: 244, 244, 249;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 37px;
                border-radius: 9px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            form {
                margin-top: 21px;
            }
            label {
                display: block;
                margin-bottom: 10px;
                color: #555;
            }
            input[type="text"] {
                width: 100%;
                padding: 11px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                background: #007BFF;
                color: #fff;
                cursor: pointer;
                font-size: 16px;
            }
            input[type="submit"]:hover {
                background: #0056b3;
            }
            .result {
                margin-top: 20px;
            }
            .result a {
                color: #007BFF;
                text-decoration: none;
            }
            .result a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>URL Shortener</h1>
            <form action="/short_url" method="post">
                <label for="long_url">Enter your long URL:</label>
                <input type="text" id="long_url" name="long_url">
                <input type="submit" value="Shorten">
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/short_url', methods=['POST'])
def short_url():
    long_url = request.form['long_url']
    short_url = generating_short_url()
    url_mapping[short_url] = long_url
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>URL Shortener</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                background: #fff;
                padding: 41px;
                border-radius: 9px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .result {{
                margin-top: 21px;
            }}
            .result a {{
                color: #007BFF;
                text-decoration: none;
                font-size: 19px;
            }}
            .result a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>URL Shortener</h1>
            <div class="result">
                Short URL is: <a href="/{short_url}">/{short_url}</a>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return '<h1>URL not found</h1>'

if __name__ == '__main__':
    app.run(debug=True)
