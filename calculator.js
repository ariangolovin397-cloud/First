function lock() { } // named function
const a = function () { } // anonymous function
const b = (p = 0) => { return p + 1 } // arrow function
const mop = b(5)
const c = p => ++p  // arrow function shorthand
const cop = c(3)

const http = require("http");

const form = `
        <form method="GET">
            <input type="text" name="num1" placeholder="Number 1"><br><br>
            <input type="text" name="num2" placeholder="Number 2"><br><br>

            <select name="action">
                <option value="">Select action</option>
                <option value="add">+</option>
                <option value="sub">-</option>
                <option value="mul">*</option>
                <option value="div">/</option>
            </select>
            <br><br>

            <button type="submit">Calculate</button>
        </form>
        <hr>
    `

http.createServer((req, res) => {
    const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
    console.log(parsedUrl);
    const { num1, num2, action } = parsedUrl.searchParams;

    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });

    if (num1 === undefined || num2 === undefined || action === undefined) {
        res.end(`
            ${form}
            <p style="color: red">All numbers and action must be defined</p>
        `);
        return;
    }

    res.end();
}).listen(3000, () => {
    console.log("http://localhost:3000");
});
