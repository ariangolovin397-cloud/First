function calculate(expression: string): number {
    const numbers: number[] = [];
    const operators: string[] = [];

    let current = "";

    for (const char of expression) {
        if ("0123456789.".includes(char)) {
            current += char;
        } else {
            numbers.push(Number(current));
            operators.push(char);
            current = "";
        }
    }
    numbers.push(Number(current));

    for (let i = 0; i < operators.length; i++) {
        if (operators[i] === "*" || operators[i] === "/") {
            const result =
                operators[i] === "*"
                    ? numbers[i] * numbers[i + 1]
                    : numbers[i] / numbers[i + 1];

            numbers.splice(i, 2, result);
            operators.splice(i, 1);
            i--;
        }
    }

    let result = numbers[0];

    for (let i = 0; i < operators.length; i++) {
        if (operators[i] === "+") result += numbers[i + 1];
        if (operators[i] === "-") result -= numbers[i + 1];
    }

    return result;

};

export function setupAction() {
    const display = document.getElementById("display") as HTMLDivElement;
    const buttons = document.querySelectorAll<HTMLButtonElement>(".button");

    let expression = "";

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const value = button.textContent!;

            if (value === "C") {
                // expression = expression.slice(0, -1);
                // if (expression === "") expression = "0";
                display.textContent = "0";
                return;
            }
            if (value === "=") {
                try {
                    expression = calculate(expression).toString();
                    display.textContent = expression;
                } catch {
                    display.textContent = "Error";
                    expression = "";
                }
                return;
            }

            if (expression === "0") {
                expression = value;
            } else {
                expression += value;
            }

            display.textContent = expression;
        });
    });

    display.textContent = "0";


}