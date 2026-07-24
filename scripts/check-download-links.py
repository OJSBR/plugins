#!/usr/bin/env python3
"""
Check that every public OJSBR plugin repository offers a direct download link.

For each public, non-fork repository in the organization (minus the ones listed in
SKIP_REPOS) this script:

  1. reads the README from the repository's default branch;
  2. requires at least one direct package link, i.e. a URL of the form
     https://github.com/OJSBR/<repo>/releases/download/<tag>/<file>.tar.gz
     (a link to /releases or /releases/latest is NOT enough: it is a page, not a file);
  3. checks that every such link actually resolves.

It also validates the direct links used in this repository's own README (the catalog),
so a stale entry there is caught as well.

The README is read through the GitHub contents API rather than raw.githubusercontent.com
because the raw host caches aggressively and reports stale content right after a push.

Exit code is 0 when everything is fine and 1 when any problem is found.
"""

import os
import re
import sys
import urllib.error
import urllib.request

ORG = "OJSBR"
SKIP_REPOS = {".github", "plugins"}
API = "https://api.github.com"
PACKAGE_LINK = re.compile(
    r"https://github\.com/" + ORG + r"/[^)\s\"']+/releases/download/[^)\s\"']+\.tar\.gz"
)
TIMEOUT = 30


def request(url, accept="application/vnd.github+json", method="GET"):
    req = urllib.request.Request(url, method=method)
    req.add_header("Accept", accept)
    req.add_header("User-Agent", "ojsbr-download-link-check")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    return urllib.request.urlopen(req, timeout=TIMEOUT)


def api_json(path):
    import json

    with request(API + path) as response:
        return json.load(response)


def list_repositories():
    repos, page = [], 1
    while True:
        batch = api_json(f"/orgs/{ORG}/repos?per_page=100&type=public&page={page}")
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return [
        repo
        for repo in repos
        if not repo["fork"] and not repo["archived"] and repo["name"] not in SKIP_REPOS
    ]


def read_readme(repo, branch):
    try:
        with request(
            f"{API}/repos/{ORG}/{repo}/contents/README.md?ref={branch}",
            accept="application/vnd.github.raw",
        ) as response:
            return response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def link_is_reachable(url):
    """Release assets answer to a plain GET after redirects; HEAD is not always allowed."""
    try:
        with request(url, accept="*/*") as response:
            return response.status == 200, str(response.status)
    except urllib.error.HTTPError as error:
        return False, str(error.code)
    except Exception as error:  # network-level failure
        return False, type(error).__name__


def check_links(label, text, problems):
    links = sorted(set(PACKAGE_LINK.findall(text)))
    if not links:
        problems.append(f"{label}: no direct .tar.gz package link in the README")
        print(f"  ✗ {label}: no direct .tar.gz link")
        return 0
    broken = False
    for link in links:
        ok, status = link_is_reachable(link)
        if not ok:
            broken = True
            problems.append(f"{label}: broken link (HTTP {status}) {link}")
            print(f"  ✗ {label}: HTTP {status} -> {link}")
    if not broken:
        print(f"  ✓ {label}: {len(links)} link(s) OK")
    return len(links)


def main():
    problems = []
    total = 0

    print(f"Checking direct download links in {ORG} plugin repositories\n")
    for repo in sorted(list_repositories(), key=lambda r: r["name"].lower()):
        name, branch = repo["name"], repo["default_branch"]
        readme = read_readme(name, branch)
        if readme is None:
            problems.append(f"{name}: no README.md on {branch}")
            print(f"  ✗ {name}: no README.md on {branch}")
            continue
        total += check_links(name, readme, problems)

    print("\nChecking the links used in this repository's catalog\n")
    try:
        with open("README.md", encoding="utf-8") as handle:
            total += check_links("catalog README", handle.read(), problems)
    except FileNotFoundError:
        print("  (catalog README.md not found, skipped)")

    print(f"\n{total} link(s) checked.")
    if problems:
        print(f"\n{len(problems)} problem(s) found:")
        for problem in problems:
            print(f"  - {problem}")
        print(
            "\nEvery repository README must link straight to the package file "
            "(/releases/download/<tag>/<file>.tar.gz), not just to the releases page."
        )
        return 1
    print("All repositories expose a working direct download link.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
