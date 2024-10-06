import os

import blockfrost
import ogmios

import pycardano
from pycardano import Network, BlockFrostChainContext
from pycardano.backend.ogmios_v6 import OgmiosV6ChainContext

ogmios_host = os.getenv("OGMIOS_API_HOST", "localhost")
ogmios_port = os.getenv("OGMIOS_API_PORT", "1338")
ogmios_protocol = os.getenv("OGMIOS_API_PROTOCOL", "ws")
ogmios_url = f"{ogmios_protocol}://{ogmios_host}:{ogmios_port}"

kupo_host = os.getenv("KUPO_API_HOST", None)
kupo_port = os.getenv("KUPO_API_PORT", "6669")
kupo_protocol = os.getenv("KUPO_API_PROTOCOL", "http")
kupo_url = (
    f"{kupo_protocol}://{kupo_host}:{kupo_port}" if kupo_host is not None else None
)

explorer = os.getenv("EXPLORER_TX", "https://preprod.cexplorer.io/tx")

network = Network.TESTNET

blockfrost_project_id = os.getenv("BLOCKFROST_PROJECT_ID")
blockfrost_client = blockfrost.BlockFrostApi(
    blockfrost_project_id,
    base_url=(
        blockfrost.ApiUrls.mainnet.value
        if network == Network.MAINNET
        else blockfrost.ApiUrls.preprod.value
    ),
)


# Load chain contexts
try:
    bf_context = BlockFrostChainContext(
        project_id=blockfrost_project_id, network=network
    )
except Exception as e:
    print("No blockfrost available")
    bf_context = None

try:
    ogmios_context = OgmiosV6ChainContext(
        host=ogmios_host,
        port=int(ogmios_port),
        secure=ogmios_protocol == "wss",
        network=network,
    )
except Exception as e:
    print("No ogmios available")
    ogmios_context = None


def show_tx(signed_tx: pycardano.Transaction):
    print(f"transaction id: {signed_tx.id}")
    if network == Network.TESTNET:
        print(f"Explorer: {explorer}/{signed_tx.id}\n")
    else:
        print(f"Explorer: https://cexplorer.io/tx/{signed_tx.id}")
        print(f"Explorer: https://cardanoscan.io/transaction/{signed_tx.id}\n")
