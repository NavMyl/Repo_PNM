from urllib.request import urlopen
import json


with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source=response.read()

data = json.loads(source)
usd_rates = dict()

for item in(data['list'] ['resources']):
    #print((item['resource']['fields']))
    del (item['resource']['classname'])
    names = item.get('resource').get('fields').get('name','NULL')
    price = item.get('resource').get('fields').get('price', 'NULL')
    usd_rates[names] = price
    if bool(item['resource']['fields']):
        del item['resource']['fields']['symbol']
        del item['resource']['fields']['ts']
    elif not bool(item['resource']['fields']):
        del item['resource']['fields']


print(usd_rates)

#print(data)

#for item2 in(data['list'] ['resources']):
 #   print(item2)
    #del (item2['classname'])

#data_formatted = json.dumps(data,indent=2)

#print(data_formatted)

usd_rates = dict()
print(bool(usd_rates))

count = 0
#for item2 in (data['list'] ['resources']):
    #print (item['resource']['fields']['name'])
    #print(item.get('resource').get('fields').get('name','NULL'))
    #names = item2.get('resource').get('fields').get('name')
    #price = item['resource']['fields']['price']
    #price = item.get('resource').get('fields').get('price', 'NULL')
    #print(price)
    #if names != 'NULL':
    #usd_rates[names]  = price
    #count+=1
print(bool(usd_rates))

with open('currency.json','w') as fw:
    json.dump(data,fw,indent = 2)

#print(usd_rates,count)
