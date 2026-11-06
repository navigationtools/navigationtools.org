# navigationtools.org

The website for Navigation Tools, built with [Hugo](https://gohugo.io/) and published by Cloudflare Pages.

## How it works

1. **Pages** are Markdown files in `content/`: `bashnav.md`, `weatherglass.md`, `support.md`, and blog posts in `content/blog/`.
2. **The look** is in `assets/css/site.css` (look D, "Almanac and instruments"); the page structure is in `layouts/`. There is no outside theme, so nothing can change underneath the site.
3. **Publishing:** every push to `main` makes Cloudflare Pages run Hugo and publish the result.

## Preview on the Mac

    cd ~/navigationtools/navigationtools.org && hugo server

Then open <http://localhost:1313/>. The page reloads as you save files. Press Ctrl-C to stop.

## A new blog post

    hugo new content blog/my-post.md

It starts as a draft (`draft: true`), shown by `hugo server -D` but not published until `draft` is removed.

## Not on this site

clipper-drill (private until Clipper approves) and WG Log (unlisted).
