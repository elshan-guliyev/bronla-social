LOGO_W = '''<svg viewBox="0 0 100 100"><defs><mask id="mk%(i)s"><rect width="100" height="100" fill="#fff"/><path d="M38 63.5l8 8 16-17" fill="none" stroke="#000" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></mask></defs><g mask="url(#mk%(i)s)" fill="%(c)s"><path d="M22 21A9 9 0 0 1 40 21V30A8 8 0 0 0 48 38H56A22 22 0 0 1 78 60V66A22 22 0 0 1 56 88H44A22 22 0 0 1 22 66Z"/></g></svg>'''
_n=[0]
def logo(color="#fff"):
    _n[0]+=1
    return LOGO_W % {"i":_n[0],"c":color}
def brand(color="#fff"):
    return f'<div class="brand" style="color:{color}">{logo(color)}<span>bronla</span></div>'
CHECK='<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def doc(body, extra=""):
    css=open('./base.css').read()
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}{extra}</style></head><body>{body}</body></html>'
