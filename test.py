# -*- coding: utf-8 -*-
from flask import Flask, request
from markupsafe import escape
from datetime import datetime
import pandas as pd
import json


app = Flask(__name__)


@app.route('/')
def index():
     return 'Index Page'


@app.route('/test')
def test():
    summary  = request.args.get('summary', None)
    change  = request.args.get('change', None)

    if not summary or not change:
        return 'error'
    else:

        df = pd.read_csv("a_lvr_land_a.csv")
        fd = df[(df['鄉鎮市區'] == summary) & (df['建物型態'] == change)]

        fd.to_json (r'C:\Users\fredreload\Desktop\Export_DataFrame_part1.json', force_ascii=False)
        
        return 'done'

@app.route('/spark1')
def spark1():
    
    df = pd.read_csv("a_lvr_land_a.csv")
    fd = df[(df['主要用途'].str.contains('住家用')) & (df['建物型態'].str.contains('住宅大樓'))]
    
    

    events = []

    for index, row in fd.iterrows():
        even = {"district":row['鄉鎮市區'],"building_state":row['建物型態']}
        events.append(even)

    time_slots = {"date":datetime.today().strftime('%Y-%m-%d'),"events":events}

    city = {"city":"臺北市","time_slots":time_slots}
    
    with open('Export_DataFrame_part2.json', 'w', encoding='utf-8') as f:
        json.dump(city, f, ensure_ascii=False, indent=4)

    return 'done'

@app.route('/spark2')
def spark2():
    
    df = pd.read_csv("b_lvr_land_a.csv")
    fd = df[(df['主要用途'].str.contains('住家用')) & (df['建物型態'].str.contains('住宅大樓'))]
    
    

    events = []

    for index, row in fd.iterrows():
        even = {"district":row['鄉鎮市區'],"building_state":row['建物型態']}
        events.append(even)

    time_slots = {"date":datetime.today().strftime('%Y-%m-%d'),"events":events}

    city = {"city":"新北市","time_slots":time_slots}
    
    with open('Export_DataFrame_part3.json', 'w', encoding='utf-8') as f:
        json.dump(city, f, ensure_ascii=False, indent=4)

    return 'done'
    

if __name__ == '__main__':
     app.run(host='127.0.0.1', port=8000)
