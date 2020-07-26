import requests
import json

apiURL="http://192.168.39.220/zabbix/api_jsonrpc.php"
apiHeader={"Content-Type":"application/json"}

def loginZabbix(URL,Header):
    global zabbixToken
    logData = json.dumps({
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "centos",
            "password": "zabbix"
        },
        "id": 1,
        })
    token = requests.post(url = URL, data = logData, headers = Header)
    if 'error' in token.text:
        return "error"
    zabbixToken =  token.json()["result"]
    return zabbixToken

def getHostgroup(URL = apiURL, Header = apiHeader):
    getData = json.dumps({
        "jsonrpc":"2.0",
        "method":"hostgroup.get",
        "params":{
        "output": "extend",
        "filter": {
            "name": [
                "39 group",
                ]
            }
        },
        "auth":loginZabbix(URL, Header),
        "id":1,
    })
    print(getData)
    result = requests.post(url = URL, headers = Header, data = getData)
    print(result.text)    

def getAllHost(URL = apiURL, Header = apiHeader):
    getData = json.dumps({
        "jsonrpc":"2.0",
        "method":"hostgroup.get",
        "params":{
            "output":["hostgroup"]
        },
        "auth":loginZabbix(URL, Header),
        "id":1
    })
    result = requests.post(url = URL, headers = Header, data = getData)
    print(result.text)

getHostgroup()
getAllHost()
