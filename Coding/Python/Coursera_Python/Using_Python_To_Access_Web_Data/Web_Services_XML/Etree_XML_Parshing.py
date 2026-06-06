import xml.etree.ElementTree as ET
data= '''<person>
<name>Ayush</name>
<age>32</age>
<phone>898777</phone>
<email hide='yes' >ayush@example.com</email>
</person>'''

tree=ET.fromstring(data)
print('Name:', tree.find('name').text) #### .text is used to get the text content of the element
print('Age:', tree.find('age').text)
print('Phone:', tree.find('phone').text)
print('Email:', tree.find('email').get('hide')) #### .get() is used to get the value of an attribute of the element, in this case 'hide' attribute of 'email' element.
print('Email:', tree.find('email').text) #### to get the text content of the 'email' element, which is 'ayush@example.com'
