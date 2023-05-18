from brownie import accounts, config, TokenERC20, EasyToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")
token_name = "FINAIToken"
token_symbol = "FINAI"


def main():
    account = get_account()
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}
    )
