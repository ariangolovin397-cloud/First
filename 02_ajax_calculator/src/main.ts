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

function onNumberClick(numm: string) {
    if (display.textContent === "0") {
        display.textContent = numm
    } else {
        display.textContent = display.textContent + numm;
    }
}

function onOperatorClick(operator: string) {
    firstNumber = Number(display.textContent);
    currentOperator = operator
    display.textContent = "0";
}

button_1.onclick = function () {
    onNumberClick("1")
};
button_2.onclick = function () {
    onNumberClick("2")
};
button_3.onclick = function () {
    onNumberClick("3")
};
button_4.onclick = function () {
    onNumberClick("4")
};
button_5.onclick = function () {
    onNumberClick("5")
};
button_6.onclick = function () {
    onNumberClick("6")
};
button_7.onclick = function () {
    onNumberClick("7")
};
button_8.onclick = function () {
    onNumberClick("8")
};
button_9.onclick = function () {
    onNumberClick("9")
};
button_0.onclick = function () {
    onNumberClick("0")
};
button_reiz.onclick = function () {
    onOperatorClick("*")
};
button_dal.onclick = function () {
    onOperatorClick("/")
};
button_del.onclick = function () {
    display.textContent = "0";
    firstNumber = null;
    currentOperator = null;
};
button_plus.onclick = function () {
    onOperatorClick("+")
};
button_minus.onclick = function () {
    onOperatorClick("-")
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