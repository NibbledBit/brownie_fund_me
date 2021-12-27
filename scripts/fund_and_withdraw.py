from brownie import FundMe
from scripts.helpful_scripts import get_account, get_publish_account


def fund():
    fund_me = FundMe[-1]
    account = get_publish_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": 1 * 10 ** 18})


def withdraw():
    fund_me = FundMe[-1]
    account = get_publish_account()
    fund_me.withdraw({"from": account})


def currentPrice():
    fund_me = FundMe[-1]
    current_price = fund_me.getPrice()
    print(f"Current price is {current_price}")


def main():
    currentPrice()
    fund()
    withdraw()
