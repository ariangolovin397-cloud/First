import './style.css'
// import { setupCounter } from './counter'
// import { setupAction } from './actions'

// const counter = document.querySelector<HTMLButtonElement>('#counter')
// if (counter) {
//     setupCounter(counter)
// }

// setupAction()
const display = document.getElementById("display")!;
display.textContent = "0";
const button_1 = document.getElementById("button_1")!;
const button_2 = document.getElementById("button_2")!;
const button_3 = document.getElementById("button_3")!;
const button_4 = document.getElementById("button_4")!;
const button_5 = document.getElementById("button_5")!;
const button_6 = document.getElementById("button_6")!;
const button_7 = document.getElementById("button_7")!;
const button_8 = document.getElementById("button_8")!;
const button_9 = document.getElementById("button_9")!;
const button_0 = document.getElementById("button_0")!;
const button_dal = document.getElementById("button_dal")!;
const button_reiz = document.getElementById("button_reiz")!;
const button_plus = document.getElementById("button_plus")!;
const button_minus = document.getElementById("button_minus")!;
const button_del = document.getElementById("button_del")!;
const button_vienad = document.getElementById("button_vienad")!;

let firstNumber: number | null = null;
let currentOperator: string | null = null;

button_1.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "1"
    } else {
        display.textContent = display.textContent + "1";
    }
};
button_2.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "2"
    } else {
        display.textContent = display.textContent + "2";
    }
};
button_3.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "3"
    } else {
        display.textContent = display.textContent + "3";
    }
};
button_4.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "4"
    } else {
        display.textContent = display.textContent + "4";
    }
};
button_5.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "5"
    } else {
        display.textContent = display.textContent + "5";
    }
};
button_6.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "6"
    } else {
        display.textContent = display.textContent + "6";
    }
};
button_7.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "7"
    } else {
        display.textContent = display.textContent + "7";
    }
};
button_8.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "8"
    } else {
        display.textContent = display.textContent + "8";
    }
};
button_9.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "9"
    } else {
        display.textContent = display.textContent + "9";
    }
};
button_0.onclick = function () {
    if (display.textContent === "0") {
        display.textContent = "0"
    } else {
        display.textContent = display.textContent + "0";
    }
};
button_reiz.onclick = function () {
    firstNumber = Number(display.textContent);
    currentOperator = "*";
    display.textContent = "0";
};
button_dal.onclick = function () {
    firstNumber = Number(display.textContent);
    currentOperator = "/";
    display.textContent = "0";
};
button_del.onclick = function () {
    display.textContent = "0";
    firstNumber = null;
    currentOperator = null;
};
button_plus.onclick = function () {
    firstNumber = Number(display.textContent);
    currentOperator = "+";
    display.textContent = "0";
};
button_minus.onclick = function () {
    firstNumber = Number(display.textContent);
    currentOperator = "-";
    display.textContent = "0";
};
button_vienad.onclick = function () {
    if (firstNumber === null || currentOperator === null) return;

    const secondNumber = Number(display.textContent);
    let result = 0;

    if (currentOperator === "+") {
        result = firstNumber + secondNumber;
    }
    if (currentOperator === "-") {
        result = firstNumber - secondNumber;
    }
    if (currentOperator === "*") {
        result = firstNumber * secondNumber;
    }
    if (currentOperator === "/") {
        result = secondNumber === 0 ? 0 : firstNumber / secondNumber;
    }

    display.textContent = result.toString();
    firstNumber = null;
    currentOperator = null;
};