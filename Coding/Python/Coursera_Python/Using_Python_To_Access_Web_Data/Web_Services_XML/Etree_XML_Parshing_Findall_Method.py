import xml.etree.ElementTree as ET
data='''<stuff>
<users>
<user x="2">
<id>001</id>
<name>Ayush</name>
</user>
<user x="7">
<id>002</id>
<name>Kumar</name>
</user>
</users>
</stuff>'''
new_data=ET.fromstring(data)
#print(new_data.find('user').get('x'))
for i in new_data.findall('users/user'):
    print (i.find("id").text)

    print (i.get('x'))
for i in new_data.findall('users'):
    print (i.find("user").find("id").text)
    print (i.find("user").get('x'))
