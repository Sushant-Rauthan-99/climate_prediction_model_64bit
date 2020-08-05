# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:53:28 2020

@author: nicpl
"""

import requests

url='http://localhost:5000/predict_api'
r=requests.post(url,json={'hr':13 ,'temp':20.6,'hmdy':83,'wdsp':2.6,'gust':5})

print(r.json())