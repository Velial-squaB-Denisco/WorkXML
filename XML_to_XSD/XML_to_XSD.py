from xmltoxsd import XSDGenerator

generator = XSDGenerator()
xsd_schema = generator.generate_xsd("example.xml") #Замените на свой файл

with open("your.xsd", "w") as f: #Замените на свой файл
    f.write(xsd_schema)