"""Builds the static site into site\\ (English at the root, Chinese in zh\\). Standard library only; no outside requests.
  python build.py                    theme moonlit (B), a draft: {{?...}} shows a "to confirm" mark, pages are noindex
  python build.py --theme notebook   or graph: the look is only themes\\<name>.css, the words never change
  python build.py --final            refuses while anything still waits for his confirmation
"""
import html
import re
import shutil
import sys
from pathlib import Path

import content as C

HERE = Path(__file__).resolve().parent
OUT = HERE / "site"
THEMES = ["moonlit", "notebook", "graph"]
TBC = re.compile(r"\{\{\?(.+?)\}\}")
PAGES = ["index", "about", "experience", "projects"]


def text(s, lang):
    """Escape, then turn {{?x}} into a marked span."""
    return TBC.sub(lambda m: f'<span class="tbc">{m.group(1)}<sup>{C.UI[lang]["tbc"]}</sup></span>', html.escape(s, quote=False))


def layout(page, lang, title, main, theme):
    ui = C.UI[lang]
    up = "../" if lang == "zh" else ""
    other = ("../" if lang == "zh" else "zh/") + f"{page}.html"
    home = "index.html"
    links = "".join(f'<a href="{p}.html"{" aria-current=page" if p == page else ""}>{ui[p]}</a>' for p in ("about", "experience", "projects"))
    full = ui["title_home"] if page == "index" else f'{title} · {ui["title_home"]}'
    sky = ""
    if theme == "moonlit":   # the home page has 小茶's sleeping cat on the moon; the other pages the plain moon
        sky_file = "sky_home.svg" if page == "index" else "sky.svg"
        sky = f'<img class="sky" src="{up}assets/{sky_file}" alt="" aria-hidden="true">'
        if page == "index":
            sky += f'<img class="mooncat" src="{up}assets/moon_cat.png" alt="" aria-hidden="true">'
    return f"""<!doctype html>
<html lang="{'zh-Hans' if lang == 'zh' else 'en'}" data-page="{page}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{html.escape(full)}</title>
<link rel="stylesheet" href="{up}assets/base.css">
<link rel="stylesheet" href="{up}assets/theme.css">
</head>
<body>
{sky}<div class="page">
<nav><a class="home" href="{home}">{ui['title_home']}</a>{links}<a href="#contact">{ui['contact']}</a><span class="sp"></span><a class="lang" href="{other}" hreflang="{'en' if lang == 'zh' else 'zh-Hans'}">{ui['other']}</a></nav>
<main>
{main}
</main>
<footer id="contact"><h2>{ui['contact_h']}</h2><p>{ui['contact_body']}</p></footer>
</div>
</body>
</html>
"""


def card(c, lang):
    tag = "a" if c.get("href") else "div"
    href = f' href="{c["href"]}"' if c.get("href") else ""
    kind = f'<span class="kind">{text(c["kind"], lang)}</span>' if c.get("kind") else ""
    foot = f'<p class="foot">{text(c["foot"], lang)}</p>' if c.get("foot") else ""
    up = "../" if lang == "zh" else ""
    img = f'<img class="cover" src="{up}assets/{c["img"]}" alt="">' if c.get("img") else ""
    return f'<{tag} class="card"{href}>{img}{kind}<h3>{text(c["title"], lang)}</h3><p>{text(c["body"], lang)}</p>{foot}</{tag}>'


def home_page(lang):
    h = C.HOME[lang]
    who = "".join(f"<p>{text(p, lang)}</p>" for p in h["who"])
    cards = "".join(card(c, lang) for c in h["cards"])
    return (f'<header class="hero"><h1>{text(h["name"], lang)}</h1><p class="tag">{text(h["tagline"], lang)}</p></header>'
            f'<section class="who"><h2>{text(h["who_h"], lang)}</h2><div class="cols">{who}</div></section>'
            f'<section class="make"><h2>{text(h["make_h"], lang)}</h2><div class="cards">{cards}</div></section>')


def head(d, lang):
    return f'<header class="sub"><h1>{text(d["h"], lang)}</h1><p class="tag">{text(d["lead"], lang)}</p></header>'


def about_page(lang):
    d = C.ABOUT[lang]
    body = "".join(f'<section class="prose"><h2>{text(s["h"], lang)}</h2><div>' + "".join(f"<p>{text(p, lang)}</p>" for p in s["p"]) + "</div></section>"
                   for s in d["sections"])
    return head(d, lang) + body


def experience_page(lang):
    d = C.EXPERIENCE[lang]
    out = head(d, lang)
    for g in d["groups"]:
        rows = ""
        for i in g["items"]:
            pts = "<ul>" + "".join(f"<li>{text(p, lang)}</li>" for p in i["points"]) + "</ul>" if i["points"] else ""
            rows += (f'<article class="entry"><div class="when">{text(i["when"], lang)}</div><div><h3>{text(i["title"], lang)}</h3>'
                     f'<p class="org">{text(i["org"], lang)}</p>{pts}</div></article>')
        out += f'<section class="timeline"><h2>{text(g["h"], lang)}</h2><div>{rows}</div></section>'
    return out


def projects_page(lang):
    d = C.PROJECTS[lang]
    out = head(d, lang)
    for g in d["groups"]:
        out += f'<section class="make" id="{g["id"]}"><h2>{text(g["h"], lang)}</h2><div class="cards">' + "".join(card(c, lang) for c in g["items"]) + "</div></section>"
    return out


def pending():
    """Every {{?...}} left, per language."""
    found = []

    def walk(v):
        if isinstance(v, str):
            found.extend(TBC.findall(v))
        elif isinstance(v, dict):
            for x in v.values():
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
    for block in (C.HOME, C.ABOUT, C.EXPERIENCE, C.PROJECTS):
        walk(block)
    return found


def main():
    theme = sys.argv[sys.argv.index("--theme") + 1] if "--theme" in sys.argv else "moonlit"
    if theme not in THEMES:
        sys.exit(f"theme must be one of {THEMES}")
    left = pending()
    if "--final" in sys.argv and left:
        sys.exit("still waiting for his confirmation: " + ", ".join(left))
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "zh").mkdir()
    shutil.copy(HERE / "themes" / "base.css", OUT / "assets" / "base.css")
    shutil.copy(HERE / "themes" / f"{theme}.css", OUT / "assets" / "theme.css")
    for f in (HERE / "themes" / "assets").glob("*"):
        shutil.copy(f, OUT / "assets" / f.name)
    makers = {"index": home_page, "about": about_page, "experience": experience_page, "projects": projects_page}
    for lang in ("en", "zh"):
        for page in PAGES:
            title = C.UI[lang].get(f"title_{page}", "")
            doc = layout(page, lang, title, makers[page](lang), theme)
            (OUT / ("zh" if lang == "zh" else "") / f"{page}.html").write_text(doc, encoding="utf-8", newline="\n")
    print(f"built site\\ with theme {theme}; to confirm: {left}")


if __name__ == "__main__":
    main()
