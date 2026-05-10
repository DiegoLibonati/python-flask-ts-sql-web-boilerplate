import { globby } from "globby";
import { readFileSync, writeFileSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const baseDir = path.resolve(__dirname, "../../js");

const files = await globby(["**/*.js"], { cwd: baseDir, absolute: true });

let totalModified = 0;

for (const file of files) {
  const content = readFileSync(file, "utf8");

  const updated = content.replace(
    /from\s+["'](\.{1,2}\/[^"']+)(?<!\.js)["']/g,
    'from "$1.js"'
  );

  if (updated !== content) {
    writeFileSync(file, updated, "utf8");
    console.log(`[fix-imports] Fixed: ${path.relative(baseDir, file)}`);
    totalModified++;
  }
}

console.log(`[fix-imports] Done. Modified ${totalModified} file(s).`);
