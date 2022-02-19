from scripts.helpful_scripts import (LOCAL_BLOCKCHAIN_ENVIRONMENTS,
        get_account)
from brownie import network
from scripts.simple.deploy_and_create import deploy_and_create
import pytest
def test_can_create():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    col = deploy_and_create()
    assert col.ownerOf(0) == get_account()