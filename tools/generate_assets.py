"""Rebuild the profile's native SVG layouts without changing the source artwork.

Run from any directory: python tools/generate_assets.py
The README uses the generated files directly; no build or hosted renderer is needed.
"""

from pathlib import Path
from html import escape
import base64

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ART = "data:image/png;base64," + base64.b64encode((ASSETS / "kiro-banner.png").read_bytes()).decode("ascii")
FONT = "'Segoe UI',Arial,sans-serif"
MONO = "'Cascadia Code',Consolas,monospace"
BG, PANEL, LINE = "#0b0e14", "#111722", "#2b384e"
WHITE, MUTED, BLUE = "#f3f3ed", "#a9b5cb", "#90a9ff"


def save(name, width, height, content, label):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(label, quote=True)}">
<title>{escape(label)}</title>
{content}
</svg>\n'''
    (ASSETS / name).write_text(svg, encoding="utf-8")


save("profile-header.svg", 1000, 380, f'''
<defs>
  <clipPath id="frame"><rect x="1" y="1" width="998" height="378" rx="16"/></clipPath>
  <linearGradient id="veil"><stop offset="0" stop-color="{BG}"/><stop offset=".42" stop-color="{BG}"/><stop offset=".55" stop-color="{BG}" stop-opacity=".87"/><stop offset=".69" stop-color="{BG}" stop-opacity=".08"/><stop offset="1" stop-color="{BG}" stop-opacity=".02"/></linearGradient>
</defs>
<g clip-path="url(#frame)">
  <rect width="1000" height="380" fill="{BG}"/>
  <image x="455" width="545" height="380" preserveAspectRatio="xMidYMid slice" xlink:href="{ART}"/>
  <rect width="1000" height="380" fill="url(#veil)"/>
  <g fill="none" stroke="{BLUE}"><path d="M0 311C200 292 248 370 490 326S811 286 1000 313" opacity=".18"/><path d="M0 330C180 311 302 359 511 337S813 303 1000 334" opacity=".09"/></g>
  <circle cx="54" cy="47" r="4" fill="#9ac9ac"/>
  <text x="69" y="51" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{MUTED}">KIROZXY / DEVELOPER PROFILE</text>
  <text x="48" y="166" font-family="{FONT}" font-size="96" font-weight="700" letter-spacing="-6" fill="{WHITE}">Kiro<tspan fill="{BLUE}">.</tspan></text>
  <rect class="cursor" x="282" y="103" width="4" height="68" rx="1" fill="{BLUE}"/>
  <text x="54" y="219" font-family="{FONT}" font-size="29" fill="{WHITE}">Android developer.</text>
  <text x="54" y="256" font-family="{FONT}" font-size="17" fill="{MUTED}">Kotlin, Compose &amp; a soft spot for retro.</text>
  <text x="54" y="340" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{BLUE}">CODE / PLAY / REPEAT</text>
  <path d="M956 25h19v19M25 354h19" fill="none" stroke="{BLUE}" stroke-width="2"/>
</g>
<rect x=".5" y=".5" width="999" height="379" rx="16" fill="none" stroke="{LINE}"/>
<style>.cursor{{animation:blink 2s steps(1,end) infinite}}@keyframes blink{{0%,48%{{opacity:1}}50%,98%{{opacity:0}}}}@media(prefers-reduced-motion:reduce){{.cursor{{animation:none}}}}</style>
''', "Kiro — Android developer. Kotlin, Compose, and a soft spot for retro.")

save("profile-header-mobile.svg", 580, 530, f'''
<defs>
  <clipPath id="frame"><rect x="1" y="1" width="578" height="528" rx="16"/></clipPath>
  <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{BG}"/><stop offset=".3" stop-color="{BG}" stop-opacity="0"/></linearGradient>
</defs>
<g clip-path="url(#frame)">
  <rect width="580" height="530" fill="{BG}"/>
  <image x="0" y="235" width="580" height="295" preserveAspectRatio="xMidYMid slice" xlink:href="{ART}"/>
  <rect x="0" y="235" width="580" height="295" fill="url(#fade)"/>
  <circle cx="33" cy="36" r="4" fill="#9ac9ac"/>
  <text x="48" y="40" font-family="{MONO}" font-size="11" letter-spacing="1.8" fill="{MUTED}">KIROZXY / DEVELOPER PROFILE</text>
  <text x="27" y="136" font-family="{FONT}" font-size="90" font-weight="700" letter-spacing="-5" fill="{WHITE}">Kiro<tspan fill="{BLUE}">.</tspan></text>
  <text x="33" y="182" font-family="{FONT}" font-size="27" fill="{WHITE}">Android developer.</text>
  <text x="33" y="216" font-family="{FONT}" font-size="17" fill="{MUTED}">Kotlin, Compose &amp; a soft spot for retro.</text>
  <path d="M538 25h17v17" fill="none" stroke="{BLUE}" stroke-width="2"/>
