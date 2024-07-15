from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

WEBSITE_DIR = './website'
COMPONENTS_DIR = './components'

@app.route('/')
def home():
    return send_from_directory(WEBSITE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    website_path = os.path.join(WEBSITE_DIR, filename)
    if os.path.isfile(website_path):
        return send_from_directory(WEBSITE_DIR, filename)
    
    components_path = os.path.join(COMPONENTS_DIR, filename)
    if os.path.isfile(components_path):
        return send_from_directory(COMPONENTS_DIR, filename)

    return abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)