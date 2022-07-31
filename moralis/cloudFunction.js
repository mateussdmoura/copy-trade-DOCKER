Moralis.Cloud.afterSave("EthTokenTransfer", async function (request) {
    const confirmed = request.object.get("confirmed");
    const txHash = request.object.get("transaction_hash");

    const HOST = "45.33.117.243";

    if (confirmed) {
      
        Moralis.Cloud.httpRequest({
            method: "GET",
            url: `${HOST}/swap/txHash/${txHash}`
        })

    }
});