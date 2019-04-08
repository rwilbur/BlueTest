
import bluetooth

serverMAC = '74:40:BB:47:5B:A8'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMAC, port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(text)
s.close()
