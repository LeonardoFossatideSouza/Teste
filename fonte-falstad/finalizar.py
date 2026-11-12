import html, sys
sys.path.insert(0, "/home/user/Teste/fonte-falstad")
from lzstring import compress_to_encoded_uri_component as cz

BASE = "https://www.falstad.com/circuit/circuitjs.html?ctz="
nets = {
    "A": ("boost_principal", "fonte_127V.txt"),
    "B": ("220V",            "fonte_220V.txt"),
    "C": ("literal",         "variantes/roteiro_literal.txt"),
}
urls, netA = {}, open("fonte_127V.txt").read().strip()
for k, (_, arq) in nets.items():
    urls[k] = BASE + cz(open(arq).read().strip() + "\n")

h = open("relatorio.html").read()
for k in "ABC":
    h = h.replace(f'<div class="mono" id="LINK_{k}"></div>',
                  f'<div class="mono"><a href="{urls[k]}">{html.escape(urls[k])}</a></div>')
h = h.replace('<pre class="mono" id="NET_A" style="background:#f5f7f9;border:1px solid #dde4ea;padding:7px;white-space:pre-wrap;margin:0"></pre>',
              '<pre class="mono" style="background:#f5f7f9;border:1px solid #dde4ea;padding:7px;white-space:pre-wrap;margin:0">' + html.escape(netA) + '</pre>')
open("relatorio.html", "w").write(h)

rot = ["CIRCUITO PRINCIPAL - Fonte chaveada flyback 12 V / 1 A, entrada 127 V AC", urls["A"], "",
       "MESMO CIRCUITO EM 220 V AC - teste bivolt automatico", urls["B"], "",
       "CIRCUITO COMPARATIVO - montagem literal do roteiro (nao regula)", urls["C"], ""]
open("links.txt", "w").write("\n".join(rot))
print("placeholders restantes:", sum(h.count(f"LINK_{k}") for k in "ABC") + h.count("NET_A"))
for k in "ABC": print(k, urls[k][:80] + "...")
