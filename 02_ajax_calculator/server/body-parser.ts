import type { Connect } from "vite";

export function bodyParser(): Connect.NextHandleFunction {
    return (req: any, _res, next) => {
        // Only parse once
        if (req.body !== undefined) return next();

        // Only parse methods that can have a body
        if (!["POST", "PUT", "PATCH"].includes(req.method || "")) {
            return next();
        }

        let data = "";

        req.on("data", (chunk: any) => {
            data += chunk;
        });

        req.on("end", () => {
            try {
                // Only parse JSON
                if (req.headers["content-type"]?.includes("application/json")) {
                    req.body = data ? JSON.parse(data) : {};
                } else {
                    req.body = data;
                }
                next();
            } catch (err) {
                next(err);
            }
        });

        req.on("error", next);
    };
}