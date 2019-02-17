#!/usr/bin/python3
# -*- coding: utf-8 -*-
from geograpy.extraction import Extractor
import geograpy

import nltk


text = """Kadawatha Opposition Leader Mahinda Rajapaksa says that the whole  public administration has collapsed due to the constitution council’s arbitrary actions.
The Opposition Leader said so in response to a query a journalised raised  after a meeting held in Malabe and Meegamuwa"""
places = geograpy.get_place_context(text=text)
print(places.places)



print("****************************************************")



text6 = u"""Opposition Leader Mahinda Rajapaksa says that the whole public administration has collapsed due to the constitution council’s arbitrary actions.
The Opposition Leader said so in response to a query a journalised raised  after a meeting held.."""
e6 = Extractor(text=text6)
e6.find_entities()
#print(e6.places)

print("****************************************************")
