import sys; sys.path.insert(0,'.')
from lib import *
from playwright.sync_api import sync_playwright
extra='''
.bgL{position:absolute;inset:0;background:radial-gradient(900px 700px at 85% 30%,#FFE6D6 0%,transparent 60%),linear-gradient(180deg,#F1F6FF 0%,#D6E4FF 45%,#8DB0FF 80%,#2A63F5 100%)}
.bgD{position:absolute;inset:0;background:radial-gradient(900px 800px at 80% 45%,#4F86FF 0%,transparent 62%),linear-gradient(160deg,#081F78 0%,#1747D8 55%,#2A63F5 100%)}
.grid{position:absolute;inset:0;background-size:108px 108px;-webkit-mask-image:linear-gradient(180deg,#000 0%,transparent 55%)}
.L .grid{background-image:linear-gradient(rgba(23,71,216,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(23,71,216,.07) 2px,transparent 2px)}
.D .grid{background-image:linear-gradient(rgba(255,255,255,.06) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.06) 2px,transparent 2px)}
.ghost{position:absolute;font-family:'Inter Display';font-weight:900;letter-spacing:-.05em;line-height:.8;white-space:nowrap}
.L .ghost{color:rgba(23,71,216,.07)}.D .ghost{color:rgba(255,255,255,.07)}
.top{position:absolute;left:72px;right:72px;top:72px}
.L .hd{color:#0B1B33}.L .hd b{color:#1747D8;font-weight:800}.L .sb{color:#3B4A60}
.D .hd{color:#fff}.D .hd b{color:#A9C6FF;font-weight:800}.D .sb{color:rgba(255,255,255,.88)}
.hd{font-size:88px}.sb{font-size:34px;line-height:46px;font-weight:500;margin-top:24px;max-width:800px}
.vis{position:absolute;left:0;right:0;top:450px;height:720px}
.vis svg.sc{position:absolute;left:0;top:0;width:1080px;height:720px;overflow:visible}
.c{position:absolute;padding:22px 30px;border-radius:30px;background:rgba(255,255,255,.88);backdrop-filter:blur(20px);border:2px solid #fff;box-shadow:0 26px 60px rgba(7,26,92,.28);color:#0B1B33;display:flex;align-items:center;gap:18px;white-space:nowrap}
.c.blue{background:linear-gradient(160deg,#2A63F5,#0B2A8F);border-color:rgba(255,255,255,.35);color:#fff}
.ct{font-weight:800;font-size:31px;line-height:38px;letter-spacing:-.01em}
.cs{font-weight:600;font-size:24px;line-height:30px;color:#5B6B82}
.blue .cs{color:rgba(255,255,255,.8)}
.ci{width:64px;height:64px;border-radius:20px;display:flex;align-items:center;justify-content:center;flex:none}
.av{width:72px;height:72px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px;color:#1747D8;background:#DDE8FF;flex:none}
.fade{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,transparent 0%,rgba(11,42,143,.88) 70%,#0B2A8F 100%)}
.ft{position:absolute;left:72px;right:72px;bottom:60px;display:flex;align-items:center;justify-content:space-between}
.url{display:inline-flex;align-items:center;gap:12px;border-radius:999px;padding:16px 28px;font-weight:700;font-size:28px;background:#fff;color:#1747D8}
'''
DEFS='''<defs>
<linearGradient id="gB" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6E9BFF"/><stop offset=".5" stop-color="#1F55EE"/><stop offset="1" stop-color="#0B2A8F"/></linearGradient>
<linearGradient id="gBL" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C4D8FF"/><stop offset="1" stop-color="#4F86FF"/></linearGradient>
<linearGradient id="gBD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1747D8"/><stop offset="1" stop-color="#061A66"/></linearGradient>
<linearGradient id="gW" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#D3E1FF"/></linearGradient>
<linearGradient id="gG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE9A8"/><stop offset=".5" stop-color="#FFC233"/><stop offset="1" stop-color="#E08900"/></linearGradient>
<linearGradient id="gR" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF9A8B"/><stop offset="1" stop-color="#E5484D"/></linearGradient>
<linearGradient id="gP" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFDF6"/><stop offset="1" stop-color="#F3EAD3"/></linearGradient>
<filter id="sh" x="-50%" y="-50%" width="200%" height="220%"><feDropShadow dx="0" dy="30" stdDeviation="28" flood-color="#071A5C" flood-opacity=".38"/></filter>
<filter id="shs" x="-50%" y="-50%" width="200%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#071A5C" flood-opacity=".3"/></filter>
<filter id="bl"><feGaussianBlur stdDeviation="18"/></filter>
</defs>'''
def svg(inner): return f'<svg class="sc" viewBox="0 0 1080 720">{DEFS}{inner}</svg>'
def ic(d,s=34,sw=2.4): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
PHd='<path d="M22 16.900v3a2 2 0 0 1-2.200 2 19.800 19.800 0 0 1-8.600-3.100 19.500 19.500 0 0 1-6-6A19.800 19.800 0 0 1 2.100 4.200 2 2 0 0 1 4.100 2h3a2 2 0 0 1 2 1.700c.1 1 .4 1.900.7 2.800a2 2 0 0 1-.5 2.100L8 9.900a16 16 0 0 0 6 6l1.300-1.300a2 2 0 0 1 2.100-.4c.9.3 1.800.6 2.800.7a2 2 0 0 1 1.700 2z"/>'
CK='<path d="M5 12.500l4.500 4.500L19 7.500"/>'
ARR=ic('<path d="M7 17L17 7M9 7h8v8"/>',26,2.8)
def chip(style,title,sub='',icon='',cls=''):
    i=f'<div class="ci" style="{icon[1]}">{icon[0]}</div>' if icon else ''
    s=f'<div class="cs">{sub}</div>' if sub else ''
    return f'<div class="c {cls}" style="{style}">{i}<div><div class="ct">{title}</div>{s}</div></div>'
