# Redbelly Node Utilities

You can clone this repository using:

    git clone https://github.com/ilkermanap/redbelly-utils

## Check Sync Status
checksync.py first looks at the Redbelly rpc at https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545 and then find outs the block height in a given rpc.


    $ python checksync.py https://mynode.example.com
    --------------------------------------------------
    URL          :  https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545
    Block Height :  41850
    --------------------------------------------------
    URL          :  https://mynode.example.com:8545
    Block Height :  6992
    
    
    Your node https://mynode.example.com:8545 is behind 34858 blocks from https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545


