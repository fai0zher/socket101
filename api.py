import requests 

for i in range(1,100,2):
    x = str(i)
    html = requests.get('http://10.10.114.96/api/'+x)
    if html.text =="{\"item_id\":"+x+",\"q\":\"Error. Key not valid!\"}":
        print("notfound"+x)
    else :
        print("Found"+x)
