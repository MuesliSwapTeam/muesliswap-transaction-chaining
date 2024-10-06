MuesliSwap Transaction Chaining
------------------------------

This repository contains the code, documentation, and references to the implementation of MuesliSwap Transaction Chaining to Speed up Transactions on Cardano, funded in Fund 10 by Project Catalyst [1].

### Structure

- `muesliswap_transaction_chaining`: Contains code for submitting chained transaction via `pycardano` (as well as some utilities for setting up wallets, a chain context via blockfrost/ogmios, etc.)
- `test`: Contains tests for the `muesliswap_transaction_chaining` code.
- `keys`: Contains the keys used for testing the transaction chaining.
- `report`: Contains the detailed analysis of the required changes to implement transaction chaining for widespread open-source projects.

### Nami Wallet

The following PRs have been opened by MuesliSwapTeam regarding Mempool support (towards implementing transaction chaining) in Nami Wallet:
- Adding pending transactions to the transaction history: https://github.com/input-output-hk/nami/pull/885
- Adding pending transactions to the transaction building and getUTxO endpoint: https://github.com/input-output-hk/nami/pull/898

A fork of Nami Wallet that supports transaction chaining can be found here:
- https://github.com/MuesliSwapLabs/muesliswap-txchaining-nami

### Tx-Chaining Demo via `pycardano`

In order to submit a chain of transactions (all in the same block) via `pycardano`, please follow this setup:

1. Install `poetry`. Follow the official documentation [here](https://python-poetry.org/docs/#installing-with-pipx).
2. Clone this repo and `cd muesliswap-transaction-chaining`.
3. Run `poetry install` to install the dependencies.
4. Run `poetry shell` to activate the virtual environment.
5. Do `export BLOCKFROST_API_KEY=<your-blockfrost-api-key>` to set the Blockfrost (`preprod`) API key.
6. Make sure an `ogmios` instance is running on `localhost:1337` (or otherwise set `export OGMIOS_API_HOST=<your-ogmios-host` and `export OGMIOS_API_PORT=<your-ogmios-port>`).
7. Create a wallet with `python -m muesliswap_transaction_chaining.create_key_pair <your-wallet-name>`.
8. Fund the wallet (to be found in `keys/<your-wallet-name>.test_addr`) with some (test)ADA.
9. Run `python -m muesliswap_transaction_chaining.construct_tx_chain <your-wallet-name> <chain-length> <use-blockfrost>` to submit a chain of `<chain-length>` transactions from the `<your-wallet-name>` wallet. The <use-blockfrost> argument should be set to `True` or `False` if you want to use the `blockfrost` or `ogmios` backend, respectively.

### Demo Video

For a demo video of both the `pycardano` and Nami Wallet implementations, we refer [here](https://www.youtube.com/watch?v=oPAOpRYLC_Q).


[1]: [Open Transaction Chaining tooling to speed up Cardano dApps - By MuesliSwap](https://projectcatalyst.io/funds/10/f10-development-and-infrastructure/open-transaction-chaining-tooling-to-speed-up-cardano-dapps-by-muesliswap)
