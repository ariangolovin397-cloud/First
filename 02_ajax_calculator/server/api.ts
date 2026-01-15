import type { Connect } from "vite";
import sqlite3 from "sqlite3";
import { open } from "sqlite";

export function apiPlugin(): Connect.NextHandleFunction {
    return (req: any, res, next) => {
        if (req.url === "/api/display" && req.method === "POST") {

            const { displayValue } = req.body;
            const timestamp = Date.now();

            open({
                filename: "data.db",
                driver: sqlite3.Database
            }).then(db => {
                return Promise.all([
                    db.exec(`
                        CREATE TABLE IF NOT EXISTS number_save (
                            id INTEGER PRIMARY KEY,
                            value TEXT,
                            timestamp INTEGER
                        );
                    `),
                    db.exec(`
                        INSERT INTO number_save (value, timestamp)
                        VALUES ("${displayValue}", ${timestamp});
                    `),
                    db.all("SELECT id, value, timestamp FROM number_save")
                        .then(result => console.log("DB:", result))
                ]);
            }).then(() => {
                res.setHeader("Content-Type", "application/json");
                res.end(JSON.stringify({ message: "saved", value: displayValue }));
            });

            return;
        }

        next();
    };
}
