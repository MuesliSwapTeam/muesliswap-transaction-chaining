import time
from dataclasses import dataclass


@dataclass
class TestConfig:
    tester_wallet_name: str
    chain_length: int


DEFAULT_TEST_CONFIG = TestConfig(
    tester_wallet_name="tester",
    chain_length=4,
)

LONG_CHAIN_TEST_CONFIG = TestConfig(
    tester_wallet_name="tester",
    chain_length=10,
)


def wait_for_tx(tx, context):
    if not context:
        return
    while not context.utxo_by_tx_id(tx.id.payload.hex(), 0):
        time.sleep(1)
        print("Waiting for transaction to be included in the blockchain")
