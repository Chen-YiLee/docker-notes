from flask import Flask, jsonify, render_template_string
import threading
import zmq

app = Flask(__name__)
latest_message = "尚未收到訊息"

HTML = """
<!doctype html>
<html>
<head>
  <title>Receiver</title>
</head>
<body>
  <h1>Received Message:</h1>
  <p id="message">{{ message }}</p>

  <script>
    function fetchMessage() {
      fetch('/api/message')
        .then(response => response.json())
        .then(data => {
          document.getElementById('message').innerText = data.message;
        });
    }

    setInterval(fetchMessage, 2000);
  </script>
</body>
</html>
"""

def zmq_listener():
    global latest_message
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    while True:
        message = socket.recv_string()
        latest_message = message
        socket.send_string("Accepted")

@app.route("/")
def index():
    return render_template_string(HTML, message=latest_message)

@app.route("/api/message")
def api_message():
    return jsonify({"message": latest_message})

if __name__ == "__main__":
    threading.Thread(target=zmq_listener, daemon=True).start()
    app.run(host="0.0.0.0", port=5001)
