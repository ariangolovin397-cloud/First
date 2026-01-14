import { defineConfig } from "vite";
import { apiPlugin } from "./server/api";
import { bodyParser } from "./server/body-parser";

export default defineConfig({
    plugins: [
        {
            name: "body-parser",
            configureServer(server) {
                server.middlewares.use(bodyParser());
            }
        },
        {
            name: "api",
            configureServer(server) {
                server.middlewares.use(apiPlugin());
            }
        }
    ]
});