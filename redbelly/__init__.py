import os
import json


testnet = "https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545"

template = """curl -k -s --location  BBBB --header 'Content-Type: application/json' --data '{             
  "jsonrpc":"2.0",
  "method":"eth_blockNumber",
  "params":[
    ],
  "id":1
}'
"""

class RedBellyRPC:
    def __init__(self, url=None):
        if url is None:
            self.url = testnet
        else:
            self.url = url
        self.height = self.lastBlock()

    def lastBlock(self):
        command = template.replace("BBBB", self.url)
        process = os.popen(command)
        content = process.read()
        return int(json.loads(content)['result'],0)

    def report(self):
        print("-"*50)
        print("URL          : ", self.url)
        print("Block Height : ", self.height)

    def __sub__(self, other):
        return self.height - other.height
