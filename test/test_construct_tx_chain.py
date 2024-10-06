from muesliswap_transaction_chaining.construct_tx_chain import (
    main as construct_tx_chain,
)
from muesliswap_transaction_chaining.utils.network import (
    bf_context,
    ogmios_context,
)
from test.util import DEFAULT_TEST_CONFIG, LONG_CHAIN_TEST_CONFIG, wait_for_tx


def test_construct_tx_chain(use_blockfrost: bool):
    print("--- TESTING CONSTRUCT TX CHAIN DEFAULT ---")
    txs = construct_tx_chain(
        wallet=DEFAULT_TEST_CONFIG.tester_wallet_name,
        chain_length=DEFAULT_TEST_CONFIG.chain_length,
        use_blockfrost=use_blockfrost,
    )
    for tx in txs:
        wait_for_tx(tx=tx, context=ogmios_context)
    print("--- TEST SUCCEEDED ---\n\n")

    print("--- TESTING CONSTRUCT TX CHAIN LONG ---")
    txs = construct_tx_chain(
        wallet=LONG_CHAIN_TEST_CONFIG.tester_wallet_name,
        chain_length=LONG_CHAIN_TEST_CONFIG.chain_length,
        use_blockfrost=use_blockfrost,
    )
    for tx in txs:
        wait_for_tx(tx=tx, context=ogmios_context)
    print("--- TEST SUCCEEDED ---\n\n")


def construct_tx_chain_bf():
    test_construct_tx_chain(use_blockfrost=True)


def construct_tx_chain_ogmios():
    test_construct_tx_chain(use_blockfrost=False)


if __name__ == "__main__":
    construct_tx_chain_bf()
    construct_tx_chain_ogmios()
