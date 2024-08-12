import bluetooth

#B8:27:EB:74:0E:EF 
bd_addr="DC:A6:32:98:11:A1"

port=2

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("client: 109511286, server: 109511041")
sock.close()

