import httplib, urllib, json
# cabeceras HTTP necesarias para realizar la conexion
headers = {
			"Host":"www.ecolegio.org",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.29.13 (KHTML, like Gecko) Version/6.0.4 Safari/536.29.13",
			"Content-Length":'0',
			"Accept": "application/json, text/javascript, */*; q=0.01",
			"Origin":"http://www.redabogacia.org",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"Referer":"http://www.redabogacia.org/mobile/censo/",
			"Accept-Language":"es-es",
			"Accept-Encoding":"gzip, deflate",
			"Connection":"keep-alive"
			}



print "---------------"
print "Appbogados v0.1"
print "---------------"

nombre = raw_input("Inserte su nombre: ")
apellidos = raw_input("Inserte sus apellidos: ")
# parametros de la consulta
params = urllib.urlencode({'action':'search','nombre':nombre,'apellidos':apellidos,'colegiado':'','colegio':'BALEARES','pagina':'1','nregistros':'-1'});
# abro conexion
httpServ = httplib.HTTPConnection("ecolegio.org",80)
print "Conectando...\n"
# me conecto al host
httpServ.connect()
# mando la peticion POST, muy raro lo de que en la URL vayan los parametros y tambien vayan por POST, una fusion GET + POST
httpServ.request("POST", "/ecensofront/ws/censoletrados?"+params,params,headers) 
# obtengo los resultados
response = httpServ.getresponse()
# cierro la conexion
httpServ.close()
# parseo el JSON devuelto de la peticion
data = json.loads(response.read())
# si me devuelve OK....
if(data['status'] == "OK"):
	# cojo los resultados de la peticion
	result = data['result'] 
	# miro que haya resultados
	if(len(result) > 0):
		# cojo el primer resultado
		lawyer = result[0]
		print "---------------"
		print "Datos obtenidos"
		print "---------------"
		# muestro todos los datos del abogado
		for item in lawyer:
			print item,":",lawyer[item]
	else:
		# no hay resultados
		print "NO SE HAN OBTENIDO DATOS"

else:
	#algo fue mal...
	print "ERROR EN LA CONSULTA"