RED=('background:#FDECEC;color:#D92D20'); GRN=('background:#E7F8EE;color:#0E8A4B'); BLU=('background:#EEF3FF;color:#1747D8')

def poster(theme,head,sub,vis,ghost='',gstyle=''):
    bg='bgL' if theme=='L' else 'bgD'
    fade='<div class="fade"></div>' if theme=='L' else ''
    g=f'<div class="ghost" style="{gstyle}">{ghost}</div>' if ghost else ''
    return doc(f'''<div class="{theme}" style="position:absolute;inset:0;overflow:hidden"><div class="{bg}"></div><div class="grid"></div>{g}
    <div class="vis">{vis}</div>{fade}
    <div class="top"><div class="h hd">{head}</div><div class="sb">{sub}</div></div>
    <div class="ft">{brand()}<span class="url">bronla.me {ARR}</span></div></div>''',extra)
P={}

# 1 ringing phone
rings=''.join(f'<circle cx="540" cy="350" r="{r}" fill="none" stroke="#1747D8" stroke-opacity="{o}" stroke-width="3"/>' for r,o in [(210,.35),(290,.22),(370,.12),(450,.06)])
P['p01']=poster('L','Əlləriniz doludur. <b>Telefon isə susmur?</b>','Müştəri boş saatı linkinizdən özü seçsin.',svg(f'''{rings}
 <g transform="rotate(-10 540 350)" filter="url(#sh)"><rect x="390" y="200" width="300" height="300" rx="84" fill="url(#gB)"/><rect x="402" y="208" width="276" height="130" rx="70" fill="#fff" opacity=".16"/>
 <g transform="translate(450 260) scale(7.5)" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{PHd}</g></g>
 <g filter="url(#shs)"><circle cx="690" cy="205" r="62" fill="url(#gR)"/><ellipse cx="678" cy="182" rx="34" ry="18" fill="#fff" opacity=".25"/><text x="690" y="232" text-anchor="middle" font-family="Inter Display" font-weight="800" font-size="76" fill="#fff">3</text></g>''')
 +chip('left:56px;top:150px;transform:rotate(-7deg)','Buraxılmış zəng','Aysel · 11:42',(ic(PHd),RED))
 +chip('right:50px;top:330px;transform:rotate(6deg)','Buraxılmış zəng','Nigar · 12:05',(ic(PHd),RED))
 +chip('left:90px;top:500px;transform:rotate(4deg)','Yeni qəbul yazıldı','Sabah, 14:30 · linkdən',(ic(CK,34,3),GRN)),
 '3','right:-40px;top:380px;font-size:900px')

