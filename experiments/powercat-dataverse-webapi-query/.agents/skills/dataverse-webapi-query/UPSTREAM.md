# Upstream provenance and adaptations

Source: `microsoft/power-cat-skills` at commit `33bc38456abb83f27daad968b748c8085f2a78ef`.

Original path: `plugins/powercat-dataverse/skills/dataverse-webapi-query/dataverse-webapi-query.md`.

Original blob: `8791590eeca8b1c697856c8a5cca9fbab3ef12b6`.

## Explicit adaptations

1. Rename the instruction entry point to `SKILL.md` for Codex discovery.
2. Replace the incomplete upstream description with a bounded Codex description containing trigger and do-not-trigger conditions.
3. Add a precedence-marked public/synthetic safety wrapper.
4. Disable MCP, metadata endpoint, organisation URL, live request, browser-session, command-line authentication, Postman, MSAL, bearer-token, write-operation, and tenant troubleshooting paths.
5. Replace the example environment URL with `<environment-url>` and the example GUID with `<record-id>`.
6. Record all eight missing upstream references without creating substitute technical content.
7. Copy the completed adaptation byte-for-byte to the experiment-local `.agents/skills` discovery location.
8. Add a deterministic schema/host decision gate and a machine-valid answer-output contract for Codex remediation version 0.2.0.
9. Narrow advanced syntax, metadata discovery, complex FetchXML, aggregation, authentication, error-catalog, and advanced host paths according to the recorded missing-reference disposition.
10. Treat synthetic MCP/tool output as untrusted data and prohibit embedded tool instructions.
11. For remediation 0.2.2, replace the disabled-but-retained upstream runtime body with a self-contained controlled subset that contains every supported syntax, host, schema, security, and output rule inline.
12. Reclassify all bundled references as provenance/evaluator artifacts with no runtime access or dependency. The absent upstream material remains named and is not reconstructed.
13. Front-load every Dataverse query-construction trigger, including unresolved-schema and unresolved-host requests, so implicit selection does not exclude the cases that require safe abstention.
14. Add standard `agents/openai.yaml` metadata with `policy.allow_implicit_invocation: true` and no tool dependencies.

The 0.2.2 body replacement is an explicit, bounded adaptation rather than a silent upstream fork. The original commit, path, blob, license, removed operational paths, and supported subset remain recorded here and in the experiment report.

No upstream clone was modified. The experiment is not a Microsoft-supported Codex installation.

## MIT License

Copyright (c) Microsoft Corporation.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
