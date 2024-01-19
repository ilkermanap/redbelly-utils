# Redbelly Node Utilities

You can clone this repository using:

    git clone https://github.com/ilkermanap/redbelly-utils

## Check Sync Status
checksync.py first looks at the Redbelly rpc at https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545 and then find outs the block height in a given rpc.


    ilker@t440s:~/src/redbelly-utils$ python3 checksync.py https://example.mynodes.xyz:8545    
    --------------------------------------------------
    URL          :  https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545
    Block Height :  41852
    Sync Speed   :  0.0005401109176198041
    Time to sync :  0:00:00
    --------------------------------------------------
    URL          :  https://example.mynodes.xyz:8545
    Block Height :  9676
    Sync Speed   :  0.3640347936808723
    Time to sync :  1 day, 0:33:07.155729


    Your node https://example.mynodes.xyz:8545 is behind 32176 blocks from https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545
