from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests

load_dotenv()

INFURA_API_KEY = os.getenv('INFURA_API_KEY')

app = Flask(__name__)
CORS(app)

@app.route("/address/balance/<address>")
def hello_world(address):
    try:
        request_url = "https://mainnet.infura.io/v3/"+INFURA_API_KEY
        print(request_url)
        app.logger.info('INITIATED to get balance for ethereum address: %s', address)
        response = requests.post(
            url=request_url, 
            json={"jsonrpc": "2.0", "id": 1, "method": "eth_getBalance", "params": [address, "latest"]},)
        if response.status_code == 200:
            app.logger.info('SUCCESSFULLY to get balance for ethereum address: %s', address)
            return response.json()['result']
    except Exception as e:
        app.logger.error('FAILURE retrieving balance for ethereum address: %s', address)
        app.logger.error(e)
        return "ERROR"