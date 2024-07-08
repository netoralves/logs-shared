from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        filename = request.form['filename']
        response = requests.get(f'http://serverb.lab.example.com/download/{filename}')
        if response.status_code == 200:
            with open(f'/tmp/{filename}', 'wb') as f:
                f.write(response.content)
            return redirect(url_for('download_file', filename=filename))
        else:
            return "File not found", 404
    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('/tmp', filename)

if __name__ == '__main__':
    app.run()

