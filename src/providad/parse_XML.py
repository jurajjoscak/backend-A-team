#! /usr/bin/python3
import xml.etree.ElementTree as ET
import sys


class XmlProductParser:
	def __init__(self, xmlLink):
		self.xmlLink = xmlLink
	def parse_xml(self):

		tree = ET.parse(self.xmlLink)
		root = tree.getroot()
		root=root[0]
		#pole
		i=0
		array=[]

		#zapis do pola
		for item in root.findall('item'):

			array.append([])

			j=0
			if item.find('image_link') != None:
				imageLink=(item.find('image_link').text)
				array[i].append({})
				array[i][j] = {'type' : "mainImage", 'url' : imageLink}
				j+=1
			if item.find('title') != None:	
				title=(item.find('title').text)
				array[i].append({})
				array[i][j] = {'type' : "mainText", 'value' : title}
				j+=1
			if item.find('description') != None:
				description=(item.find('description').text)
				array[i].append({})
				array[i][j] = {'type' : "description", 'value' : description}
				j+=1
			if item.find('price') != None:
				price=(item.find('price').text)
				array[i].append({})
				array[i][j] = {'type' : "price", 'value' : price}
				j+=1
			if item.find('category1') != None:
				category=(item.find('category1').text)
				array[i].append({})
				array[i][j] = {'type' : "category", 'value' : category}
				j+=1
			for altImage in item.findall('image_alt'):
				array[i].append({})
				array[i][j] = {'type' : "simpleImage", 'url' : altImage.text}
				j+=1
			for simpleText in item.findall('simple_text'):
				array[i].append({})
				array[i][j] = {'type' : "simpleText", 'value' : simpleText.text}
				j+=1
			i+=1

		return array