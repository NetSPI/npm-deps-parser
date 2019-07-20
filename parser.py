import json
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cves-only", dest="cve_only", help="Adds only libraries with cves",
                        action="store_true")
    parser.add_argument("-f", "--file", help="Path for json file")
    args = parser.parse_args()
    return args

def get_root_deps(paths):
    deps = []
    for d in paths:
        root = d.split(">",1)[0]
        if root not in deps:
            deps.append(root)
    return deps

def parse(file_path, cve_only):
    with open(file_path) as json_file:
        npm_json = json.load(json_file)
    print("| CVE | Dependencies | Module | Title | CVSS 3.0 Score | Info |")
    print("| --- | --- | --- | --- | --- | --- |")
    for adv in npm_json["advisories"]:
        vuln = npm_json["advisories"][adv]
        cves = vuln["cves"]
        paths = vuln["findings"][0]["paths"]
        deps_str = ", ".join(get_root_deps(paths))
        if len(cves) > 0:
            for cve in cves:
                print(f"| {cve} | {deps_str} | {vuln['module_name']} | {vuln['title']} | ? | {vuln['url']} |")
            continue
        if not cve_only and len(cves) is 0:
            print(f"| N/A | {deps_str}  | {vuln['module_name']} | {vuln['title']} | N/A | {vuln['url']} |")
        print


def main():
    args = get_arguments()
    parse(args.file, args.cve_only)

if __name__ == "__main__":
    main()

