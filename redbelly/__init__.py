import os
from subprocess import PIPE, Popen
import time
import json
import sqlite3
from datetime import datetime, timedelta

devnet = "https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545"

testnet = "https://governors.testnet.redbelly.network"

template = """curl -k -s --location  BBBB --header 'Content-Type: application/json' --data '{             
  "jsonrpc":"2.0",
  "method":"eth_blockNumber",
  "params":[
    ],
  "id":1
}'
"""

class Record:
    def __init__(self):
        first = False
        if os.path.isfile(".redbellycheck.db") is False:
            first = True
        self.con = sqlite3.connect(".redbellycheck.db")
        if first:
            cursor = self.con.cursor()
            cursor.execute("CREATE TABLE redbelly(url, date, height)")
            self.con.commit()

    def height(self, url):
        cursor = self.con.cursor()
        rec = cursor.execute("SELECT max(height) from redbelly where url=?",(url,)).fetchone()
        return rec[0]
    
    def record(self, rpcobject):
        url = rpcobject.url
        date = datetime.now().timestamp()
        height = rpcobject.height
        cursor = self.con.cursor()
        records = cursor.execute("SELECT * FROM redbelly where url = ? order by date asc", (url,)).fetchall()
        if len(records) == 0:
            print(f"This is the first check for {url}. I will wait for 10 seconds and check again")
            cursor.execute("INSERT INTO redbelly values(?,?,?)", (url, date, height))
            self.con.commit()
            time.sleep(10)
            cursor = self.con.cursor()
            date = datetime.now().timestamp()
            height = rpcobject.lastBlock()
            cursor.execute("INSERT INTO redbelly values(?,?,?)", (url, date, height))
            self.con.commit()
        else:
            cursor.execute("INSERT INTO redbelly values(?,?,?)", (url, date, height))
            self.con.commit()

    def speed(self, url):
        cursor = self.con.cursor()
        records = cursor.execute("SELECT * FROM redbelly where url = ? order by date asc", (url,)).fetchall()
        if len(records) > 1:
            interval = records[-1][1] - records[0][1]
            numblock = records[-1][2] - records[0][2]
            return numblock / interval
        else:
            #Should not be in here
            return 0

    def timetosync(self,url, targetheight):
        urlspeed = self.speed(url)
        urlheight = self.height(url)
        diff = targetheight - urlheight
        try:
            synctime = diff / urlspeed
            return str(timedelta(seconds=synctime))
        except:
            return 0

        
class RedBellyRPC:
    def __init__(self, url=None, db=None):
        if url is None:
            self.url = testnet
        else:
            self.url = url        
        self.height = self.lastBlock()
        self.db = db
        
    def log(self):
        self.db.record(self)
        
    def lastBlock(self):
        command = template.replace("BBBB", self.url)
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        #TODO: Check the content of err for errors coming from curl
        content, err = process.communicate()
        return int(json.loads(content)['result'],0)

    def report(self, targetheight):
        print("-"*50)
        print("URL          : ", self.url)
        print("Block Height : ", self.height)
        print("Sync Speed   : ", self.db.speed(self.url))
        print("Time to sync : ", self.db.timetosync(self.url, targetheight))
        
    def __sub__(self, other):
        return self.height - other.height
