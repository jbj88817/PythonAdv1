from xml.etree.ElementTree import Element, ElementTree, tostring

e = Element('data')
print e.tag

e.set('name', 'abc')
print tostring(e)
e.text = '123'
print tostring(e)

e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)
print tostring(e2)
e.text = None
e.append(e2)
print tostring(e)

et = ElementTree(e)
et.write('demo1.xml')
