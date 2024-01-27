from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

IPDATA_API_KEY = '6e712aba1626089ace36c9a89e31430fb267f14e0d16666f2b0ca4d4'  # Replace with your actual API key

def get_client_details_api(ip):
    # Make an API call to ipdata
    response = requests.get(f'https://api.ipdata.co/{ip}?api-key={IPDATA_API_KEY}')
    data = response.json()
    
    current_time = datetime.strptime(data['time_zone']['current_time'], '%Y-%m-%dT%H:%M:%S%z')
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S UTC%z')
    asn_name = data.get('asn', {}).get('name', '')
    
    client_details = {
        'ip': ip,
        'country': data.get('country_name', ''),
        'city': data.get('city', ''),
        'local-time': formatted_time,
        'isp': asn_name
    }

    return client_details
 
def get_client_details_web(ip):
    # Make an API call to ipdata
    response = requests.get(f'https://api.ipdata.co/{ip}?api-key={IPDATA_API_KEY}')
    data = response.json()
    return data

@app.route('/')
def index():
    client_ip = request.remote_addr
    client_details = get_client_details_web(client_ip)

    return render_template('index.html', client_details=client_details)

@app.route('/api')
def get_client_api():
    client_ip = request.remote_addr
    client_details = get_client_details_api(client_ip)

    return jsonify(client_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