# 2 bell
P['p02']=poster('D','Müştəri unutdu. <b>Yeriniz boş qaldı?</b>','Xatırlatma qəbuldan əvvəl WhatsApp ilə özü gedir.',svg(f'''
 <g fill="none" stroke="#fff" stroke-linecap="round" stroke-width="10" opacity=".35"><path d="M250 180q-50 90-10 190"/><path d="M190 150q-70 120-20 250"/><path d="M640 120q60 80 40 190"/></g>
 <g transform="rotate(14 430 330)" filter="url(#sh)">
  <circle cx="430" cy="585" r="46" fill="url(#gG)"/>
  <path d="M430 110c-118 0-180 86-180 196v112l-66 102a16 16 0 0 0 14 25h464a16 16 0 0 0 14-25l-66-102V306c0-110-62-196-180-196z" fill="url(#gW)"/>
  <path d="M430 110c-118 0-180 86-180 196v112l-66 102h130c-10-150 0-330 116-410z" fill="#fff" opacity=".7"/>
  <rect x="396" y="70" width="68" height="60" rx="30" fill="url(#gW)"/>
  <rect x="170" y="505" width="520" height="46" rx="23" fill="url(#gBL)"/>
 </g>''')
 +f'<div class="c" style="right:48px;top:250px;transform:rotate(-4deg);border-radius:36px 36px 36px 10px;padding:30px 34px;white-space:normal;width:500px;display:block"><div class="cs" style="color:#1747D8;font-weight:700;margin-bottom:8px">Leyla Beauty</div><div style="font-size:32px;line-height:44px;font-weight:500">Salam, Aysel xanım. Sabah saat <b>14:30</b>-da qəbulunuz var.</div><div style="display:flex;gap:14px;margin-top:20px"><span class="pill b" style="font-size:26px;padding:14px 26px">Gələcəm</span><span class="pill" style="font-size:26px;padding:14px 26px;background:#F1F4FA;color:#3B4A60">Vaxtı dəyiş</span></div></div>'
 +chip('right:90px;top:560px;transform:rotate(3deg)','Avtomatik göndərildi','',(ic(CK,34,3),GRN)),
 '','')

# 3 bars + coins
def bar(x,h,w=120,top=600,hi=False):
    y=top-h; f='url(#gB)' if hi else 'url(#gBL)'; t='#A9C6FF' if hi else '#EAF1FF'; s='#0B2A8F' if hi else '#7FA6FF'
    return f'<g filter="url(#shs)"><polygon points="{x},{y} {x+34},{y-26} {x+w+34},{y-26} {x+w},{y}" fill="{t}"/><polygon points="{x+w},{y} {x+w+34},{y-26} {x+w+34},{top-26} {x+w},{top}" fill="{s}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}"/></g>'
