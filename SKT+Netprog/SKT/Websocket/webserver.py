from flask import Flask, abort, request
import json

app = Flask(__name__)

list_node = [
		{"id":1, "suhu":30, "kelembaban":80},
		{"id":2, "suhu":28, "kelembaban":70}
	]

@app.route('/node', methods=['GET'])
def semua():
	return json.dumps(list_node)

@app.route('/node/<int:id_node>', methods=['GET'])
def satu(id_node):
	node = None
	# Iterasi data tiap node yang ada di list
	for n in list_node :
		if n["id"] == id_node:
			node = n
	# Cek apakah node tersebut ditemukan
	if node is None :
		abort(404)
	else :
		return json.dumps(node)
@app.route('/node/', methods=['POST'])
def tambah():
	id_tambah=list_node[-1]["id"]
	id = id_tambah+1
	suhu = request.form.get('suhu')
	kelembaban = request.form.get('kelembaban')

	node_tambah = {"id":id, "suhu": suhu, "kelembaban":kelembaban}
	list_node.append(node_tambah)
	node_cetak = json.dumps(list_node)
	return node_cetak
@app.route('/node/<int:id>', methods=['PUT'])
def edit(id):
    suhu = request.form.get('suhu')
    kelembaban = request.form.get('kelembaban')

    node = None
    index = 0
    for n in list_node:
        if n['id'] == id:
            node = n
            break
        index+1
    if node == None:
        abort(404)
        node['suhu']=suhu
        node['kelembaban']= kelembaban
        list_node[index] = node
        node_cetak = json.dumps(list_node)
        return node_cetak

app.run(debug=True, port=5566)