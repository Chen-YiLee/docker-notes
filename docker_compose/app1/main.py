from flask import Flask, request, render_template_string, redirect, url_for
import zmq
import time

app = Flask(__name__)

context = zmq.Context()
socket = context.socket(zmq.REQ)
time.sleep(2)
socket.connect("tcp://app2:5555")

HTML = """
<!doctype html>
<title>Sender</title>
<h1>Send a message</h1>
<form method=post>
  <input type=text name=message required>
  <input type=submit value=Send>
</form>
<p>{{ status }}</p>
"""

last_sent_message = ""

@app.route("/", methods=["GET", "POST"])
def send():
    global last_sent_message
    if request.method == "POST":
        msg = request.form["message"]
        socket.send_string(msg)
        socket.recv_string()
        last_sent_message = msg
        return redirect(url_for("send"))
    return render_template_string(HTML, status=f"Last sent: {last_sent_message}" if last_sent_message else "")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
