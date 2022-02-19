//SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";


contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokencounter;
    bytes32 public keyhash;
    uint256 fee;
    enum Breed{PUG, SHIBA_INU, ST_BERNARD}
    mapping(uint256=>Breed) public tokenIDtoBreed;
    mapping(bytes32=>address) public reqidtosender;
    event requestedcollectible(bytes32 indexed reqid, address requester);
    event requestedbreed(uint256 indexed tid, Breed breed);

    constructor(address _vrfcoordinator, address _linktoken,
        bytes32 _keyhash, uint256 _fee)
        VRFConsumerBase(_vrfcoordinator, _linktoken) 
        ERC721("Dogie", "DOG")    public {
            tokencounter = 0;
            keyhash = _keyhash;
            fee = _fee;
    }

    function createCollectible() public returns(bytes32)
    {
        bytes32 reqID = requestRandomness(keyhash, fee);
        reqidtosender[reqID] = msg.sender;
        emit requestedcollectible(reqID, msg.sender);
    }

    function fulfillRandomness(bytes32 reqID, uint256 random_no) internal override
    {
        Breed breed = Breed(random_no%3);
        uint256 newtokID = tokencounter;
        tokenIDtoBreed[newtokID] = breed; 
        emit requestedbreed(newtokID, breed);
        _safeMint(reqidtosender[reqID], newtokID);
        tokencounter += 1;
    }

    function settokenURI(string memory tokenURI, uint256 tokid) public{
        require(_isApprovedOrOwner(_msgSender(), tokid), "Not Owner");
        _setTokenURI(tokid, tokenURI);
    }

    
}