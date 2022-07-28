Moralis.Cloud.afterSave("EthTokenTransfer", async function (request) {
    const confirmed = request.object.get("confirmed");
    const tokenAddress = request.object.get("token_address");

    const HOST = "45.33.117.243";

    if (confirmed) {
      
        Moralis.Cloud.httpRequest({
            method: "GET",
            url: `${HOST}/swap/${tokenAddress}`
        })

    }
});