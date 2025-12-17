// function lock() { } // named function
// const a = function () { } // anonymous function
// const b = (p = 0) => { return p + 1 } // arrow function
// const mop = b(5)
// const c = p => ++p  // arrow function shorthand
// const cop = c(3)
// 1
// const option = action === "add" ? "selected" : ""; // ternary operator

// clasic way to define condicional value
// let selected;
// if (action === "add") {
//     selected = "selected";
// } else {
//     selected = "";
// } 

// `
//         <form method="GET">
//         <input type="text" name="num1" placeholder="Number 1" value=""><br><br>
//         <input type="text" name="num2" placeholder="Number 2" value=""><br><br>

//         <select name="action">
//             <option value="">Select action</option>
//             <option value="add" ${action === "add" ? "selected" : ""}>+</option>
//             <option value="sub" ${action === "sub" ? "selected" : ""}>-</option>
//             <option value="mul" ${action === "mul" ? "selected" : ""}>*</option>
//             <option value="div" ${action === "div" ? "selected" : ""}>/</option>
//         </select>
//         <br><br>

//         <button type="submit">Calculate</button>
//     </form>
//     <hr>
//     `; //template literal
// const select = "<select name=\"action\">" +
//     "<option value=\"\">Select action</option>" +
//     "<option value=\"add" + action === "add" ? "selected" : "" + ">+</option>" +
//         "<option value=\"sub" + action === "sub" ? "selected" : "" + ">-</option>" +
//             "<option value=\"mul" + action === "mul" ? "selected" : "" + ">*</option>" +
//                 "<option value=\"div" + action === "div" ? "selected" : "" + ">/</option>" +
// "</select>"; // clasic string

// const fs = require("fs");


// function fnWithCallback(funkcijaObratnogoVizova) {
//     // console.log("argument type", typeof callback);
//     // const result = callback("capuchino", 2, "croissant");// передаём capuchino в качестве аргумента callback
//     // console.log("result:", result);
//     fs.readdir("asdasdadadas",null,funkcijaObratnogoVizova);
//     // let err = null;
//     // // assigne if there's an error
//     // let files = undefined;
//     // // set to array of strings if file list is avalible
//     // callback(err,files);
// };
// const result = "cocacola";
// const cb = function (err,fl) {
//     console.log("callback message:", err, fl);
//     // const obj = { coffe: fl };
//     // return `${obj.coffe} coffe`;
// };
// const ab = function (drink, spoonsOfSugar, snacks) {
//     const a = { drink, spoonsOfSugar, snacks };
//     return a;
// };

// fnWithCallback(cb);
// fnWithCallback(ab);

const http = require("http");

const message = `<p style="color: red">All numbers and action must be defined</p>`;

const server = http.createServer(function (req, res) {
    const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
    const num1 = parsedUrl.searchParams.get('num1');
    const num2 = parsedUrl.searchParams.get('num2');
    const action = parsedUrl.searchParams.get('action');

    const form = `
            <form method="GET">
            <input type="text" name="num1" placeholder="Number 1" value="${num1 ?? ''}"><br><br>
            <input type="text" name="num2" placeholder="Number 2" value="${num2 ?? ''}"><br><br>
    
            <select name="action">
                <option value="">Select action</option>
                <option value="add" ${action === "add" ? "selected" : ""}>+</option>
                <option value="sub" ${action === "sub" ? "selected" : ""}>-</option>
                <option value="mul" ${action === "mul" ? "selected" : ""}>*</option>
                <option value="div" ${action === "div" ? "selected" : ""}>/</option>
            </select>
            <br><br>
    
            <button type="submit">Calculate</button>
        </form>
        <hr>
        `;

    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });

    if (parsedUrl.pathname === '/') {
        // console.log("url output", req.url);
        console.log(parsedUrl);
        console.log({ num1, num2, action });
        // console.log("Test", !num1 || !num2 || !action);
    } else {
        res.end();
        return;
    }

    if (!num1 || !num2 || !action) {

        const withMessage = `
            ${form}
            ${message}
            `;
        const isWithMessage = num1 === null && num2 === null && action === null;

        const response = isWithMessage ? form : withMessage;

        res.end(response);
        return;
    }

    const a = Number(num1);
    const b = Number(num2);

    let result;

    switch (action) {
        case "add":
            result = a + b;
            break;
        case "sub":
            result = a - b;
            break;
        case "mul":
            result = a * b;
            break;
        case "div":
            if (b === 0) {
                result = "Division by zero!";
            } else {
                result = a / b;
            }
            break;
    }
    res.end(`
        ${form}
        Result: ${result}
    `);
});

server.listen(3000, () => {
    console.log("http://localhost:3000");
});
