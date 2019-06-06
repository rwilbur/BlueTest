
import bluetooth

serverMAC = '80:C5:F2:DA:36:E0'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMAC, port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(text)
s.close()
