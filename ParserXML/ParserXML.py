import xml.etree.ElementTree as ET

def parse_element(element, file, level=0):

    indent = "  " * level
    tag = element.tag
    attrib = element.attrib
    text = element.text.strip() if element.text else ""

    file.write(f"{indent}Tag: {tag}\n")
    if attrib:
        file.write(f"{indent}  Attributes: {attrib}\n")
    if text:
        file.write(f"{indent}  Text: {text}\n")

    # Рекурсивно обрабатываем дочерние элементы
    for child in element:
        parse_element(child, file, level + 1)

def parse_xml(input_file_path, output_file_path):

    tree = ET.parse(input_file_path)
    root = tree.getroot()

    with open(output_file_path, 'w', encoding='utf-8') as file:
        parse_element(root, file)

input_file_path = 'example.xml'  # Укажите путь к вашему XML-файлу
output_file_path = 'parsed_output.txt'  # Путь к выходному файлу
parse_xml(input_file_path, output_file_path)