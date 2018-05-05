# https://docs.python.org/2/library/xml.etree.elementtree.html
from xml.etree.ElementTree import parse

f = open('demo.xml')
tree = parse(f)
root = tree.getroot()
