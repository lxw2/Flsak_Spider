function ale() {

        alert(" msg ..");
        let req = new XMLHttpRequest();
        req.open('GET', document.location, false);
        req.send(null);
        console.log(req)
        let content=req.getResponseHeader('content-type')
        console.log(content)
        var headers = req.getAllResponseHeaders().toLowerCase();
        console.log(headers);
    }