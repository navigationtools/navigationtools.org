#!/bin/sh
# tests/gate.sh - the website's pass-or-fail check.
#
# Gap analysis fix 5 (Larry's decision, 14 November 2026). The queue runs a repository's
# tests/gate.sh before committing anything to it; if this script exits non-zero, the request is
# refused and nothing reaches Cloudflare.
#
# Why: every other repository had a check that comes back pass or fail; the website had none,
# so a page that failed to build was found only when Cloudflare's build broke after the push.
# What it checks:
#   1. Hugo is installed (it is on Larry's Mac at /opt/homebrew/bin).
#   2. The version matches Cloudflare's build (0.169.0); a different one is reported, not refused.
#   3. The whole site builds without error, into a scratch folder outside the repository, so the
#      working tree is never touched.
#   4. The pages every visitor lands on are in the build: the home page and the sitemap.
# Impact: website commits take a few seconds longer; nothing else changes.

want=0.169.0
command -v hugo >/dev/null 2>&1 || {
    echo "Hugo is not installed, or not on the PATH. Install it with:  brew install hugo"
    exit 1
}
have=$(hugo version | sed -n 's/^hugo v\([0-9.]*\).*/\1/p')
[ "$have" = "$want" ] || echo "note: this Mac has Hugo $have; Cloudflare builds with $want"

out=$(mktemp -d "${TMPDIR:-/tmp}/ntgate.XXXXXX")
# --noBuildLock and --cacheDir keep Hugo's lock and cache out of the repository.
if ! hugo --logLevel warn --destination "$out/site" --cacheDir "$out/cache" --noBuildLock > "$out/log" 2>&1; then
    echo "The site does not build:"
    cat "$out/log"
    rm -rf "$out"
    exit 1
fi
grep -i "warn" "$out/log" | sed 's/^/warning (not a failure): /'

missing=""
for page in index.html sitemap.xml; do
    [ -s "$out/site/$page" ] || missing="$missing $page"
done
pages=$(find "$out/site" -name index.html | wc -l | tr -d ' ')
rm -rf "$out"
if [ -n "$missing" ]; then
    echo "The site built, but these pages are missing:$missing"
    exit 1
fi
echo "site builds: $pages pages"
