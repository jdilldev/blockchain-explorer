import json
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests
from web3 import Web3

load_dotenv()

INFURA_API_KEY = os.getenv('INFURA_API_KEY')

app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,)

CORS(app)
w3 = Web3(Web3.IPCProvider())

def _convert_hex_to_decimal(hex:str):
    wei_as_number = int(hex, 16) # convert hexstring to integer
    return w3.from_wei(wei_as_number,'ether') # convert wei to ether

@app.route("/address/balance/<address>")
def get_balance(address:str):
    try:
        if address is not None:
            request_url = "https://mainnet.infura.io/v3/"+INFURA_API_KEY
            json_body = {"jsonrpc": "2.0", "id": 1, "method": "eth_getBalance", "params": [address, "latest"]}
            # TODO some validation on the address before making the API call
            app.logger.info('INITIATED to get balance for ethereum address: %s', address)
            response = requests.post(
                url=request_url, 
                json=json_body
            )
            if response.status_code == 200:
                app.logger.info('SUCCESS retrieving balance for ethereum address: %s', address)
                balance = _convert_hex_to_decimal(response.json()['result'])
                return json.dumps({'balance': float(balance)}) # convert Decimal to float so it can be jsonified
        else:
            return "Invalid input"
    except Exception as e:
        app.logger.error('FAILURE retrieving balance for ethereum address: %s', address)
        app.logger.error(e)
        return "ERROR"
    

@app.route("/")
def hi():
    return "Hello"