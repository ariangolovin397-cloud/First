import type { Connect } from "vite";
import fs from "fs";

type Data = { value?: string, timestamp: number };

export function apiPlugin(): Connect.NextHandleFunction {
    return (req: any, res, next) => {

        if (req.url === "/api/hello") {
            console.log("body", req.body);
            res.setHeader("Content-Type", "application/json");
            res.end(JSON.stringify({ message: "Hello from Vite API" }));
            return;
        }

        if (req.url === "/api/display" && req.method === "POST") {
            console.log("display value:", req.body.displayValue);

            const filePath = "data.json";
            let data: Data[] = [];

            if (fs.existsSync(filePath)) {
                const content = fs.readFileSync(filePath, "utf8");
                if (content.trim().length > 0) {
                    data = JSON.parse(content);
                    // data = JSON.parse('[{ a: "1" }]')
                }
            }
            const newValue: Data = {
                value: req.body.displayValue,
                timestamp: Date.now()
            };
            data.push(newValue);
            fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
            res.setHeader("Content-Type", "application/json");
            res.end(JSON.stringify({ message: "data saved" }));
            return;
        }

        next();
    };
}
