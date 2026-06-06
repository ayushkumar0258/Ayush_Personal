import json
data = ''' [
{
"name":"ayush",
"age" : "45",
"phone" : "87887"
},
{
"name":"kumar",
"age" : "89",
"phone" : "8567887"
}
]'''

data1=json.loads(data)
for i in data1:
    print("name : ",i["name"])
    print("Age  : ",i["age"])
    print("phone : ",i["phone"])
