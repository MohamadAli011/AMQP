import json

a = 20
b = 10
c = 10.0

"""
d = a + b
print d

f = a + c
print f

x = "Hasil penjumlahannya adalah : "
print x+str(f)
"""

list_hari = [8,"Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
#print("hari :",list_hari[0])
#print list_hari[0]
#for i in list_hari:
#	print i

#for j in range(0,len(list_hari)):
#	print list_hari[j]

data = [220, 2, 10]
data1 = str(data[0])
data2 = str(data[1])
dataFul = data1+"\n"+data2
#print("datanya ",dataFul)
#print("hasilnya",dataFul)

volt = 220
tegangan = 10
energy = 2 /1000
VS = str(volt)
Ts = str(tegangan)
ES = str(energy)
full = VS+","+Ts+","+ES
#print("hasilnya fullnya", full)
foo = full[7:12]
#print("arusnya :",foo)

#foo="Teks ini akan dipecah\nke dalam 2 baris"
#print(foo)

#a =10
#uabh = str(a)
#print("hasil ubah :",uabh)

jso = {
    "name" : "lala",
    "date" : "12"
}
#data = json.loads(jso.read())
# cetak isi data JSON
#print(data)
json.dumps(jso)

#dict_ibukota = ["Indonesia":"Jakarta", "Thailand":"Bangkok", "India" : "New Delhi"]
#print dict_ibukota["Thailand"]

#for i in dict_ibukota:
#	print i+' '+dict_ibukota[i]

#try :
#	print dict_ibukota["Malaysia"]
#except KeyError:
#	print "Index tidak ditemukan di dictionary"

