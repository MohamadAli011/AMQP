<head>
	<title>Simple Websocket Client</title>
	<script type="text/javascript">
		ws = new WebSocket('ws://localhost:8877/');

		ws.onmessage = function(evt){
			//alert(evt.data);
			setHasil(evt.data);
		};

		function kirimData(){
			nama = document.getElementById('nama');
			//alert(nama.value);
			ws.send(nama.value);
		}

		function setHasil(data){
			hasil = document.getElementById('hasil');
			hasil.innerHTML = data
		}
	</script>
</head>

<body>
	<input type="text" name="nama" id="nama">
	<button onclick="kirimData()">Kirim</button>
	<div>
	Hasil : 
	<div id="hasil" nama="hasil" style="display: inline-block;">
		-
	</div>

	</div>
</body>
