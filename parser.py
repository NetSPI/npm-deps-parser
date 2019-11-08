import sys
import json
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cves-only", dest="cve_only", help="Adds only libraries with cves",
                        action="store_true")
    parser.add_argument("-i", dest="stdin", help="takes input from stdin instead of a file",
                        action="store_true")
    parser.add_argument("-f", "--file", help="Path for json file")
    args = parser.parse_args()
    return args

def get_root_deps(paths):
    deps = []
    depths = []
    for d in paths:
        libs = d.split(">")
        root = libs[0] 
        depths.append(len(libs))
        if root not in deps:
            deps.append(root)
    return deps, str(max(depths))

def parse(stdin=False, file_path="", cve_only=False):
    if stdin:
        npm_json = json.load(sys.stdin)
        process_json(npm_json, cve_only=cve_only)
    elif file_path is not "":
        with open(file_path) as json_file:
            npm_json = json.load(json_file)
        process_json(npm_json, cve_only=cve_only)
    else:
        print("[-] You must specify a path or pass json via stdin using -i")

def process_json(npm_json, cve_only=False):
    print("\n\n| CVE | Module | Dependecy of | Depth |  Title | CVSS 3.0 Score | Info |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for adv in npm_json["advisories"]:
        vuln = npm_json["advisories"][adv]
        cves = vuln["cves"]
        paths = vuln["findings"][0]["paths"]
        deps,depth = get_root_deps(paths)
        deps_str = ", ".join(deps)
        if len(cves) > 0:
            for cve in cves:
                print(f"| {cve} | {vuln['module_name']} | {deps_str} | {depth} |" 
                      +f" {vuln['title']} | ? | {vuln['url']} |")
            continue
        if not cve_only and len(cves) is 0:
            print(f"| N/A | {vuln['module_name']} | {deps_str} | {depth} |" +
                 f" {vuln['title']} | N/A | {vuln['url']} |")
    print("\n")

def main():
    args = get_arguments()
    parse(stdin=args.stdin ,file_path=args.file, cve_only=args.cve_only)

if __name__ == "__main__":
    main()