</g>
<rect x=".5" y=".5" width="579" height="529" rx="16" fill="none" stroke="{LINE}"/>
''', "Kiro — Android developer. Kotlin, Compose, and a soft spot for retro.")


def project(name, title, kind, first, second, tags, footer, icon):
    save(name, 620, 312, f'''
<g transform="translate(10 10)">
<rect x="1" y="1" width="598" height="290" rx="14" fill="{PANEL}" stroke="{LINE}"/>
<path d="M1 58h598" stroke="{LINE}"/>
<text x="28" y="36" font-family="{MONO}" font-size="13" letter-spacing="1.3" fill="{BLUE}">{escape(kind)}</text>
<g transform="translate(528 87)" fill="none" stroke="{BLUE}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
<text x="27" y="113" font-family="{FONT}" font-size="42" font-weight="600" letter-spacing="-1.8" fill="{WHITE}">{escape(title)}</text>
<text x="29" y="155" font-family="{FONT}" font-size="21" fill="{MUTED}">{escape(first)}</text>
<text x="29" y="185" font-family="{FONT}" font-size="21" fill="{MUTED}">{escape(second)}</text>
<text x="29" y="222" font-family="{MONO}" font-size="14" fill="{BLUE}">{escape(tags)}</text>
<path d="M29 245h542" stroke="{LINE}"/>
<text x="29" y="273" font-family="{FONT}" font-size="16" fill="{WHITE}">{escape(footer)}</text>
<path d="M545 265h24m-8-8 8 8-8 8" fill="none" stroke="{BLUE}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</g>
''', f"{title} — {first} {second} {tags}. {footer}")


project("project-kiroemu.svg", "kiroEmu", "01 / ANDROID APP", "A home for your retro games.", "Library, controls, shaders & save states.", "KOTLIN / COMPOSE / C++", "Explore the app", '<path d="M6 7h22c5 0 8 19 5 21s-8-6-9-6H10c-1 0-6 8-9 6S1 7 6 7Z"/><path d="M8 11v9m-4-4h8m12-4h.1m5 6h.1"/>')
project("project-kiroads.svg", "kiroAds", "02 / OPEN SOURCE", "Ads, billing, analytics & consent.", "Connected in one Android SDK.", "KOTLIN / ADMOB / FIREBASE", "Explore the source", '<path d="m10 5-9 11 9 11m16-22 9 11-9 11m-6-26-5 30"/>')

buttons = {
    "website": ("Website", '<circle cx="13" cy="13" r="10"/><ellipse cx="13" cy="13" rx="4" ry="10"/><path d="M3 13h20"/>'),
    "play": ("kiroEmu", '<path d="m5 3 18 10L5 23Z"/>'),
    "email": ("Say hello", '<rect x="2" y="5" width="22" height="17" rx="2"/><path d="m3 6 10 8L23 6"/>'),
    "coffee": ("Ko-fi", '<path d="M3 7h15v11c0 6-15 6-15 0Zm15 1h3c7 0 7 9-3 9M2 25h18M7 2v2m7-2v2"/>'),
}
for name, (label, icon) in buttons.items():
    save(f"link-{name}.svg", 154, 42, f'''
<rect x="1" y="1" width="152" height="40" rx="7" fill="{PANEL}" stroke="#3a4b68"/>
<g transform="translate(15 10) scale(.8)" fill="none" stroke="{BLUE}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
<text x="48" y="26" font-family="{FONT}" font-size="13" font-weight="500" fill="{WHITE}">{label}</text>
<path d="m130 16 6 5-6 5" fill="none" stroke="#7f91b3" stroke-width="1.5"/>
''', label)

save("footer.svg", 1000, 58, f'''
<path d="M0 29h390m220 0h390" stroke="{LINE}"/>
<g fill="{BLUE}" opacity=".85"><path d="M461 17h8v8h8v-8h8v8h8v24h-40V25h8Z"/><rect x="461" y="29" width="4" height="4" fill="{BG}"/><rect x="481" y="29" width="4" height="4" fill="{BG}"/></g>
<text x="510" y="34" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{MUTED}">GG, WP.</text>
''', "Code. Play. Repeat.")

print("Generated 9 profile SVG assets. Original anime artwork is unchanged.")
