import fire

from muesliswap_transaction_chaining.utils.network import (
    show_tx,
    bf_context,
    ogmios_context,
)
from muesliswap_transaction_chaining.utils import get_signing_info
from pycardano import (
    TransactionBuilder,
    TransactionOutput,
    UTxO,
    TransactionInput,
)

INIT_LVL = 3_000_000
LVL_STEP_PER_TX = 3_000_000


def main(
    wallet: str = "tester",
    chain_length: int = 4,
    use_blockfrost: bool = True,
):
    _, payment_skey, payment_address = get_signing_info(wallet)

    if chain_length < 1:
        return

    submitted_txs = []

    context = bf_context if use_blockfrost else ogmios_context

    builder = TransactionBuilder(context)
    builder.add_input_address(payment_address)
    prev_output_amount = INIT_LVL + LVL_STEP_PER_TX * (chain_length - 1)
    builder.add_output(
        TransactionOutput(
            address=payment_address,
            amount=prev_output_amount,
        )
    )
    signed_tx = builder.build_and_sign(
        signing_keys=[payment_skey],
        change_address=payment_address,
    )
    prev_tx_hash = signed_tx.id
    context.submit_tx(signed_tx)
    show_tx(signed_tx)
    submitted_txs.append(signed_tx)

    for i in range(chain_length - 1):
        builder = TransactionBuilder(context)
        builder.add_input(
            utxo=UTxO(
                input=TransactionInput(
                    transaction_id=prev_tx_hash,
                    index=0,
                ),
                output=TransactionOutput(
                    address=payment_address,
                    amount=prev_output_amount,
                ),
            )
        )
        prev_output_amount -= LVL_STEP_PER_TX
        builder.add_output(
            TransactionOutput(
                address=payment_address,
                amount=prev_output_amount,
            )
        )
        signed_tx = builder.build_and_sign(
            signing_keys=[payment_skey],
            change_address=payment_address,
        )
        context.submit_tx(signed_tx)
        show_tx(signed_tx)
        submitted_txs.append(signed_tx)
        prev_tx_hash = signed_tx.id

    return submitted_txs


if __name__ == "__main__":
    fire.Fire(main)
