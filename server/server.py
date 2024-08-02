# Import flask class. Flask helps handle HTTP requests. In this case it routes the GET requests. It also, might be why you see who makes a request to the server and when since it aids in it.
from flask import Flask, request, make_response
# Calling the ServerData class in sever_data.py. This is the class that will be used to get the names and ids of the candidates.
from sever_data import ServerData

# Setting up flask app. Creating an instance of Flask class.
app = Flask(__name__)

# Kind confused but almost get it. Creating an instance of ServerData class by making an object of it, but only if the script is run directly. I think this is to make sure the data is loaded when the server is started. It blocks it to this local block though.
if __name__ == '__main__':
    sd = ServerData()

# @app.route binds this function to the url, so it will run if the url is searched from anywhere. It maps the url to here. If someone successfully sends a GET request to this server, ending /data, it will return an HTML message, "This is my message to Danielle!!!", and a status code of 200.
@app.route('/data', methods=['GET'])
def send_data():
    return "This is my message to Danielle!!!", 200


# Similar process, but more specific. If someone sends a GET request to the server, ending in /name_id, it will call an instance for a function that will return the names and ids of the candidates from the get_names function in the sd class. 
@app.route('/name_id', methods=['GET'])
def send_name_id():
    return sd.get_name_id(), 200

@app.route('/get_candidate', methods=['GET'])
def get_candidate():
    candidate_id = request.args.get('candidate_id', type=str)
    if candidate_id:
        data, code = sd.get_candidate(candidate_id)
        return data, code
    return f"Bad request. Please provide a candidate_id. '{candidate_id}' not understood", 400

# If the script is run directly, the server will run on the host on port 5000. THis is what makes it accessable from other devices on the same network.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
