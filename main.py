import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

def get_earthquake_data():
    url = 'http://www.koeri.boun.edu.tr/scripts/lst1.asp'
    response = requests.get(url)
    data = response.content.decode('windows-1254')  # Kandilli Rasathanesi Türkçe karakter setiyle kodlanmıştır.
    return data

def parse_earthquake_data(data):
    lines = data.split('\n')
    earthquake_data = []
    for line in lines[6:-2]:  
        parts = line.strip().split()
        if len(parts) == 13:  
            date = parts[0]
            time = parts[1]
            latitude = float(parts[2])
            longitude = float(parts[3])
            depth = float(parts[4])
            magnitude = float(parts[11])
            location = ' '.join(parts[12:])
            earthquake_data.append({
                'date': date,
                'time': time,
                'latitude': latitude,
                'longitude': longitude,
                'depth': depth,
                'magnitude': magnitude,
                'location': location
            })
    return earthquake_data

@app.route('/earthquakes')
def get_earthquakes():
    data = get_earthquake_data()
    earthquake_data = parse_earthquake_data(data)
    return jsonify(earthquake_data)

if __name__ == '__main__':
    app.run()

#mustafamete.com.tr / admin@mustafamete.com.tr
