import socket
import json
from twisted.web import resource, server
from twisted.internet import reactor
# Inisiasi socket TCP/IPv4
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi 3-way handshaking
#sock.connect( ('127.0.0.1', 8888) )

#Topik = {
#	"Topik" : "Olahraga",
#	"Data" : "Sepakbola"
#}
#text_json = json.dumps(Topik)

# Oleh receiver, data diterima dalam bentuk string JSON
# Untuk mengubah kembali menjadi dictionary, kita bisa
# memanfaatkan fungsi json.loads()

#Topik_kirim = json.loads(text_json)

#sock.send(text_json)
	# Cetak data
#print "Topik sudah terkirim"
# Protocol untuk handle HTTP


class Home(resource.Resource) :

    isLeaf = True

    def render_GET(self, request):
        return "Hello World"

    def render_POST(self, request):
        return "Anda mengirimkan "+str(request.args)

# Factory
site = server.Site(Home())

# Reactor
reactor.listenTCP(8888, site)
reactor.run()
