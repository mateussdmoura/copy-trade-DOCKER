Moralis.Cloud.beforeSave("EthTokenTransfer", async (request) => {

    let tokenAddress = request.object.get("token_address");

    let url = 45.33.117.243;

    Moralis.Cloud.httpRequest({
        method: "GET",
        url:  `${url}/swap/${tokenAddress}`
    })
});