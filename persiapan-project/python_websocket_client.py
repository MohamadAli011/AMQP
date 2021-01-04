import websocket
import time

# Buat object websocket
ws = websocket.WebSocket()
# Buat koneksi ke server
ws.connect("ws://localhost:8877")

while True:
	Kirim = "wooo"
	ws.send(Kirim)
	print "Sudah mengirim" ,Kirim
	data = ws.recv()
	print "dari server ",data
	
	
	time.sleep(3)
