from scripts.helpful_scripts import fund_with_link, get_account, OPENSEA_URL, get_contract, fund_with_link
from brownie import AdvancedCollectible, config, network

def deploy_and_create():
    acc = get_account()
    adv = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["fee"], {"from": acc}, 
        publish_source=config["networks"][network.show_active()].get("verify"))
    fund_with_link(adv.address)
    tx = adv.createCollectible({"from": acc})
    tx.wait(1)
    print("Done")
    #print(
    #   f"You can view your nft at {OPENSEA_URL.format(adv.address, adv.tokencounter() - 1)}")
    return adv

def main():
    deploy_and_create()