from brownie import network, exceptions
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_publish_account,
)
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_publish_account()
    fund_me = deploy_fund_me()
    tx = fund_me.fund({"from": account, "value": 1 * 10 ** 18})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 1 * 10 ** 18
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    badActor = get_account()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": badActor})
