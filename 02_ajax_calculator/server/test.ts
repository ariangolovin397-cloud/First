import * as fs from "fs";

console.log("ok")
const test = fs.readFileSync("server/api.ts", "utf-8");
console.log("working", test);