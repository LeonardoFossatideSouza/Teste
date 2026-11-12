from PIL import Image, ImageDraw
import os, sys
arqs = sys.argv[1:] or ["E1_127V","E2_220V","E3_carga_leve","E4_roteiro_literal","E5_mosfet_potencia"]
tiles=[]
for n in arqs:
    p=f"shots_hd/{n}.png"
    if not os.path.exists(p): continue
    im=Image.open(p); w,h=im.size
    tiles.append((n, im.crop((0,int(h*0.785),int(w*0.80),h))))
W=max(t[1].width for t in tiles); H=sum(t[1].height+40 for t in tiles)
s=Image.new("RGB",(W,H),(255,255,255)); d=ImageDraw.Draw(s); y=0
for n,c in tiles:
    d.text((10,y+14), n, fill=(0,0,0)); s.paste(c,(0,y+36)); y+=c.height+40
s.thumbnail((1500,2400)); s.save("shots_hd/_leituras.png")
print("montado:", [t[0] for t in tiles], s.size)