bars=''.join(bar(150+i*150,h,hi=(i==4)) for i,h in enumerate([150,220,190,300,420]))
coins=''.join(f'<g><ellipse cx="930" cy="{590-i*30}" rx="86" ry="30" fill="#C97A00"/><rect x="844" y="{566-i*30}" width="172" height="24" fill="#E08900"/><ellipse cx="930" cy="{566-i*30}" rx="86" ry="30" fill="url(#gG)"/><ellipse cx="930" cy="{566-i*30}" rx="58" ry="18" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="4"/></g>' for i in range(4))
P['p03']=poster('L','Çox işlədiniz. <b>Bəs nə qədər qazandınız?</b>','Gəliriniz gün, həftə və ay üzrə bir ekranda.',svg(f'''<ellipse cx="540" cy="620" rx="460" ry="50" fill="#0B2A8F" opacity=".25" filter="url(#bl)"/>{bars}<g filter="url(#shs)">{coins}</g>
 <path d="M170 400 L330 330 L470 360 L640 230 L800 110" fill="none" stroke="#1747D8" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 22"/>
 <g filter="url(#shs)"><circle cx="800" cy="110" r="26" fill="#fff"/><circle cx="800" cy="110" r="14" fill="#1747D8"/></g>''')
 +chip('left:520px;top:20px;transform:rotate(-4deg)','4 520 ₼','Bu ay · gəlir','', 'blue').replace('font-size:31px','').replace('class="ct"','class="ct" style="font-size:54px;line-height:60px"')
 +chip('left:70px;top:210px;transform:rotate(-6deg)','86 qəbul','',(ic('<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>'),BLU)),
 '₼','right:-60px;top:330px;font-size:900px')

# 4 notebook vs calendar
lines=''.join(f'<line x1="250" x2="620" y1="{y}" y2="{y}" stroke="#B9C7E6" stroke-width="3"/>' for y in range(170,620,56))
scr=''.join(f'<path d="M{270+dx} {y} q40 -22 80 0 t80 0 t80 0 t{w} 0" fill="none" stroke="#3B4A60" stroke-width="6" stroke-linecap="round" opacity=".75"/>' for dx,y,w in [(0,150,60),(10,206,20),(0,262,80),(20,318,40),(0,374,70),(10,430,30)])
P['p04']=poster('D','Dəftər itə bilər. <b>Təqvim yox.</b>','Bütün qəbullarınız telefonunuzda, bir yerdə.',svg(f'''
 <g transform="rotate(-9 420 380)" filter="url(#sh)"><rect x="210" y="70" width="440" height="580" rx="18" fill="url(#gP)"/>{lines}<line x1="262" x2="262" y1="70" y2="650" stroke="#F3A3A3" stroke-width="4"/>{scr}
 <path d="M280 190 l300 30" stroke="#E5484D" stroke-width="7" stroke-linecap="round"/><path d="M276 300 l260 -30" stroke="#E5484D" stroke-width="7" stroke-linecap="round"/>
 <circle cx="560" cy="520" r="70" fill="none" stroke="#C99A6B" stroke-width="10" opacity=".45"/>
 {''.join(f'<circle cx="210" cy="{y}" r="16" fill="#0B2A8F"/><rect x="180" y="{y-7}" width="46" height="14" rx="7" fill="#C7D4EE"/>' for y in range(120,640,74))}</g>''')
 +f'<div class="c" style="right:44px;top:210px;transform:rotate(5deg);display:block;padding:30px 32px;width:500px;background:#fff"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px"><div class="ct" style="font-size:36px">Bu gün</div><span class="pill b" style="font-size:24px;padding:10px 22px">6 qəbul</span></div>'
 +''.join(f'<div style="display:flex;gap:20px;align-items:center;padding:16px 0;border-top:2px solid #EEF2F9"><div style="font-weight:800;font-size:32px;color:#1747D8;width:110px">{t}</div><div><div class="ct">{n}</div><div class="cs">{s}</div></div></div>' for t,n,s in [('10:00','Nigar','Manikür'),('11:30','Leyla','Saç boyası'),('14:30','Aysel','Saç kəsimi')])+'</div>',
 '','')

