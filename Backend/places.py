"""
Created on Sun Mar 19 2018
@author: Asel
"""

import googlemaps


class Places:
    gmaps = googlemaps.Client('AIzaSyDV3GWjqPrcqe2KQQCX1y2gwJBDveg_Fwc')
    geocode_result = gmaps.reverse_geocode("Parliament","english")

    print(geocode_result)
