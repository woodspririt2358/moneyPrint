const MyToken = artifacts.require("LifeDeathCoin");

module.exports = function (deployer) {
    deployer.deploy(MyToken, 8000000000); // Initial supply of tokens
};
