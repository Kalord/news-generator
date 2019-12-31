# -*- coding: utf-8 -*-
from lxml import etree

"""
    XML Parser
    @package xml.Parser
"""
class Parser:
    @staticmethod
    def run(XMLString):
        #Корень XML документа
        root = etree.fromstring(XMLString)

        data = []

        #Разбор
        for item in root.getchildren():
            for element in item.getchildren():
                new = {}
                for content in element.getchildren():
                    new[content.tag] = content.text
                data.append(new)
        
        return data
            