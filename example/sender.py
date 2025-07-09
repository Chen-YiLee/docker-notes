import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5555")

message = "這是一筆資料"
socket.send_string(message)