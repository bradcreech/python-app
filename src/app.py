from flask import Flask, jsonify
import socket
from datetime import datetime
app = Flask(__name__)

def get_hostname():
    return socket.gethostname()

def get_date_dd_mm_yyyy():
    return datetime.now().strftime("%d-%m-%Y")

@app.route('/api/v1/info')

def info():
    return jsonify({
        "time": get_date_dd_mm_yyyy(),
        "hostname": get_hostname(),
        "message": 'You are doing a good job human!! :-)',
        "deployed_on": 'kubernetes'
    })

@app.route('/api/v1/healthz')

def healthz():
    return jsonify({
        "status": "up"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
