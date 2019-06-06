import bluetooth

serverMAC = "B8:27:EB:E6:3B:B6"
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
