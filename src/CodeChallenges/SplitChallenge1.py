import pprint
# Output: 
# [
#    {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Lima'},
#    {'nombre': 'Luis', 'edad': 34, 'ciudad': 'Arequipa'},
#    ...
# ]

datos_crudos = [
    "nombre,edad,ciudad",
    "Ana,35,Lima",
    "Luis,34,Arequipa",
    "María,29,Lima",
    "Carlos,42,Cusco",
    "Valeria,19,Lima",
    "Jorge,55,Arequipa"
]
size = len(datos_crudos)
output = []
headers = []

for id, registro in enumerate(datos_crudos):
    if id==0:
        for i in registro.split(","):
#            output[i]=[]
            headers.append(i)
    else:
        record = {}
        for id, i in enumerate(registro.split(",")):
            record[headers[id]]=int(i) if headers[id]=="edad" else i
#            output[headers[id]].append(i)
        output.append(record)

output2 = []
for idx, record1 in enumerate(output):
    if record1["ciudad"]=="Lima" and record1["edad"]>=30:
        output2.append(record1)

pprint.pprint(output2)