# 5 chain link
P['p05']=poster('L','Bir link. <b>Dolu təqvim.</b>','Linkinizi profilinizə qoyun, müştəri özü yazılsın.',svg(f'''
 <g transform="rotate(-28 540 330)" filter="url(#sh)">
  <rect x="210" y="210" width="420" height="240" rx="120" fill="none" stroke="url(#gB)" stroke-width="64"/>
  <rect x="450" y="210" width="420" height="240" rx="120" fill="none" stroke="url(#gBL)" stroke-width="64"/>
  <path d="M510 210 h0 a120 120 0 0 1 120 120" fill="none" stroke="url(#gB)" stroke-width="64"/>
  <rect x="210" y="210" width="420" height="240" rx="120" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="10" transform="translate(0 -18)"/>
 </g>''')
 +f'<div class="c" style="left:150px;top:300px;transform:rotate(-3deg);padding:30px 40px;border-radius:999px;background:#fff"><div class="ci" style="{BLU};width:76px;height:76px;border-radius:50%">{ic("<path d=\'M10 14a4 4 0 0 0 5.700 0l3-3a4 4 0 0 0-5.700-5.700l-1 1\'/><path d=\'M14 10a4 4 0 0 0-5.700 0l-3 3a4 4 0 0 0 5.700 5.700l1-1\'/>",40)}</div><div style="font-family:Inter Display;font-weight:800;font-size:58px;letter-spacing:-.02em;color:#1747D8">bronla.me/leyla</div></div>'
 +chip('right:60px;top:110px;transform:rotate(6deg)','Instagram profilində','')
 +chip('left:70px;top:540px;transform:rotate(-5deg)','Bu həftə 9 yeni qəbul','Linkdən yazılanlar',(ic(CK,34,3),GRN)),
 '','')

# 6 client memory
pts=[(250,150),(830,170),(230,560),(850,540)]
ln=''.join(f'<path d="M540 360 L{x} {y}" stroke="#fff" stroke-opacity=".55" stroke-width="4" stroke-dasharray="4 14" stroke-linecap="round"/><circle cx="{x}" cy="{y}" r="9" fill="#fff"/>' for x,y in pts)
P['p06']=poster('D','Aysel hansı tonu <b>sevirdi?</b>','Hər müştərinin qeydləri və tarixçəsi bir toxunuşda.',svg(ln+'<circle cx="540" cy="360" r="210" fill="#fff" opacity=".08"/><circle cx="540" cy="360" r="150" fill="#fff" opacity=".1"/>')
 +f'<div class="c" style="left:330px;top:250px;display:block;text-align:center;padding:34px 44px;background:#fff;width:420px"><div class="av" style="width:120px;height:120px;font-size:44px;margin:0 auto 16px">AM</div><div class="ct" style="font-size:38px">Aysel Məmmədova</div><div class="cs">14 qəbul · 2 ildir müştəri</div></div>'
 +chip('left:60px;top:90px;transform:rotate(-5deg)','Küllü sarışın','Sevimli ton')
 +chip('right:50px;top:100px;transform:rotate(5deg)','Boyaya allergiya','Qeyd',(ic('<path d="M12 8v5M12 17h.01"/><circle cx="12" cy="12" r="9"/>'),RED))
 +chip('left:50px;top:530px;transform:rotate(4deg)','12 noyabr','Son qəbul')
 +chip('right:60px;top:520px;transform:rotate(-4deg)','3 dekabr','Ad günü',(ic('<path d="M4 21h16M5 21v-8h14v8M12 13V8M12 4.500v.5"/>'),BLU)),
 '','')

# 7 megaphone
arcs=''.join(f'<path d="M{560+i*70} {250-i*38} q{70+i*20} {110+i*38} 0 {220+i*76}" fill="none" stroke="#1747D8" stroke-opacity="{.5-i*.13}" stroke-width="10" stroke-linecap="round"/>' for i in range(3))
P['p07']=poster('L','Bir mesaj. <b>128 müştəri.</b>','Kampaniya xəbərini WhatsApp ilə toplu göndərin.',svg(f'''{arcs}
 <g transform="rotate(-14 330 360)" filter="url(#sh)">
  <rect x="150" y="300" width="150" height="130" rx="34" fill="url(#gBD)"/>
  <path d="M230 430 l40 150 a26 26 0 0 0 50 -12 l-26 -138z" fill="url(#gBD)"/>
  <polygon points="250,290 500,170 500,560 250,440" fill="url(#gB)"/>
  <polygon points="250,290 500,170 500,260 250,330" fill="#fff" opacity=".18"/>
  <ellipse cx="500" cy="365" rx="62" ry="200" fill="url(#gBL)"/><ellipse cx="506" cy="365" rx="34" ry="150" fill="#0B2A8F" opacity=".55"/>
 </g>''')
 +chip('right:60px;top:60px;transform:rotate(5deg)','Bu həftə 20% endirim','Kampaniya mesajı','','blue')
 +''.join(f'<div class="av" style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;font-size:{int(s*.36)}px;border:5px solid #fff;box-shadow:0 16px 36px rgba(7,26,92,.3)">{t}</div>' for x,y,s,t in [(720,250,110,'AM'),(880,330,92,'NH'),(760,420,96,'LQ'),(910,500,80,'SR'),(660,540,84,'GƏ')])
 +chip('left:70px;top:590px;transform:rotate(-3deg)','46 / 128 göndərildi','',(ic('<path d="M21 3L10 14"/><path d="M21 3l-7 18-4-7-7-4z"/>'),BLU)),
 '','')

