from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    directory = '/var/log'
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run()

