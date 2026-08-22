#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const katexCandidates = [
  process.env.KATEX_MODULE,
  "katex",
  "/opt/homebrew/lib/node_modules/@mermaid-js/mermaid-cli/node_modules/katex",
].filter(Boolean);

let katex;
for (const candidate of katexCandidates) {
  try {
    katex = require(candidate);
    break;
  } catch (error) {
    if (candidate === katexCandidates.at(-1)) throw error;
  }
}

const katexOutput = process.env.KATEX_OUTPUT || "htmlAndMathml";
if (!new Set(["html", "mathml", "htmlAndMathml"]).has(katexOutput)) {
  throw new Error(`unsupported KATEX_OUTPUT: ${katexOutput}`);
}

const [inputName, outputName = inputName] = process.argv.slice(2);
if (!inputName) {
  throw new Error("usage: render_katex.js INPUT.html [OUTPUT.html]");
}

function decodeEntities(text) {
  return text
    .replaceAll("&lt;", "<")
    .replaceAll("&gt;", ">")
    .replaceAll("&amp;", "&")
    .replaceAll("&quot;", '"')
    .replaceAll("&#39;", "'");
}

let html = fs.readFileSync(inputName, "utf8");
html = html.replace(
  /<span\s+class="math (inline|display)">([\s\S]*?)<\/span>/g,
  (_, mode, escapedTex) =>
    katex.renderToString(decodeEntities(escapedTex.trim()), {
      displayMode: mode === "display",
      output: katexOutput,
      strict: "error",
      throwOnError: true,
    }),
);

const outputPath = path.resolve(outputName);
fs.writeFileSync(outputPath, html, "utf8");
process.stdout.write(`${outputPath}\n`);
