import json


people_string = '''
{
    "people": [
        {
            "name" : "John Smith",
            "phone" : "615-330-5655",
            "emails" : ["jsmith@abc.net", "jonsmi@gmail.com"],
            "has_license" : false
        },
        {
            "name" : "Jack Dorsey",
            "phone" : "714-330-5655",
            "emails" : null,
            "has_license" : true
        }
    ]
}
'''


data = json.loads(people_string)

print (data)
print (type(data))


for p in data['people']:
    print( p['name'])

for person in data['people']:
    #print(person)
    #print(person['name']) #to get the name values
    del (person['phone'])  ## To Delete phone from the list

new_string = json.dumps(data,indent = 3,sort_keys=True)
print(new_string)