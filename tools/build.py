"""Build the two versions of the site from one master file.

master.html (kept in the private WIP artifact) contains:
  <!--wip:start--> ... <!--wip:end-->     only in the private WIP version
  /*wip:start*/ ... /*wip:end*/           same, inside CSS
  <!--pub:start ... pub:end-->            only in the public version
  <!--body-->                             where <head> ends and <body> starts

The WIP artifact page IS the master: Artifact-read it, save as master.html, edit, rebuild.

usage: python3 tools/build.py master.html  -> writes index.html (public) and wip.html (artifact page)
"""
import re, sys
src = open(sys.argv[1]).read()

def public(s):
    s = re.sub(r'<!--wip:start-->.*?<!--wip:end-->\n?', '', s, flags=re.S)
    s = re.sub(r'/\*wip:start\*/.*?/\*wip:end\*/\n?', '', s, flags=re.S)
    s = re.sub(r'<!--pub:start(.*?)pub:end-->', r'\1', s, flags=re.S)
    s = s.replace('<title>Portfolio WIP</title>', '<title>Orlando Adams</title>')
    return s

def wip(s):
    # public-only blocks stay as HTML comments, so the WIP page doubles as the master
    return s

def page(s):
    """Full HTML document for GitHub Pages."""
    head, body = s.split('<!--body-->', 1)
    head = re.sub(r'<!doctype html>|<html[^>]*>|</?head>|<body>|<meta charset[^>]*>|<meta name="viewport"[^>]*>', '', head, flags=re.I)
    body = re.sub(r'</body>|</html>', '', body)
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head.strip() + '\n</head>\n<body>\n' + body.strip() + '\n</body>\n</html>\n')

def artifact(s):
    """Artifact page: no document wrapper, title first."""
    s = re.sub(r'<!doctype html>\s*|<html[^>]*>\s*|</?head>\s*|<body>\s*|</body>\s*|</html>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', s, flags=re.I)
    t = re.search(r'<title>.*?</title>\n?', s).group(0)
    return t + s.replace(t, '', 1)

open('index.html', 'w').write(page(public(src)))
m = artifact(wip(src))
if '<title>Portfolio WIP</title>' not in m:
    m = m.replace(re.search(r'<title>.*?</title>', m).group(0), '<title>Portfolio WIP</title>', 1)
open('wip.html', 'w').write(m)
print('built index.html (public) and wip.html (private)')
