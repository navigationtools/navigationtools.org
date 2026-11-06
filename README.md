# navigationtools.org

The website for Navigation Tools, built with [Hugo](https://gohugo.io/) and published by Cloudflare as a Worker with static assets.

## How it works

1. **Pages** are Markdown files in `content/`: `bashnav.md`, `weatherglass.md`, `support.md`, and blog posts in `content/blog/`.
2. **The look** is in `assets/css/site.css` (look D, "Almanac and instruments"); the page structure is in `layouts/`. There is no outside theme, so nothing can change underneath the site.
3. **Publishing:** every push to `main` makes Cloudflare build and publish the site.
   1. **Build command** (set in the Cloudflare dashboard): downloads Hugo 0.169.0 for Linux and runs `./hugo --gc --minify`, so Cloudflare builds with the same Hugo as the Mac. When Hugo is upgraded on the Mac, change the version in that command too.
   2. **Deploy command:** `npx wrangler deploy`, which reads `wrangler.jsonc` and serves `public/`.
   3. **Why Workers, not Pages:** Cloudflare now treats Pages as legacy, so new sites start as Workers.
4. **The build command is for Cloudflare only.** On the Mac, use `hugo server` (below). The Linux Hugo it downloads won't run on a Mac, and `.gitignore` keeps it out of commits.

## Preview on the Mac

    cd ~/navigationtools/navigationtools.org && hugo server

Then open <http://localhost:1313/>. The page reloads as you save files. Press Ctrl-C to stop.

## A new blog post

    hugo new content blog/my-post.md

It starts as a draft (`draft: true`), shown by `hugo server -D` but not published until `draft` is removed.

## Not on this site

clipper-drill (private until Clipper approves) and WG Log (unlisted).
