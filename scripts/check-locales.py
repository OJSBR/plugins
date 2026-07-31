#!/usr/bin/env python3
"""
Check that every public OJSBR plugin ships a European Portuguese (pt) translation.

OJSBR plugins are a showcase for an international community, so every translatable
plugin must carry Brazilian Portuguese (pt_BR) *and* European Portuguese, alongside
the other standard locales. This script enforces the European Portuguese part.

For each public, non-fork repository in the organization (minus SKIP_REPOS) it:

  1. lists the plugin's `locale/` directory on the default branch;
  2. if the repository is translatable at all (it has a `locale/` directory),
     requires a European Portuguese locale to be present:
       - `locale/pt/`      on OJS/OMP 3.4+ default branches (short codes), or
       - `locale/pt_PT/`   on OJS 3.3 default branches (five-letter codes);
  3. requires that locale to actually contain a `locale.po` file.

A repository with no `locale/` directory is treated as non-translatable and skipped.

The directory listing is read through the GitHub contents API. Exit code is 0 when
everything is fine and 1 when any plugin is missing the European Portuguese locale.
"""

import json
import os
import sys
import urllib.error
import urllib.request

ORG = "OJSBR"
SKIP_REPOS = {".github", "plugins"}
API = "https://api.github.com"
TIMEOUT = 30


def request(url, accept="application/vnd.github+json"):
    req = urllib.request.Request(url)
    req.add_header("Accept", accept)
    req.add_header("User-Agent", "ojsbr-locale-check")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    return urllib.request.urlopen(req, timeout=TIMEOUT)


def api_get(path):
    try:
        with request(API + path) as response:
            return json.load(response), response.status
    except urllib.error.HTTPError as error:
        return None, error.code


def list_repositories():
    repos, page = [], 1
    while True:
        batch, _ = api_get(f"/orgs/{ORG}/repos?per_page=100&type=public&page={page}")
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return [
        repo
        for repo in repos
        if not repo["fork"] and not repo["archived"] and repo["name"] not in SKIP_REPOS
    ]


def list_dir(repo, path, branch):
    data, status = api_get(f"/repos/{ORG}/{repo}/contents/{path}?ref={branch}")
    if status == 404 or data is None:
        return None
    return [entry["name"] for entry in data]


def main():
    problems = []
    checked = 0

    print(f"Checking European Portuguese (pt) locale in {ORG} plugin repositories\n")
    for repo in sorted(list_repositories(), key=lambda r: r["name"].lower()):
        name, branch = repo["name"], repo["default_branch"]
        locales = list_dir(name, "locale", branch)
        if locales is None:
            print(f"  – {name}: no locale/ directory (not translatable, skipped)")
            continue
        checked += 1
        # 3.3 branches use five-letter codes (pt_PT); 3.4+ use the short code (pt).
        wanted = "pt_PT" if branch.endswith("3_3_0") else "pt"
        if wanted not in locales:
            problems.append(f"{name}: missing locale/{wanted}/ on {branch}")
            print(f"  ✗ {name}: missing locale/{wanted}/ (has: {', '.join(sorted(locales))})")
            continue
        files = list_dir(name, f"locale/{wanted}", branch) or []
        if "locale.po" not in files:
            problems.append(f"{name}: locale/{wanted}/ has no locale.po on {branch}")
            print(f"  ✗ {name}: locale/{wanted}/ has no locale.po")
            continue
        print(f"  ✓ {name}: locale/{wanted}/locale.po")

    print(f"\n{checked} translatable plugin(s) checked.")
    if problems:
        print(f"\n{len(problems)} problem(s) found:")
        for problem in problems:
            print(f"  - {problem}")
        print(
            "\nEvery translatable OJSBR plugin must ship a European Portuguese locale "
            "(locale/pt/, or locale/pt_PT/ on OJS 3.3) with a locale.po file."
        )
        return 1
    print("All translatable plugins ship a European Portuguese locale.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
