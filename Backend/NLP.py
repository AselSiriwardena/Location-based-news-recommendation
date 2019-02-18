#!/usr/bin/python3
# -*- coding: utf-8 -*-
from geograpy.extraction import Extractor
import geograpy
from geotext import GeoText

import nltk
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
#
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# sentence = "I am from Kadawatha"
# places = GeoText(sentence)
# print (places.cities)

text = "Kadawatha Opposition Leader Mahinda Rajapaksa says that the whole  public administration has collapsed due to the constitution council’s arbitrary actions. " \
       "The Opposition Leader said so in response to a query a journalised raised  after a meeting held in Malabe and Meegamuwa"
places = geograpy.get_place_context(text=text)
print(places.places)
# url = 'http://www.bbc.com/news/world-europe-26919928'
# places = geograpy.get_place_context(url=url)
# print(places.cities)


print("****************************************************")


#
# text6 = u"""Opposition Leader Mahinda Rajapaksa says that the whole public administration has collapsed due to the constitution council’s arbitrary actions.
# The Opposition Leader said so in response to a query a journalised raised  after a meeting held.."""
# e6 = Extractor(text=text6)
# e6.find_entities()
#print(e6.places)

print("****************************************************")
