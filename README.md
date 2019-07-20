# npm-deps-parser

Parses, summarizes, and prints "npm audit" json output to markdown for nVision reports. Because neither making sense out of `npm audit` nor manually writing markdown tables is fun.

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

| CVE | Module | Dependecy of | Title | CVSS 3.0 Score | Info |
| --- | --- | --- | --- | --- | --- |
| N/A | handlebars | react-scripts | Prototype Pollution | N/A | https://npmjs.com/advisories/755 |
| N/A | braces | react-scripts | Regular Expression Denial of Service | N/A | https://npmjs.com/advisories/786 |
| N/A | js-yaml | husky, react-scripts | Denial of Service | N/A | https://npmjs.com/advisories/788 |
| N/A | tar | react-scripts | Arbitrary File Overwrite | N/A | https://npmjs.com/advisories/803 |
| N/A | js-yaml | husky, react-scripts | Code Injection | N/A | https://npmjs.com/advisories/813 |
| CVE-2019-10747 | set-value | lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1012 |
| CVE-2019-10746 | mixin-deep | lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1013 |
| CVE-2019-10744 | lodash | @redux-offline/redux-offline, aws-appsync, lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1065 |

```shell
$ python3 parser.py -f "../../../Assesments/client/vuln_code.json"
```

results in:

| CVE | Module | Dependecy of | Title | CVSS 3.0 Score | Info |
| --- | --- | --- | --- | --- | --- |
| CVE-2019-10747 | set-value | lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1012 |
| CVE-2019-10746 | mixin-deep | lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1013 |
| CVE-2019-10744 | lodash | @redux-offline/redux-offline, aws-appsync, lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1065 |


