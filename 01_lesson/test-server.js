const http = require("http");

console.log("this function");

const server = http.createServer(function (req, res) {
    if (req.url === '/') {
        return res.end("<h1>home page</h1>");
    }
    console.log(req.url);
    res.end("other path");
});
server.listen(3000, function () {
    console.log("server started");
});