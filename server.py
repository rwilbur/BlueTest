import bluetooth

serverMAC = "74:40:BB:47:5B:A8"
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((serverMAC, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)  # Echo back to client
except:
    print("Closing socket")
    client.close()
    s.close()
