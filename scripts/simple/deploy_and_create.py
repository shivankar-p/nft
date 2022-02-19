from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

def deploy_and_create():
    acc = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": acc})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": acc})
    tx.wait(1)
    print(
        f"You can view your nft at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}")
    return simple_collectible

def main():
    deploy_and_create()