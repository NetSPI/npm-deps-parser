# npm-deps-parser

Parses, summarizes, and prints "npm audit" json output to markdown. Because neither making sense out of `npm audit` nor manually writing markdown tables is fun.

## Caveats

Will need to parse the CSV rating or get it from an api.

## Usage

The fastest way to use the parser is to pass the `npm audit --json` output as stdin. To do so run the following from the folder where the `package.json` file is located:

```shell
npm audit --json | python3 ~/path/to/npm-vuln-parser/parser.py -i
```

If you get errors, you can try the below method:

1. From the source code repo, run `npm audit --json > path/to/output_file.json` 
2. Navigate to this repo, and run `python3 parser.py -f "path/to/output_file.json"`.
3. If you are only interested in vulns with published CVEs, add `--cves-only` to the above command.
4. Copy and paste the markdown table in your MD editor.
5. For now, you'd have to manually look for the CVE scores of vulnerabilities with CVEs assigned. I have not found a reliable API to grab that from yet.

Feel free to change and/or improve as needed.

## Example 

```shell
$ python3 parser.py -f "../../../Assesments/client/vuln_code.json"
```

results in:

| CVE | Module | Dependency of | Title | CVSS 3.0 Score | Info |
| --- | --- | --- | --- | --- | --- |
| N/A | handlebars | react-scripts | Prototype Pollution | N/A | https://npmjs.com/advisories/755 |
| CVE-2019-10746 | mixin-deep | lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1013 |
| CVE-2019-10744 | lodash | @redux-offline/redux-offline, aws-appsync, lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1065 |

```shell
$ python3 parser.py -f "../../../Assesments/client/vuln_code.json" --cves-only
```

results in:

| CVE | Module | Dependency of | Title | CVSS 3.0 Score | Info |
| --- | --- | --- | --- | --- | --- |
| CVE-2019-10747 | set-value | lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1012 |
| CVE-2019-10746 | mixin-deep | lint-staged, react-scripts | Prototype Pollution | ? | https://npmjs.com/advisories/1013 |


You can also display the max depth for the reported vulnerabilities using the `-d` flag.

