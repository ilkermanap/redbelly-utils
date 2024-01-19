import os
import sys
from redbelly import RedBellyRPC, Record
import traceback as tb


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            logger = Record()
            master = RedBellyRPC(db=logger)
            mynode = RedBellyRPC(url=sys.argv[1], db=logger)
            master.log()
            mynode.log()
            master.report(master.height)
            mynode.report(master.height)
            diff = master - mynode
            print("\n")
            if diff == 0:
                print(f"Your node is in sync with {master.url} at block number {master.height}")
            if diff > 0:
                print(f"Your node {mynode.url} is behind {diff} blocks from {master.url}" )
        except:
            print("An error happened. You can find details in error.log file.")
            with open("error.log", "a") as ferr:
                ferr.write(tb.format_exc())
                ferr.write("-"*80+"\n")
    else:
        print("""
Please provide your RPC url as parameter. Sample:

        python3 checksync.py https://myredbellynode.example.com:8545
        """)

