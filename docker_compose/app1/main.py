from flask import Flask, request, render_template_string
import zmq
import time

app = Flask(__name__)

# ZeroMQ 設定
context = zmq.Context()
socket = context.socket(zmq.REQ)
# 等待 receiver 啟動
time.sleep(2)
socket.connect("tcp://app2:5555")

HTML = """
<!doctype html>
<title>Sender</title>
<h1>Send a message</h1>
<form method=post>
  <input type=text name=message>
  <input type=submit value=Send>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        msg = request.form["message"]
        socket.send_string(msg)
        socket.recv_string()  # 等待 ack
        return f"Sent: {msg}<br><a href='/'>Back</a>"
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)