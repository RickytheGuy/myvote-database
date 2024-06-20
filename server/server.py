from flask import Flask, request
from sever_data import ServerData

app = Flask(__name__)

if __name__ == '__main__':
    sd = ServerData()

@app.route('/data', methods=['GET'])
def send_data():
    return "This is my message to Danielle!!!", 200

@app.route('/name_id', methods=['GET'])
def send_name_id():
    return sd.get_names(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
