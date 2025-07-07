from flask import Flask
import threading
import zmq

app = Flask(__name__)
latest_message = ""

def zmq_listener():
    global latest_message
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    while True:
        message = socket.recv_string()
        latest_message = message
        socket.send_string("Accecpted")

@app.route("/")
def show_message():
    return f"<h1>Received Message:</h1><p>{latest_message}</p>"

if __name__ == "__main__":
    thread = threading.Thread(target=zmq_listener, daemon=True)
    thread.start()
    app.run(host="0.0.0.0", port=5001)