# 8 orbit
P['p08']=poster('D','Hansı ustasınız? <b>Bronla sizin üçündür.</b>','Müştərini qəbula yazan hər gözəllik ustası üçün.',svg(f'''
 <g fill="none" stroke="#fff"><ellipse cx="540" cy="380" rx="470" ry="250" stroke-opacity=".18" stroke-width="3"/><ellipse cx="540" cy="380" rx="340" ry="180" stroke-opacity=".28" stroke-width="3"/><ellipse cx="540" cy="380" rx="210" ry="112" stroke-opacity=".4" stroke-width="3"/></g>
 <g filter="url(#sh)"><rect x="430" y="270" width="220" height="220" rx="62" fill="url(#gW)"/></g>
 <g transform="translate(455 295) scale(1.7)"><g fill="#1747D8" mask="url(#mkx)"><path d="M22 21A9 9 0 0 1 40 21V30A8 8 0 0 0 48 38H56A22 22 0 0 1 78 60V66A22 22 0 0 1 56 88H44A22 22 0 0 1 22 66Z"/></g><path d="M38 63.500l8 8 16-17" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>''')
 +chip('left:60px;top:150px;transform:rotate(-5deg)','Bərbər','',(ic('<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.500 8l12 10M8.500 16l12-10"/>'),BLU))
 +chip('right:60px;top:120px;transform:rotate(5deg)','Saç ustası','',(ic('<rect x="3" y="5" width="18" height="6" rx="2"/><path d="M6 11v8M10 11v8M14 11v8M18 11v8"/>'),BLU))
 +chip('left:50px;top:540px;transform:rotate(4deg)','Dırnaq ustası','',(ic('<path d="M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z"/>'),BLU))
 +chip('right:70px;top:560px;transform:rotate(-4deg)','Vizajist','',(ic('<path d="M14 4l6 6-8 8H6v-6z"/><path d="M4 22c0-2 1-4 3-4"/>'),BLU)),
 '','')

# 9 stars
def star(cx,cy,r,rot=0):
    import math
    pts=' '.join(f'{cx+ (r if i%2==0 else r*.46)*math.sin(math.pi*i/5):.1f},{cy-(r if i%2==0 else r*.46)*math.cos(math.pi*i/5):.1f}' for i in range(10))
    return f'<g transform="rotate({rot} {cx} {cy})" filter="url(#shs)"><polygon points="{pts}" fill="url(#gG)" stroke="url(#gG)" stroke-width="{r*.22}" stroke-linejoin="round"/><ellipse cx="{cx-r*.25}" cy="{cy-r*.3}" rx="{r*.3}" ry="{r*.14}" fill="#fff" opacity=".45" transform="rotate(-30 {cx-r*.25} {cy-r*.3})"/></g>'
