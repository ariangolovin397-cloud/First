// import * as fs from "fs";

// console.log("ok")
// const test = fs.readFileSync("server/api.ts", "utf-8");
// console.log("working", test);

// import sqlite3 from 'sqlite3'
// import { open } from 'sqlite'

// open({
//     filename: 'data.db',
//     driver: sqlite3.Database
// }).then((db) => {
//     return Promise.all([
//         db.exec(`
//             CREATE TABLE IF NOT EXISTS number_save (
//                 id INTEGER PRIMARY KEY,
//                 value TEXT DEFAULT NULL,
//                 timestamp INTEGER
//             )
//         `),
//         db.exec(`
//             INSERT INTO number_save (
//                 value,
//                 timestamp
//             ) VALUES (
//              "8",
//              29865
//              )
//         `),
//         db.all("SELECT id, value, timestamp FROM number_save").then(result => console.log("object", result))
//     ]);

// }).then(() => console.log("success"))
//     .catch(error => console.log("error don't work", error))