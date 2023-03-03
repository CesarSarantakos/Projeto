import requests
import json

#Aqui é feita a chamada para a API. Não consegui integra-la no projeto, mas TODAS as informações utilizadas foram obtidas através dessa chamada.

iEstado = input("Informe a sigla do estado desejado:")
token = "ad473031a78b5fb08ee68bf39a0e5375"
listEstado = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?state=" + str(iEstado) +"&token=" + str(token)
iRESPOSTA = requests.request("GET",listEstado)
iRETORNO_REQ = json.loads(iRESPOSTA.text)
print(iRETORNO_REQ)
for iCHAVE in iRETORNO_REQ:
    iNAME = iCHAVE['name']
    iSTATE = iCHAVE['state']
    print(str(iNAME))