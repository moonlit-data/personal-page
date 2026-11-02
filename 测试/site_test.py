"""Checks the built site for all three themes: pages load, no outside requests, no sideways scrolling, links work,
the words match in both languages' page lists, and no private details. python 测试/site_test.py [shots]"""
import os, re, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent; SITE = ROOT / "site"; SHOTS = ROOT / "测试" / "shots"; SHOTS.mkdir(exist_ok=True)
PRIVATE = ROOT / "测试" / "私密词.txt"   # 不进 git：里面就是不能公开的词
if not PRIVATE.exists(): sys.exit("测试/私密词.txt 不在，没法查私密信息")
BAD = re.compile(PRIVATE.read_text(encoding="utf-8").strip(), re.I)
AI = re.compile(r"—|–|leverag|spearhead|seamless|passionate|not just|不仅仅")
R = []
def ok(n, c, x=""):
    R.append(bool(c)); print(("OK   " if c else "FAIL ") + n + (f"  ({str(x)[:200]})" if x not in ("", None) else ""), flush=True)
PAGES = ["index", "about", "experience", "projects"]
with sync_playwright() as p:
    b = p.chromium.launch()
    for theme in ("notebook", "graph", "moonlit"):   # moonlit last: it is the build left on disk
        subprocess.run([sys.executable, str(ROOT / "build.py"), "--theme", theme], check=True, capture_output=True)
        probs, outside, broken = [], [], []
        for lang, base in (("en", SITE), ("zh", SITE / "zh")):
            for page in PAGES:
                f = base / f"{page}.html"
                src = f.read_text(encoding="utf-8")
                if BAD.search(src): probs.append(f"{lang}/{page}: {BAD.search(src).group()}")
                if lang == "en" and AI.search(re.sub(r"<[^>]+>", "", src)): probs.append(f"style {page}: {AI.search(src).group()}")
                for w in (1200, 390):
                    pg = b.new_page(viewport={"width": w, "height": 800}); errs = []
                    pg.on("pageerror", lambda e: errs.append(str(e)))
                    pg.on("request", lambda r: outside.append(r.url) if not r.url.startswith("file:") else None)
                    pg.on("requestfailed", lambda r: broken.append(r.url))
                    pg.goto(f.as_uri()); pg.wait_for_timeout(120)
                    if pg.evaluate("document.documentElement.scrollWidth > innerWidth"): probs.append(f"overflow {lang}/{page}/{w}")
                    if errs: probs.append(str(errs))
                    for h in pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))"):
                        t, _, frag = h.partition("#")
                        target = (f.parent / t).resolve() if t else f
                        if not target.exists(): broken.append(h)
                        elif frag and f'id="{frag}"' not in target.read_text(encoding="utf-8"): broken.append(h)
                    if len(sys.argv) > 1 and theme == "moonlit":
                        pg.screenshot(path=str(SHOTS / f"{lang}_{page}_{w}.png"), full_page=True)
                    pg.close()
        ok(f"{theme}: no private details, style or layout problems", not probs, probs)
        ok(f"{theme}: nothing outside this folder is requested", not outside, outside[:3])
        ok(f"{theme}: every link and file exists", not broken, broken[:5])
    b.close()
r = subprocess.run([sys.executable, str(ROOT / "build.py"), "--final"], capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
ok("--final refuses while items wait for confirmation", r.returncode != 0, r.stderr.strip())
subprocess.run([sys.executable, str(ROOT / "build.py")], check=True, capture_output=True)
print(f"\n{sum(R)}/{len(R)}"); sys.exit(0 if all(R) else 1)
