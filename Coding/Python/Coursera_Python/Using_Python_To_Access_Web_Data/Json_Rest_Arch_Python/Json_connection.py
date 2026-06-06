import json
data = ''' {
"name" : "Ayush",
"age" : 56,
"phone" : {
"type" : "intl",
"number" : "93857676"
},
"email" : {
"hide" : "yes"
}
} '''
info =json.loads(data)
print('Name : ',info["name"] )
print('email : ',info["email"]["hide"] )
