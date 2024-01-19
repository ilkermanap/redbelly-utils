# Redbelly Node Utilities

You can clone this repository using:

    git clone https://github.com/ilkermanap/redbelly-utils

## Check Sync Status
checksync.py first looks at the Redbelly rpc at https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545 and then find outs the block height in a given rpc.

   ilker@t440s:~/src/redbelly-utils$ python3 checksync.py https://example.mynodes.xyz:8545
   Your node https://liglow.mynodes.xyz:8545 is behind 35191 blocks from https://rbn-gcp-australia-southeast1-a-0-b-v2.devnet.redbelly.network:8545


