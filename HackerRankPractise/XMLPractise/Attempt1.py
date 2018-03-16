# Sources used: 
# http://effbot.org/zone/celementtree.htm
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://docs.python.org/2/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.append
# https://docs.python.org/2/library/xml.etree.elementtree.html#xml.etree.ElementTree.SubElement

import xml.etree.cElementTree as ElementTree

# Store file name
fileName = 'test[1][1].xml'
# Open file as read only and use Element Tree to store the XML contents in an Element object then close the file
file = open(fileName, "r")
tree = ElementTree.parse(file)
file.close()
# Get the root element (<note>)
elem = tree.getroot()

# Create subelement in child element at index 1 (so inside <b>)
# then set the attribute name
myName = ElementTree.SubElement(elem[1], 'c')
elem[1][2].set('name', 'Rob')

# Just some debug print to keep track of indexes and things	
for val in elem.iter('c'):
	print (val.attrib['name'])

# Once found I want to rename the attribute name, I do so by using set
print (elem[3].attrib['file']) # Debug
#elem[3].attrib['file'] = "FinalName.jpg" another way of writing it rather than using set, not sure which is best yet
elem[3].set('file', 'FinalName.jpg') # Debug
print (elem[3].attrib['file'])
		
#Debug stuff please ignore
#for val in elem.iter('body'):
	#print (val.attrib['file'])
#tree = ElementTree(file='test[1][1].xml')
#rootEl = tree.getroot()
#html = Element("body file")
#ElementTree(elem).write(file2)
#body = SubElement(rootEl, "body file")

# Adding b, required by python3 to flag file open as binary, see: 
# https://stackoverflow.com/questions/47027254/typeerror-write-argument-must-be-str-not-bytes-python-3-vs-python-2
file = open(fileName, "wb")
tree.write(file)
file.close()