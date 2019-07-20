# npm-deps-parser

Parses, summarizes, and prints "npm audit" json output to markdown for nVision reports. Because neither making sense out of `npm audit` or manually writing markdown tables is fun.

## Usage

1. From the source code repo, run `npm audit --json > path/to/output_file.json` 
2. Navigate to this repo, and run `python3 parser.py -f "path/to/output_file.json"`.
3. If you are only interested in vulns with published CVEs, add `--cves-only` to the above command.
4. Copy and paste the markdown table printed in terminal in nVision.
5. For now, you'd have to manually look for the CVE scores of vulnerabilities with CVEs assigned. I have not found a reliable API to grab that from yet.

Feel free to change and/or improve as needed.

## Example 

```shell
$ python3 parser.py -f "../../../Assesments/client/vuln_code.json"
```

results in:

| CVE | Dependencies | Module | Title | CVSS 3.0 Score | Info |
| --- | --- | --- | --- | --- | --- |
| N/A | react-scripts  | handlebars | Prototype Pollution | N/A | https://npmjs.com/advisories/755 |
| N/A | react-scripts  | braces | Regular Expression Denial of Service | N/A | https://npmjs.com/advisories/786 |
| N/A | husky, react-scripts  | js-yaml | Denial of Service | N/A | https://npmjs.com/advisories/788 |
| N/A | react-scripts  | tar | Arbitrary File Overwrite | N/A | https://npmjs.com/advisories/803 |
| N/A | husky, react-scripts  | js-yaml | Code Injection | N/A | https://npmjs.com/advisories/813 |
| CVE-2019-10747 | lint-staged, react-scripts | set-value | Prototype Pollution | ? | https://npmjs.com/advisories/1012 |
| CVE-2019-10746 | lint-staged, react-scripts | mixin-deep | Prototype Pollution | ? | https://npmjs.com/advisories/1013 |
| CVE-2019-10744 | @redux-offline/redux-offline, aws-appsync, lint-staged, react-scripts | lodash | Prototype Pollution | ? | https://npmjs.com/advisories/1065 |

```shell
$ python3 parser.py -f "../../../Assesments/client/vuln_code.json"
```

results in:

| CVE | Dependencies | Module | Title | CVSS 3.0 Score | Info |
| --- | --- | --- | --- | --- | --- |
| CVE-2019-10747 | lint-staged, react-scripts | set-value | Prototype Pollution | ? | https://npmjs.com/advisories/1012 |
| CVE-2019-10746 | lint-staged, react-scripts | mixin-deep | Prototype Pollution | ? | https://npmjs.com/advisories/1013 |
| CVE-2019-10744 | @redux-offline/redux-offline, aws-appsync, lint-staged, react-scripts | lodash | Prototype Pollution | ? | https://npmjs.com/advisories/1065 |


