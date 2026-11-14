# Draws docs/develop.svg and docs/operate.svg for docs/WORKFLOW.md (navigationtools, 12 Nov 2026).
# Run from docs/: python3 draw.py
import html
def box(x,y,w,h,title,lines,fill):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#33415c" stroke-width="1.5"/>'
    s+=f'<text x="{x+w/2}" y="{y+24}" text-anchor="middle" font-weight="bold" font-size="15">{html.escape(title)}</text>'
    for i,l in enumerate(lines):
        s+=f'<text x="{x+w/2}" y="{y+46+i*18}" text-anchor="middle" font-size="12.5">{html.escape(l)}</text>'
    return s
def arrow(x1,y1,x2,y2,label=""):
    s=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#33415c" stroke-width="2" marker-end="url(#a)"/>'
    if label: s+=f'<text x="{(x1+x2)/2+8}" y="{(y1+y2)/2+4}" font-size="12" font-style="italic" fill="#555">{html.escape(label)}</text>'
    return s
def svg(w,h,body,title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Helvetica, Arial, sans-serif">'
      '<defs><marker id="a" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#33415c"/></marker></defs>'
      f'<rect width="{w}" height="{h}" fill="white"/><text x="{w/2}" y="30" text-anchor="middle" font-size="19" font-weight="bold">{html.escape(title)}</text>{body}</svg>')

# 1. Developing the site
B=[("1. A shipmate releases",["writes a web note to inbox/navigationtools/:","what changed and why, release text, documents"],"#e8f0fe"),
   ("2. Navigation Tools session",["writes the page (content/*.md), copies the PDFs","and pictures into static/; checks the build"],"#e6f4ea"),
   ("3. The queue request",["one request in spec/queue/: repository,","paths, message; the session reads it back"],"#e6f4ea"),
   ("4. Larry runs the queue",["checks the paths and PDF pairs, builds the","site (tests/gate.sh), commits and pushes"],"#fef7e0"),
   ("5. Cloudflare builds",["sees the push to main; downloads Hugo 0.169.0;","builds public/; Worker navigationtools-org serves it"],"#fce8e6"),
   ("6. Live, and checked",["navigationtools.org updated in a minute or two;","the session opens the page to confirm"],"#e6f4ea")]
w,h=380,90; L,R=30,500; rows=[70,215,360]
pos=[(L,rows[0]),(R,rows[0]),(R,rows[1]),(L,rows[1]),(L,rows[2]),(R,rows[2])]
body=""
for (t,l,f),(bx,by) in zip(B,pos): body+=box(bx,by,w,h,t,l,f)
body+=arrow(L+w,rows[0]+h/2,R-2,rows[0]+h/2)
body+=arrow(R+w/2,rows[0]+h,R+w/2,rows[1]-2)
body+=arrow(R,rows[1]+h/2,L+w+2,rows[1]+h/2)
body+=arrow(L+w/2,rows[1]+h,L+w/2,rows[2]-2)
body+=arrow(L+w,rows[2]+h/2,R-2,rows[2]+h/2)
y=rows[2]+h+20
open('develop.svg','w').write(svg(910,y,body,"Developing navigationtools.org"))

# 2. Operating the site
body=""
body+=box(268,55,240,62,"A visitor",["types an address"],"#e8f0fe")
body+=box(268,160,240,62,"Cloudflare DNS",["answers for navigationtools.org"],"#fce8e6")
body+=arrow(388,117,388,158)
cols=[("navigationtools.org",["Worker navigationtools-org","serves Hugo's public/","unknown pages: 404 page","public"],"#e6f4ea"),
      ("bashnav.navigationtools.org",["GitHub Pages, from the","bashnav repository","(and the course, later)","public"],"#e6f4ea"),
      ("shipshape.navigationtools.org",["Cloudflare Access first:","Larry only, email code","then Worker shipshape;","manuals from R2: private"],"#fef7e0"),
      ("support@navigationtools.org",["mail: MX records in","Cloudflare DNS point to","iCloud+, delivered","to Larry"],"#e8f0fe")]
cw,cx0=178,16
for i,(t,l,f) in enumerate(cols):
    cx=cx0+i*(cw+10)
    body+=box(cx,280,cw,130,"",l,f)
    body+=f'<text x="{cx+cw/2}" y="302" text-anchor="middle" font-weight="bold" font-size="11">{html.escape(t)}</text>'
    body+=arrow(388,222,cx+cw/2,278)
open('operate.svg','w').write(svg(776,430,body,"Operating navigationtools.org"))