stars=star(190,330,62,-18)+star(350,230,80,-9)+star(540,180,112,0)+star(730,230,80,9)+star(890,330,62,18)
P['p09']=poster('L','İşinizi bəyəndilər. <b>Bunu hamı görsün.</b>','Qəbuldan sonra rəy sorğusu özü gedir.',svg(stars)
 +f'<div class="c" style="left:330px;top:310px;display:block;text-align:center;padding:26px 50px;background:#fff;width:420px"><div class="h" style="font-size:150px;color:#0B1B33">4,9</div><div class="cs" style="margin-top:6px">128 rəy əsasında</div></div>'
 +f'<div class="c" style="left:110px;top:545px;transform:rotate(-3deg);white-space:normal;background:#fff"><div class="av">AM</div><div><div class="ct">Vaxtında başladı, çox razı qaldım.</div><div class="cs">Aysel · Saç kəsimi</div></div></div>',
 '','')

# 10 web app
P['p10']=poster('D','Yükləməyə ehtiyac yoxdur. <b>Brauzerdə açın.</b>','Bronla hazırda veb tətbiq kimi işləyir.',
 f'''<div style="position:absolute;left:110px;right:110px;top:70px;border-radius:40px;background:#fff;box-shadow:0 50px 110px rgba(4,16,64,.5);transform:rotate(-3deg);overflow:hidden">
  <div style="display:flex;align-items:center;gap:14px;padding:24px 30px;background:#EEF3FF"><i style="width:20px;height:20px;border-radius:50%;background:#FF8A7A"></i><i style="width:20px;height:20px;border-radius:50%;background:#FFC233"></i><i style="width:20px;height:20px;border-radius:50%;background:#7BE3A6"></i><div style="flex:1;margin-left:16px;background:#fff;border-radius:999px;padding:14px 26px;font-weight:700;font-size:28px;color:#1747D8">bronla.me</div></div>
  <div style="padding:34px 36px;color:#0B1B33"><div style="display:flex;align-items:center;gap:14px;color:#1747D8;font-family:Inter Display;font-weight:800;font-size:36px;letter-spacing:-.03em">{logo('#1747D8').replace('<svg','<svg width="48" height="48"')}bronla</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px"><div style="border-radius:28px;padding:28px;background:linear-gradient(160deg,#2A63F5,#0B2A8F);color:#fff"><div style="font-size:24px;font-weight:600;opacity:.85">Bu gün</div><div class="h" style="font-size:58px;margin-top:6px">6 qəbul</div></div><div style="border-radius:28px;padding:28px;background:#F1F4FA"><div class="cs">Növbəti</div><div class="ct" style="font-size:36px;margin-top:8px">14:30 · Aysel</div></div></div></div></div>'''
 +'<div class="c" style="left:130px;top:520px;transform:rotate(3deg);padding:24px 32px"><div><div class="cs">Tezliklə</div><div class="ct">App Store</div></div></div>'
 +'<div class="c" style="right:130px;top:560px;transform:rotate(-4deg);padding:24px 32px"><div><div class="cs">Tezliklə</div><div class="ct">Google Play</div></div></div>',
 '','')
# slogan on p10 footer
P['p10']=P['p10'].replace('</span></div></div>','</span></div><div style="position:absolute;left:0;right:0;bottom:160px;text-align:center;font-family:Inter Display;font-weight:800;font-size:64px;letter-spacing:-.03em;color:#fff">Bronla, gəl!</div></div>',1)
# mask for p08 logo
P['p08']=P['p08'].replace('<defs>','<defs><mask id="mkx"><rect width="100" height="100" fill="#fff"/><path d="M38 63.500l8 8 16-17" fill="none" stroke="#000" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></mask>',1)

import os
os.makedirs('out2',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for k,v in P.items():
        pg.set_content(v); pg.wait_for_timeout(150); pg.screenshot(path=f'out2/bronla_{k}.png')
    b.close()
from PIL import Image
ks=sorted(P)
for n,grp in enumerate([ks[:5],ks[5:]]):
    s=Image.new('RGB',(5*520,640),'#777')
    for i,k in enumerate(grp): s.paste(Image.open(f'out2/bronla_{k}.png').resize((512,640)),(i*520,0))
    s.save(f'p2sheet{n}.png')
