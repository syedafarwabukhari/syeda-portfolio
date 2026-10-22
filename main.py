import streamlit as st
import streamlit.components.v1 as components
import textwrap
from pathlib import Path
import json
import urllib.request
import urllib.error

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="Syeda Ume Farwa Bukhari | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown(
textwrap.dedent("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F8FAFC;
}

/* Hide Streamlit Branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1E293B 100%);
    border-right: 1px solid #334155;
}

/* Sidebar background and menu fix */
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"],
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] [data-testid="stRadio"],
section[data-testid="stSidebar"] div[role="radiogroup"] {
    background: transparent !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(255,255,255,0.05) !important;
    color: #FFFFFF !important;
    border-radius: 10px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label p,
section[data-testid="stSidebar"] div[role="radiogroup"] label span {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: rgba(167,139,250,0.25) !important;
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] * {
    color: #F8FAFC !important;
}

/* Sidebar title */
section[data-testid="stSidebar"] h2 {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

/* Radio menu */
section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 8px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.05);
    padding: 12px 15px;
    border-radius: 10px;
    transition: all 0.2s ease;
    cursor: pointer;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(167, 139, 250, 0.20);
}
/* Main container */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Hero */
.hero-box {
    padding: 55px 45px;
    border-radius: 28px;
    background: linear-gradient(135deg, #111827, #1E293B);
    color: white;
    margin-bottom: 35px;
    box-shadow: 0 20px 50px rgba(15, 23, 42, 0.15);
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.18);
    padding: 8px 16px;
    border-radius: 50px;
    font-size: 14px;
    margin-bottom: 18px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 15px;
}

.hero-title span {
    color: #A78BFA;
}

.hero-subtitle {
    font-size: 18px;
    line-height: 1.8;
    color: #CBD5E1;
    max-width: 750px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    font-weight: 700;
    color: #111827;
    margin-top: 35px;
    margin-bottom: 10px;
}

.section-text {
    color: #64748B;
    font-size: 16px;
    line-height: 1.8;
}

/* Cards */
.service-card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    border: 1px solid #E2E8F0;
    min-height: 190px;
    margin-bottom: 20px;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.05);
    transition: 0.3s;
}

.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(15, 23, 42, 0.10);
}

.service-icon {
    font-size: 32px;
    margin-bottom: 12px;
}

.service-title {
    font-size: 19px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 10px;
}

.service-text {
    color: #64748B;
    line-height: 1.7;
}

/* Stats */
.stat-card {
    background: white;
    padding: 25px;
    text-align: center;
    border-radius: 18px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
}

.stat-number {
    font-size: 30px;
    font-weight: 800;
    color: #4F46E5;
}

.stat-text {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.3px;
}


/* PREMIUM PORTFOLIO CARDS */

/* TOOLS CARDS ENTRANCE ANIMATION */
.tools-card {
    animation: toolsCardEnter 0.75s cubic-bezier(0.2, 0.75, 0.25, 1) both;
}
@keyframes toolsCardEnter {
    from {
        opacity: 0;
        transform: translateY(22px) scale(0.98);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}
@media (prefers-reduced-motion: reduce) {
    .tools-card {
        animation: none !important;
    }
}

.project-card {
    position: relative;
    overflow: hidden;
    background: linear-gradient(145deg, #FFFFFF 0%, #F8F7FF 100%);
    padding: 28px;
    border-radius: 22px;
    border: 1px solid #E5E7FF;
    margin-bottom: 20px;
    box-shadow: 0 10px 28px rgba(79, 70, 229, 0.07);
    transition: transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
}

.project-card:hover {
    transform: translateY(-7px);
    border-color: #A78BFA;
    box-shadow: 0 20px 40px rgba(79, 70, 229, 0.15);
}

/* PORTFOLIO IMAGE ALIGNMENT */
div[data-testid="stImage"] {
    margin-bottom: 12px;
}

div[data-testid="stImage"] img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    object-position: center;
    border-radius: 16px;
}

/* Consistent portfolio card spacing */
.project-card {
    min-height: 245px;
    box-sizing: border-box;
}
.project-title {
    font-size: 21px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 12px;
    line-height: 1.4;
}

.project-text {
    color: #64748B;
    line-height: 1.8;
    font-size: 15px;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    padding: 10px 25px;
}
/* Fix white box behind sidebar profile title */
section[data-testid="stSidebar"] [data-testid="stMarkdown"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
/* Footer */

.profile-image {
    width: 100%;
    max-width: 340px;
    margin: 15px auto;
    border-radius: 28px;
    border: 4px solid #FFFFFF;
    overflow: hidden;
    background: linear-gradient(135deg, #EDE9FE, #F8FAFC);
    box-shadow: 0 22px 50px rgba(79, 70, 229, 0.18);
    transition: transform 0.35s ease, box-shadow 0.35s ease;
}

.profile-image img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
}

.profile-image:hover {
    transform: translateY(-5px);
    box-shadow: 0 28px 60px rgba(79, 70, 229, 0.25);
}
.footer {
    text-align: center;
    padding: 35px 10px;
    margin-top: 50px;
    border-top: 1px solid #E2E8F0;
    color: #64748B;
}
@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-box {
        padding: 35px 25px;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-subtitle {
        font-size: 16px;
    }

    .section-title {
        font-size: 28px;
    }

    .service-card {
        padding: 22px;
    }

    .project-card {
        padding: 22px;
    }

    .stat-card {
        margin-bottom: 15px;
    }
}

/* PREMIUM VISUAL UPGRADE */
:root { color-scheme: light; }
.stApp { background: radial-gradient(circle at 95% 2%,#ede9fe 0,transparent 30%),#f8fafc; }
.block-container { animation: pageEnter .55s ease both; }
@keyframes pageEnter { from {opacity:0;transform:translateY(12px)} to {opacity:1;transform:translateY(0)} }
.hero-box { position:relative;overflow:hidden;background:linear-gradient(125deg,#101827 5%,#29205b 65%,#4f46e5 120%);border:1px solid rgba(255,255,255,.12); }
.hero-box:after {content:"";position:absolute;right:-70px;top:-90px;width:250px;height:250px;border-radius:50%;background:radial-gradient(circle,rgba(167,139,250,.3),transparent 70%);pointer-events:none;animation:glow 5s ease-in-out infinite alternate;}
@keyframes glow {to{transform:scale(1.35) translate(-20px,15px);opacity:.55}}
/* SMOOTH PREMIUM ANIMATIONS */
html {
    scroll-behavior: smooth;
}

.hero-badge {
    animation: fadeSlideUp 0.7s ease-out both;
}

.hero-title {
    animation: fadeSlideUp 0.85s ease-out both;
    animation-delay: 0.1s;
}

.hero-subtitle {
    animation: fadeSlideUp 0.95s ease-out both;
    animation-delay: 0.2s;
}

@keyframes fadeSlideUp {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* HOME HERO PREMIUM UPGRADE */
.hero-box {
    min-height: 330px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 55px 45px;
    border-radius: 28px;
    background:
        radial-gradient(circle at 90% 10%, rgba(167,139,250,0.22), transparent 32%),
        linear-gradient(125deg, #101827 5%, #29205b 65%, #4f46e5 120%);
    box-shadow: 0 24px 55px rgba(31, 25, 80, 0.20);
}

.hero-badge {
    width: fit-content;
    max-width: 100%;
    letter-spacing: 1px;
    font-size: 12px;
    font-weight: 700;
}

.hero-title {
    font-size: clamp(34px, 4vw, 52px);
    line-height: 1.15;
    overflow-wrap: anywhere;
}

.hero-subtitle {
    font-size: 17px;
    line-height: 1.9;
    max-width: 680px;
}

@media (max-width: 768px) {
    .hero-box {
        min-height: auto;
        padding: 32px 22px;
        border-radius: 22px;
    }

    .hero-badge {
        font-size: 10px;
        letter-spacing: 0.5px;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-subtitle {
        font-size: 15px;
    }
}

.hero-title {letter-spacing:-1.4px;}
.service-card,.project-card,.stat-card {height:100%;transition:transform .3s ease,box-shadow .3s ease,border-color .3s ease;}
.service-card:hover,.project-card:hover,.stat-card:hover {transform:translateY(-7px);border-color:#c4b5fd;box-shadow:0 20px 40px rgba(79,70,229,.12);}
.service-icon {display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:16px;background:#f1edff;}
.stButton>button[kind="primary"],.stButton>button {background:linear-gradient(110deg,#4f46e5,#7c3aed);color:#fff;border:0;box-shadow:0 8px 22px rgba(79,70,229,.2);transition:transform .2s,box-shadow .2s;}
.stButton>button:hover {transform:translateY(-2px);color:white;border:0;box-shadow:0 12px 26px rgba(79,70,229,.28);}
[data-testid="stProgressBar"] [role="progressbar"]>div {background:linear-gradient(90deg,#4f46e5,#a78bfa);}
[data-testid="stForm"] {background:white;border:1px solid #e2e8f0;border-radius:20px;padding:24px;box-shadow:0 10px 30px rgba(15,23,42,.05)}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {background:rgba(167,139,250,.25);outline:1px solid rgba(167,139,250,.45)}
@media (prefers-reduced-motion:reduce) {*,*:before,*:after {animation-duration:.01ms!important;transition-duration:.01ms!important}}

/* ABOUT ME - PREMIUM APPROACH SECTION */
.approach-card {
    background: linear-gradient(135deg, #FFFFFF 0%, #F3F0FF 100%);
    border: 1px solid #E5E7FF;
    border-radius: 22px;
    padding: 28px 30px;
    margin: 16px 0 26px;
    box-shadow: 0 12px 30px rgba(79, 70, 229, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.approach-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 38px rgba(79, 70, 229, 0.13);
}

.approach-card p {
    color: #475569;
    font-size: 16px;
    line-height: 1.9;
    margin: 0;
}

/* SERVICES PAGE POLISH */
.service-card {
    min-height: 220px;
    padding: 30px;
    margin-bottom: 22px;
    border-radius: 22px;
    border: 1px solid #E5E7FF;
    background: linear-gradient(145deg, #FFFFFF 0%, #F8F7FF 100%);
    box-shadow: 0 10px 28px rgba(79, 70, 229, 0.07);
    transition: transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
}

.service-card:hover {
    transform: translateY(-6px);
    border-color: #A78BFA;
    box-shadow: 0 18px 36px rgba(79, 70, 229, 0.13);
}

.service-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 58px;
    height: 58px;
    margin-bottom: 18px;
    border-radius: 17px;
    background: linear-gradient(135deg, #EDE9FE, #F5F3FF);
    font-size: 27px;
}

.service-title {
    font-size: 19px;
    font-weight: 750;
    color: #111827;
    margin-bottom: 12px;
    line-height: 1.45;
}

.service-text {
    color: #64748B;
    font-size: 14px;
    line-height: 1.8;
}

/* PREMIUM CONTACT PAGE */
[data-testid="stForm"] {
    background: linear-gradient(145deg, #FFFFFF 0%, #F8F7FF 100%);
    border: 1px solid #E5E7FF;
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0 12px 32px rgba(79, 70, 229, 0.08);
}

[data-testid="stForm"] label {
    color: #334155;
    font-weight: 600;
}

[data-testid="stForm"] input,
[data-testid="stForm"] textarea {
    border-radius: 12px;
    border-color: #D8D5F5;
    background: #FFFFFF;
}

[data-testid="stForm"] input:focus,
[data-testid="stForm"] textarea:focus {
    border-color: #7C3AED;
    box-shadow: 0 0 0 1px #7C3AED;
}

[data-testid="stForm"] button {
    min-height: 48px;
    border-radius: 12px;
    font-weight: 700;
}

/* ==========================================
   CREATIVE MOTION UPGRADE — ALL PAGES
   ========================================== */

/* Smooth page transitions and colorful accents */
.stApp {
    background:
        radial-gradient(ellipse at 5% 5%, rgba(167, 139, 250, 0.16), transparent 32%),
        radial-gradient(ellipse at 95% 45%, rgba(196, 181, 253, 0.18), transparent 30%),
        radial-gradient(ellipse at 45% 100%, rgba(224, 231, 255, 0.45), transparent 38%),
        #F8FAFC;
}

/* Animated entrance for content cards across pages */
.service-card,
.project-card,
.stat-card,
.approach-card {
    animation: creativeRiseIn 0.75s cubic-bezier(0.2, 0.75, 0.25, 1) both;
    will-change: transform, opacity;
}

/* Stagger card entrance for a smoother effect */
.service-card:nth-of-type(2),
.project-card:nth-of-type(2),
.stat-card:nth-of-type(2),
.approach-card:nth-of-type(2) {
    animation-delay: 0.10s;
}

.service-card:nth-of-type(3),
.project-card:nth-of-type(3),
.stat-card:nth-of-type(3),
.approach-card:nth-of-type(3) {
    animation-delay: 0.18s;
}

.service-card:nth-of-type(4),
.project-card:nth-of-type(4),
.stat-card:nth-of-type(4) {
    animation-delay: 0.26s;
}

@keyframes creativeRiseIn {
    from {
        opacity: 0;
        transform: translateY(24px) scale(0.985);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

/* Premium glowing hero border */
.hero-box {
    isolation: isolate;
    border: 1px solid rgba(167, 139, 250, 0.25);
    box-shadow:
        0 24px 55px rgba(31, 25, 80, 0.18),
        0 0 35px rgba(124, 58, 237, 0.08);
    transition: box-shadow 0.4s ease, border-color 0.4s ease;
}

.hero-box:hover {
    border-color: rgba(167, 139, 250, 0.6);
    box-shadow:
        0 28px 65px rgba(31, 25, 80, 0.23),
        0 0 45px rgba(124, 58, 237, 0.15);
}

/* More expressive card hover */
.service-card,
.project-card,
.stat-card,
.approach-card {
    transition:
        transform 0.35s cubic-bezier(0.2, 0.75, 0.25, 1),
        box-shadow 0.35s ease,
        border-color 0.35s ease;
}

.service-card:hover,
.project-card:hover,
.stat-card:hover,
.approach-card:hover {
    transform: translateY(-8px);
    border-color: #A78BFA;
    box-shadow: 0 22px 42px rgba(79, 70, 229, 0.15);
}

/* Animated navigation hover */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    transition:
        background 0.25s ease,
        transform 0.25s ease,
        color 0.25s ease;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    transform: translateX(4px);
}

/* Buttons: polished movement and glow */
.stButton > button,
.stLinkButton > a,
[data-testid="stForm"] button {
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        filter 0.25s ease;
}

.stButton > button:hover,
.stLinkButton > a:hover,
[data-testid="stForm"] button:hover {
    transform: translateY(-3px);
    filter: brightness(1.06);
    box-shadow: 0 12px 28px rgba(79, 70, 229, 0.24);
}

/* Headings get a gentle entrance */
.section-title {
    animation: creativeHeadingIn 0.65s ease-out both;
}

@keyframes creativeHeadingIn {
    from {
        opacity: 0;
        transform: translateX(-12px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Mobile layout safety */
@media (max-width: 768px) {
    .hero-box {
        overflow: hidden;
    }

    .service-card:hover,
    .project-card:hover,
    .stat-card:hover,
    .approach-card:hover {
        transform: translateY(-3px);
    }
}

/* Respect visitors who prefer reduced motion */
@media (prefers-reduced-motion: reduce) {
    .service-card,
    .project-card,
    .stat-card,
    .approach-card,
    .section-title,
    .hero-badge,
    .hero-title,
    .hero-subtitle,
    .block-container {
        animation: none !important;
        transition: none !important;
    }
}

/* ==========================================
   ANIMATED SKILLS PROGRESS BARS
   ========================================== */

[data-testid="stProgressBar"] {
    margin-top: 8px;
    margin-bottom: 22px;
    overflow: hidden;
    border-radius: 999px;
    background: #E9E7F5;
    box-shadow: inset 0 1px 3px rgba(31, 25, 80, 0.08);
}

[data-testid="stProgressBar"] [role="progressbar"] {
    border-radius: 999px;
    overflow: hidden;
}

[data-testid="stProgressBar"] [role="progressbar"] > div {
    background: linear-gradient(
        90deg,
        #4F46E5 0%,
        #7C3AED 55%,
        #C4B5FD 100%
    ) !important;
    background-size: 200% 100% !important;
    border-radius: 999px;
    animation:
        skillBarReveal 1.2s cubic-bezier(0.22, 1, 0.36, 1) both,
        skillBarShimmer 3s ease-in-out 1.2s infinite alternate;
    transform-origin: left center;
}

@keyframes skillBarReveal {
    from {
        transform: scaleX(0.03);
        opacity: 0.5;
    }
    to {
        transform: scaleX(1);
        opacity: 1;
    }
}

@keyframes skillBarShimmer {
    from {
        background-position: 0% 50%;
    }
    to {
        background-position: 100% 50%;
    }
}

@media (prefers-reduced-motion: reduce) {
    [data-testid="stProgressBar"] [role="progressbar"] > div {
        animation: none !important;
    }
}

/* ==========================================
   PORTFOLIO — CREATIVE MOTION UPGRADE
   ========================================== */

/* Project images: smooth zoom and rounded corners */
div[data-testid="stImage"] {
    overflow: hidden;
    border-radius: 20px;
    margin-bottom: 14px;
    box-shadow: 0 12px 30px rgba(31, 25, 80, 0.10);
}

div[data-testid="stImage"] img {
    display: block;
    border-radius: 20px;
    transition:
        transform 0.55s cubic-bezier(0.2, 0.75, 0.25, 1),
        filter 0.45s ease;
}

div[data-testid="stImage"]:hover img {
    transform: scale(1.045);
    filter: saturate(1.08);
}

/* Portfolio project cards */
.project-card {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    min-height: 245px;
    border: 1px solid rgba(196, 181, 253, 0.65);
    background:
        radial-gradient(
            circle at 100% 0%,
            rgba(196, 181, 253, 0.22),
            transparent 42%
        ),
        linear-gradient(145deg, #FFFFFF, #F8F7FF);
    box-shadow: 0 12px 30px rgba(79, 70, 229, 0.08);
    transition:
        transform 0.4s cubic-bezier(0.2, 0.75, 0.25, 1),
        box-shadow 0.4s ease,
        border-color 0.4s ease;
}

/* Soft accent glow */
.project-card::before {
    content: "";
    position: absolute;
    z-index: -1;
    top: -65px;
    right: -65px;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background: rgba(167, 139, 250, 0.18);
    filter: blur(28px);
    transition:
        transform 0.45s ease,
        background 0.45s ease;
    pointer-events: none;
}

.project-card:hover {
    transform: translateY(-8px);
    border-color: #A78BFA;
    box-shadow:
        0 24px 48px rgba(79, 70, 229, 0.15),
        0 0 0 1px rgba(167, 139, 250, 0.10);
}

.project-card:hover::before {
    transform: scale(1.5);
    background: rgba(124, 58, 237, 0.25);
}

/* Project title accent */
.project-title {
    transition: color 0.3s ease;
}

.project-card:hover .project-title {
    color: #5B21B6;
}

/* Mobile-friendly hover */
@media (max-width: 768px) {
    .project-card {
        min-height: auto;
        padding: 22px;
    }

    div[data-testid="stImage"]:hover img {
        transform: none;
    }

    .project-card:hover {
        transform: translateY(-3px);
    }
}

/* Motion accessibility */
@media (prefers-reduced-motion: reduce) {
    .project-card,
    .project-card::before,
    .project-title,
    div[data-testid="stImage"] img {
        transition: none !important;
        animation: none !important;
    }

    div[data-testid="stImage"]:hover img {
        transform: none !important;
    }
}
/* ==========================================
   PREMIUM SIDEBAR NAVIGATION
   ========================================== */

section[data-testid="stSidebar"] {
    background:
        radial-gradient(
            circle at 20% 10%,
            rgba(124, 58, 237, 0.20),
            transparent 42%
        ),
        linear-gradient(180deg, #111827, #1E293B);
}

/* Navigation menu items */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 13px;
    transition:
        transform 0.3s ease,
        background 0.3s ease,
        border-color 0.3s ease,
        box-shadow 0.3s ease;
}

/* Elegant hover effect */
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    transform: translateX(5px);
    background: rgba(167, 139, 250, 0.18) !important;
    border-color: rgba(196, 181, 253, 0.40);
    box-shadow: 0 5px 18px rgba(124, 58, 237, 0.12);
}

/* Active navigation item */
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(
        90deg,
        rgba(124, 58, 237, 0.40),
        rgba(167, 139, 250, 0.16)
    ) !important;
    border-color: rgba(196, 181, 253, 0.65);
    box-shadow: 0 5px 20px rgba(124, 58, 237, 0.18);
}

/* Mobile spacing */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1.5rem !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        padding: 11px 13px;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        transform: none;
    }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        transition: none !important;
    }
}
/* ==========================================
   HOME HERO — PREMIUM MOTION UPGRADE
   ========================================== */

.hero-box {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    background: linear-gradient(135deg, #111827, #25204B, #1E293B);
    background-size: 200% 200%;
    animation: heroGradientFlow 9s ease-in-out infinite;
    border: 1px solid rgba(167, 139, 250, 0.22);
    box-shadow: 0 24px 60px rgba(79, 70, 229, 0.16);
}

.hero-box::before {
    content: "";
    position: absolute;
    z-index: -1;
    width: 280px;
    height: 280px;
    top: -120px;
    right: -90px;
    border-radius: 50%;
    background: rgba(167, 139, 250, 0.26);
    filter: blur(55px);
    pointer-events: none;
    animation: heroGlowFloat 7s ease-in-out infinite;
}

.hero-box::after {
    content: "";
    position: absolute;
    z-index: -1;
    width: 220px;
    height: 220px;
    bottom: -130px;
    left: -80px;
    border-radius: 50%;
    background: rgba(79, 70, 229, 0.24);
    filter: blur(50px);
    pointer-events: none;
}

.hero-badge {
    animation: heroBadgeFloat 4s ease-in-out infinite;
}

.hero-title span {
    background: linear-gradient(90deg, #C4B5FD, #A78BFA, #E9D5FF);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

@keyframes heroGradientFlow {
    0%, 100% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
}

@keyframes heroGlowFloat {
    0%, 100% {
        transform: translate(0, 0) scale(1);
    }
    50% {
        transform: translate(-35px, 35px) scale(1.18);
    }
}

@keyframes heroBadgeFloat {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-5px);
    }
}

@media (max-width: 768px) {
    .hero-box::before {
        width: 180px;
        height: 180px;
    }
}

@media (prefers-reduced-motion: reduce) {
    .hero-box,
    .hero-box::before,
    .hero-badge {
        animation: none !important;
    }
}
/* ==========================================
   STATS CARDS — PREMIUM FINISH
   ========================================== */

.stat-card {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(
            circle at 100% 0%,
            rgba(196, 181, 253, 0.28),
            transparent 45%
        ),
        linear-gradient(145deg, #FFFFFF, #F8F7FF);
    border: 1px solid rgba(196, 181, 253, 0.55);
    box-shadow: 0 10px 28px rgba(79, 70, 229, 0.07);
    transition:
        transform 0.35s ease,
        box-shadow 0.35s ease,
        border-color 0.35s ease;
}

.stat-card:hover {
    transform: translateY(-7px) scale(1.015);
    border-color: #A78BFA;
    box-shadow:
        0 18px 38px rgba(79, 70, 229, 0.14),
        0 0 20px rgba(167, 139, 250, 0.10);
}

.stat-number {
    background: linear-gradient(110deg, #4F46E5, #7C3AED, #A78BFA);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    letter-spacing: -1px;
    transition: letter-spacing 0.3s ease;
}

.stat-card:hover .stat-number {
    letter-spacing: 0.5px;
}

.stat-text {
    color: #64748B;
    font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
    .stat-card,
    .stat-number {
        transition: none !important;
    }

    .stat-card:hover {
        transform: none !important;
    }
}

/* ABOUT ME — PREMIUM CREATIVE MOTION */
.service-card,
.approach-card {
    position: relative;
    overflow: hidden;
    isolation: isolate;
    border: 1px solid rgba(167, 139, 250, 0.22);
    transition:
        transform 0.35s ease,
        box-shadow 0.35s ease,
        border-color 0.35s ease;
    animation: aboutCardReveal 0.8s ease both;
}

.service-card::before,
.approach-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(
        120deg,
        transparent 20%,
        rgba(167, 139, 250, 0.12) 50%,
        transparent 80%
    );
    transform: translateX(-120%);
    transition: transform 0.7s ease;
    pointer-events: none;
    z-index: -1;
}

.service-card:hover,
.approach-card:hover {
    transform: translateY(-8px);
    border-color: rgba(124, 58, 237, 0.65);
    box-shadow:
        0 18px 40px rgba(79, 70, 229, 0.15),
        0 0 22px rgba(167, 139, 250, 0.12);
}

.service-card:hover::before,
.approach-card:hover::before {
    transform: translateX(120%);
}

.service-card .service-icon {
    transition: transform 0.35s ease;
}

.service-card:hover .service-icon {
    transform: translateY(-4px) scale(1.12) rotate(-5deg);
}

.approach-card p {
    line-height: 1.9;
}

@keyframes aboutCardReveal {
    from {
        opacity: 0;
        transform: translateY(22px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (prefers-reduced-motion: reduce) {
    .service-card,
    .approach-card {
        animation: none;
        transition: none;
    }

    .service-card:hover,
    .approach-card:hover {
        transform: none;
    }
}

/* SERVICES — ENHANCED MOTION */
.service-card {
    transform-origin: center;
    transition:
        transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1),
        box-shadow 0.4s ease,
        border-color 0.4s ease,
        background 0.4s ease;
    will-change: transform;
}

.service-card:hover {
    transform: translateY(-9px) scale(1.015);
    border-color: rgba(124, 58, 237, 0.7);
    box-shadow:
        0 20px 42px rgba(79, 70, 229, 0.17),
        0 0 24px rgba(167, 139, 250, 0.16);
}

.service-card .service-title {
    transition: color 0.3s ease;
}

.service-card:hover .service-title {
    color: #6D28D9;
}

.service-card .service-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.service-card:hover .service-icon {
    transform: scale(1.14) rotate(-7deg);
}

@media (max-width: 768px) {
    .service-card:hover {
        transform: translateY(-4px);
    }
}

@media (prefers-reduced-motion: reduce) {
    .service-card,
    .service-card .service-title,
    .service-card .service-icon {
        transition: none;
        animation: none;
        will-change: auto;
    }

    .service-card:hover {
        transform: none;
    }
}

/* TOOLS & EXPERTISE — DISTINCT CARD FINISH */
.tools-card {
    min-height: 235px;
    background: linear-gradient(145deg, #ffffff 0%, #f8f7ff 100%);
    border: 1px solid rgba(167, 139, 250, 0.28);
    border-radius: 22px;
    box-shadow: 0 10px 28px rgba(79, 70, 229, 0.07);
}

.tools-card .service-icon {
    background: linear-gradient(135deg, #ede9fe, #ddd6fe);
    box-shadow: 0 5px 16px rgba(124, 58, 237, 0.10);
}

.tools-card .service-title {
    margin-bottom: 12px;
}

.tools-card .service-text {
    line-height: 1.9;
}

.tools-card:hover {
    background: linear-gradient(145deg, #ffffff 0%, #f1edff 100%);
    border-color: #a78bfa;
    box-shadow: 0 18px 38px rgba(79, 70, 229, 0.14);
}

@media (max-width: 768px) {
    .tools-card {
        min-height: auto;
    }
}

/* ==========================================
   PORTFOLIO — STAGGERED ENTRANCE MOTION
   ========================================== */

.project-card {
    animation: portfolioCardEnter 0.75s cubic-bezier(0.2, 0.75, 0.25, 1) both;
}

.project-card:nth-of-type(2) {
    animation-delay: 0.10s;
}

.project-card:nth-of-type(3) {
    animation-delay: 0.18s;
}

.project-card:nth-of-type(4) {
    animation-delay: 0.26s;
}

.project-card:nth-of-type(5) {
    animation-delay: 0.34s;
}

.project-card:nth-of-type(6) {
    animation-delay: 0.42s;
}

.project-card:nth-of-type(7) {
    animation-delay: 0.50s;
}

@keyframes portfolioCardEnter {
    from {
        opacity: 0;
        transform: translateY(24px) scale(0.985);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

/* Animated image highlight */
div[data-testid="stImage"] {
    position: relative;
}

div[data-testid="stImage"] img {
    animation: portfolioImageReveal 0.9s ease both;
}

@keyframes portfolioImageReveal {
    from {
        opacity: 0.65;
        filter: saturate(0.75);
    }
    to {
        opacity: 1;
        filter: saturate(1);
    }
}

/* Respect reduced-motion preferences */
@media (prefers-reduced-motion: reduce) {
    .project-card,
    div[data-testid="stImage"] img {
        animation: none !important;
    }
}

/* HOME HERO — TEXT ENTRANCE MOTION */

.hero-box .hero-title {
    animation: heroTextReveal 0.9s cubic-bezier(0.2, 0.75, 0.25, 1) both;
    animation-delay: 0.12s;
}

.hero-box .hero-subtitle {
    animation: heroTextReveal 1s cubic-bezier(0.2, 0.75, 0.25, 1) both;
    animation-delay: 0.28s;
}

.hero-box .hero-badge {
    animation:
        heroBadgeFloat 4s ease-in-out infinite,
        heroTextReveal 0.7s ease-out both;
}

@keyframes heroTextReveal {
    from {
        opacity: 0;
        transform: translateY(22px);
        filter: blur(4px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}

@media (prefers-reduced-motion: reduce) {
    .hero-box .hero-title,
    .hero-box .hero-subtitle,
    .hero-box .hero-badge {
        animation: none !important;
        filter: none !important;
    }
}
</style>
"""), unsafe_allow_html=True)

# =========================
# HELPER FUNCTIONS
# =========================

def card(icon, title, lines):
    body = "<br>".join(lines)
    html = (
        f'<div class="service-card">'
        f'<div class="service-icon">{icon}</div>'
        f'<div class="service-title">{title}</div>'
        f'<div class="service-text">{body}</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.html("""
<div style="
    background: transparent;
    padding: 10px 5px 20px 5px;
    text-align: center;
    border: none;
    box-shadow: none;
">
    <div style="
        font-size: 28px;
        font-weight: 800;
        color: #A78BFA;
        margin-bottom: 8px;
    ">
        ✨
    </div>

    <div style="
        font-size: 21px;
        font-weight: 800;
        color: #FFFFFF;
    ">
        Syeda Ume Farwa
    </div>

    <div style="
        font-size: 13px;
        color: #CBD5E1;
        margin-top: 6px;
    ">
        Digital Growth Specialist
    </div>
</div>
""")

if "page" not in st.session_state:
    st.session_state.page = "Home"


pages = [
    "Home",
    "About Me",
    "Services",
    "Skills",
    "Portfolio",
    "Contact"
]
def go_to_contact():
    st.session_state["sidebar_navigation"] = "Contact"
page = st.sidebar.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.page),
    key="sidebar_navigation",
)

st.session_state.page = page


# =========================
# HOME
# =========================

if page == "Home":

    hero_left, hero_right = st.columns([1.6, 0.8])

    with hero_left:

        st.html(textwrap.dedent("""
            <div class="hero-box">

                <div class="hero-badge">
                    ✨ DIGITAL GROWTH • DESIGN • SEO • PYTHON
                </div>

                <div class="hero-title">
                    Hi, I'm <span>Syeda Ume Farwa Bukhari</span>
                </div>

                <div class="hero-subtitle">
                    I help businesses build a strong digital presence through
                    creative design, strategic SEO, engaging content,
                    WordPress development and smart Python automation.
                </div>

            </div>
            """))

    with hero_right:

        st.markdown(
        '<div class="profile-image">',
        unsafe_allow_html=True
)

        profile_path = next((Path(__file__).with_name(filename) for filename in ("profile.png", "profile.jpg", "profile.jpeg") if Path(__file__).with_name(filename).is_file()), None)
        if profile_path is not None:
            st.image(str(profile_path), use_container_width=True)
        else:
            st.markdown(
                """
                <div style="height:320px;display:flex;align-items:center;justify-content:center;
                flex-direction:column;background:linear-gradient(135deg,#1E293B,#4F46E5);
                color:white;text-align:center;padding:24px;">
                    <div style="font-size:64px;margin-bottom:12px;">✨</div>
                    <div style="font-size:22px;font-weight:800;">Syeda Ume Farwa Bukhari</div>
                    <div style="font-size:14px;margin-top:8px;color:#E2E8F0;">Digital Growth Specialist</div>
                    <div style="font-size:12px;margin-top:18px;color:#CBD5E1;">Add profile.png beside main.py to show your photo</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    # =========================
    # ANIMATED DIGITAL GROWTH STORY
    # =========================
    components.html("""
    <div class="growth-wrap">
      <div class="growth-heading">From Creative Ideas to <span>Digital Growth</span></div>
      <div class="growth-subheading">A connected process: design, visibility, website, automation and measurable growth.</div>
      <div class="growth-track">
        <div class="growth-line"></div>
        <div class="growth-step step-one"><div class="growth-icon">🎨</div><div class="growth-label">01 · DESIGN</div><div class="growth-detail">Build a clear, memorable brand</div></div>
        <div class="growth-step step-two"><div class="growth-icon">🔎</div><div class="growth-label">02 · SEO</div><div class="growth-detail">Help the right people find you</div></div>
        <div class="growth-step step-three"><div class="growth-icon">🌐</div><div class="growth-label">03 · WEBSITE</div><div class="growth-detail">Turn visits into experiences</div></div>
        <div class="growth-step step-four"><div class="growth-icon">⚙️</div><div class="growth-label">04 · AUTOMATION</div><div class="growth-detail">Make repetitive work simpler</div></div>
        <div class="growth-step step-five"><div class="growth-icon">📈</div><div class="growth-label">05 · GROWTH</div><div class="growth-detail">Connect strategy with results</div></div>
      </div>
      <div class="growth-bottom"><span class="pulse-dot"></span> CREATIVITY <b>+</b> STRATEGY <b>+</b> TECHNOLOGY</div>
    </div>
    <style>
      *{box-sizing:border-box}.growth-wrap{font-family:Inter,Arial,sans-serif;padding:28px 22px 30px;background:radial-gradient(circle at 12% 10%,#ede9fe 0,transparent 35%),linear-gradient(135deg,#fff 0%,#f8fafc 100%);border:1px solid #e2e8f0;border-radius:24px;overflow:hidden;color:#111827;box-shadow:0 15px 38px rgba(15,23,42,.07)}
      .growth-heading{text-align:center;font-size:clamp(22px,3vw,32px);font-weight:800;letter-spacing:-.8px}.growth-heading span{color:#6d4aff}.growth-subheading{text-align:center;color:#64748b;font-size:13px;line-height:1.6;margin:9px auto 28px;max-width:600px}
      .growth-track{position:relative;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;align-items:stretch}.growth-line{position:absolute;left:9%;right:9%;top:38px;height:2px;background:linear-gradient(90deg,#c4b5fd,#818cf8,#a78bfa);opacity:.75}
      .growth-step{position:relative;z-index:1;text-align:center;padding:0 4px;animation:rise-in .7s both}.step-two{animation-delay:.18s}.step-three{animation-delay:.36s}.step-four{animation-delay:.54s}.step-five{animation-delay:.72s}
      .growth-icon{width:76px;height:76px;display:flex;align-items:center;justify-content:center;margin:0 auto 13px;border-radius:22px;background:#fff;border:1px solid #ddd6fe;box-shadow:0 8px 24px rgba(79,70,229,.12);font-size:30px;animation:floaty 3s ease-in-out infinite}.step-two .growth-icon{animation-delay:.2s}.step-three .growth-icon{animation-delay:.4s}.step-four .growth-icon{animation-delay:.6s}.step-five .growth-icon{animation-delay:.8s}
      .growth-label{font-size:11px;font-weight:800;letter-spacing:.7px;color:#4f46e5}.growth-detail{font-size:11px;color:#64748b;line-height:1.5;margin-top:7px}.growth-bottom{display:flex;align-items:center;justify-content:center;gap:9px;margin-top:28px;font-size:10px;letter-spacing:1.3px;font-weight:800;color:#475569}.growth-bottom b{color:#8b5cf6}.pulse-dot{width:8px;height:8px;border-radius:50%;background:#8b5cf6;box-shadow:0 0 0 5px #ede9fe;animation:pulse 1.7s infinite}
      @keyframes rise-in{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}@keyframes pulse{0%,100%{box-shadow:0 0 0 4px #ede9fe}50%{box-shadow:0 0 0 8px rgba(237,233,254,.5)}}
      @media(max-width:600px){.growth-wrap{padding:22px 12px}.growth-track{grid-template-columns:1fr;gap:18px}.growth-line{left:37px;right:auto;top:30px;bottom:30px;width:2px;height:auto}.growth-step{display:grid;grid-template-columns:66px 1fr;text-align:left;column-gap:12px;align-items:center}.growth-icon{grid-row:span 2;width:58px;height:58px;border-radius:17px;margin:0;font-size:24px}.growth-label{align-self:end}.growth-detail{align-self:start;margin-top:4px}.growth-bottom{font-size:9px;letter-spacing:.8px;flex-wrap:wrap}}
    </style>
    <script>
      document.querySelectorAll('.growth-step').forEach((step) => {
        step.addEventListener('mouseenter', () => step.style.filter = 'drop-shadow(0 6px 12px rgba(79,70,229,.16))');
        step.addEventListener('mouseleave', () => step.style.filter = '');
      });
    </script>
    """, height=460, scrolling=False)

    st.write("")

    col1, col2 = st.columns([1.25, 0.75])

    with col1:

        st.markdown(
            '<div class="section-title">Turning Ideas Into Digital Growth</div>',
            unsafe_allow_html=True
        )

        st.html(textwrap.dedent("""
            <div class="section-text">
                I combine <b>creativity, technology and digital strategy</b>
                to create solutions that help brands stand out online.
                <br><br>
                Whether you need a professional website, better search visibility,
                engaging social media content or workflow automation,
                I focus on creating work that is both <b>beautiful and effective.</b>
            </div>
            """))

        st.write("")

        button1, button2 = st.columns(2)

        with button1:
            if st.button("🚀 Hire Me", use_container_width=True):
                st.session_state.page = "Contact"
                st.session_state.sidebar_navigation = "Contact"
                st.rerun()

        with button2:
            if st.button("📂 Explore My Work", use_container_width=True):
                st.session_state.page = "Portfolio"
                st.session_state.sidebar_navigation = "Portfolio"
                st.rerun()

    with col2:

        st.html(textwrap.dedent("""
            <div class="service-card">

                <div class="service-icon">💡</div>

                <div class="service-title">
                    Why Work With Me?
                </div>

                <div class="service-text">
                    <b>Creative Thinking</b><br>
                    Modern and engaging visual solutions.

                    <br><br>

                    <b>Growth Focused</b><br>
                    Strategies designed around visibility and results.

                    <br><br>

                    <b>Technology Driven</b><br>
                    Smart websites, automation and digital workflows.
                </div>

            </div>
            """))

    st.write("")

    st.markdown(
        '<div class="section-title">What I Bring</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.html(textwrap.dedent("""
        <div class="stat-card">
            <div class="stat-number">6+</div>
            <div class="stat-text">Digital Skills</div>
        </div>
        """))

    with col2:
        st.html(textwrap.dedent("""
        <div class="stat-card">
            <div class="stat-number">10+</div>
            <div class="stat-text">Creative Projects</div>
        </div>
        """))

    with col3:
        st.html(textwrap.dedent("""
        <div class="stat-card">
            <div class="stat-number">5+</div>
            <div class="stat-text">Digital Services</div>
        </div>
        """))

    
    with col4:

        st.html(textwrap.dedent("""
        <div class="stat-card">
            <div class="stat-number">100%</div>
            <div class="stat-text">Creative Focus</div>
        </div>
        """))

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.html(textwrap.dedent("""
            <div class="service-card">
                <div class="service-icon">🎨</div>
                <div class="service-title">Creative Design</div>
                <div class="service-text">
                    Professional graphic design, branding,
                    social media creatives and visual content.
                </div>
            </div>
            """))

    with c2:
        st.html(textwrap.dedent("""
            <div class="service-card">
                <div class="service-icon">📈</div>
                <div class="service-title">SEO & Growth</div>
                <div class="service-text">
                    Keyword research, on-page SEO,
                    off-page SEO and digital growth strategies.
                </div>
            </div>
            """))

    with c3:
        st.html(textwrap.dedent("""
            <div class="service-card">
                <div class="service-icon">⚙️</div>
                <div class="service-title">Web & Automation</div>
                <div class="service-text">
                    WordPress websites, Python automation
                    and efficient digital workflows.
                </div>
            </div>
            """))

    st.write("")

    st.markdown(
        '<div class="section-title">My Digital Expertise</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">From creative ideas to digital growth, I combine design, technology and strategy to build better online experiences.</div>',
        unsafe_allow_html=True
    )

    st.write("")
    
    st.markdown(
    '<div class="section-title">Core Skills</div>',
    
    unsafe_allow_html=True
)

    skill1, skill2 = st.columns(2)

    with skill1:
        st.markdown("**🎨 Graphic Design**")
        st.progress(90)

        st.markdown("**🔍 SEO & Digital Marketing**")
        st.progress(85)

        st.markdown("**🌐 WordPress Development**")
        st.progress(80)

    with skill2:
        st.markdown("**🎬 Video Editing**")
        st.progress(88)

        st.markdown("**📱 Social Media Management**")
        st.progress(85)

        st.markdown("**🐍 Python Automation**")
        st.progress(75)

    st.write("")
    st.markdown('<div class="section-title">Featured Work</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">A quick look at some of the creative and digital projects I work on.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    project1, project2, project3 = st.columns(3)

    with project1:
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">🎨</div>
            <div class="project-title">Creative Design</div>
            <div class="project-text">
                Branding, social media creatives and
                professional visual content for businesses.
            </div>
        </div>
        """))

    with project2:
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">📈</div>
            <div class="project-title">SEO & Digital Growth</div>
            <div class="project-text">
                SEO strategies focused on improving
                visibility, traffic and online presence.
            </div>
        </div>
        """))

    with project3:
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">🐍</div>
            <div class="project-title">Python Automation</div>
            <div class="project-text">
                Smart automation solutions that simplify
                repetitive digital tasks and workflows.
            </div>
        </div>
        """))
    st.write("")

    if st.button("📂 View All Projects", use_container_width=True):
        st.session_state.page = "Portfolio"
        st.session_state.sidebar_navigation = "Portfolio"
        st.rerun()
# =========================
# ABOUT
# =========================

elif page == "About Me":

    st.markdown(
        '<div class="section-title">About Me</div>',
        unsafe_allow_html=True
    )

    st.html(textwrap.dedent("""
        <div class="section-text">
            I’m Syeda Ume Farwa Bukhari, a Digital Growth Specialist
            passionate about combining creativity, technology and strategy
            to help businesses build a stronger online presence.
        </div>
        """))

    st.write("")

    about1, about2 = st.columns([1.2, 0.8])

    with about1:

        st.html(textwrap.dedent("""
            <div class="service-card">

                <div class="service-icon">✨</div>

                <div class="service-title">
                    Creative + Digital Mindset
                </div>

                <div class="service-text">
                    I work across graphic design, SEO, content creation,
                    WordPress development, social media and Python automation.
                    <br><br>
                    My goal is simple: create digital solutions that look
                    professional, communicate clearly and support real
                    business growth.
                </div>

            </div>
            """))

    with about2:

        st.html(textwrap.dedent("""
            <div class="service-card">

                <div class="service-icon">🚀</div>

                <div class="service-title">
                    What I Focus On
                </div>

                <div class="service-text">
                    🎨 Creative Design<br><br>
                    🔍 SEO & Digital Growth<br><br>
                    🌐 WordPress Development<br><br>
                    🐍 Python Automation
                </div>

            </div>
            """))

    st.write("")

    st.markdown(
        '<div class="section-title">My Approach</div>',
        unsafe_allow_html=True
    )

    
    st.html(textwrap.dedent("""
      <div class="approach-card">
        <p>
            I believe great digital work comes from the right balance of
            creativity, strategy and technology. I focus on understanding
            the goal first, then creating a solution that is practical,
            visually strong and results-focused.
        </p>
    </div>
    """))

# =========================
# SERVICES
# =========================

elif page == "Services":

    st.markdown(
        '<div class="section-title">My Services</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">Professional digital services for businesses, brands and creators.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    services = [
        (
            "🎬",
            "Video Editing & Content Creation",
            "Short-form Reels, YouTube Shorts, TikTok videos, long-form editing, captions and visual effects."
        ),
        (
            "🎨",
            "Graphic Design & Branding",
            "Social media posts, thumbnails, carousel designs, promotional graphics and branding materials."
        ),
        (
            "🌐",
            "WordPress Development",
            "Modern, responsive and professional WordPress websites for businesses and personal brands."
        ),
        (
            "🔍",
            "SEO Strategy",
            "Keyword research, on-page SEO, technical SEO, off-page SEO and authority building."
        ),
        (
            "📱",
            "Social Media Management",
            "Content planning, publishing, engagement and social media growth strategies."
        ),
        (
            "🐍",
            "Python Automation",
            "Custom Python scripts, data processing, web automation and workflow solutions."
        )
    ]

    for i in range(0, len(services), 2):

        col1, col2 = st.columns(2)

        with col1:
            icon, title, text = services[i]

            st.html(textwrap.dedent(f"""
            <div class="service-card">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-text">{text}</div>
            </div>
            """))

        if i + 1 < len(services):

            with col2:
                icon, title, text = services[i + 1]

                st.html(textwrap.dedent(f"""
                <div class="service-card">
                    <div class="service-icon">{icon}</div>
                    <div class="service-title">{title}</div>
                    <div class="service-text">{text}</div>
                </div>
                """))


# =========================
# SKILLS
# =========================

elif page == "Skills":

    st.markdown(
        '<div class="section-title">My Skills</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">A combination of creative, technical and digital growth skills.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    skill1, skill2 = st.columns(2)

    with skill1:

        st.markdown("### 🎨 Creative Skills")

        st.markdown("**Graphic Design**")
        st.progress(90)

        st.markdown("**Video Editing**")
        st.progress(88)

        st.markdown("**Content Creation**")
        st.progress(85)

        st.markdown("**Branding & Visual Design**")
        st.progress(85)

    with skill2:

        st.markdown("### 💻 Digital & Technical Skills")

        st.markdown("**SEO & Digital Marketing**")
        st.progress(85)

        st.markdown("**WordPress Development**")
        st.progress(80)

        st.markdown("**Social Media Management**")
        st.progress(85)

        st.markdown("**Python Automation**")
        st.progress(75)

    st.write("")

    
    
    st.markdown(
        '<div class="section-title">Tools & Expertise</div>',
        unsafe_allow_html=True
    )

    tools1, tools2, tools3 = st.columns(3)

    with tools1:
        st.html(textwrap.dedent("""
        <div class="service-card tools-card">
            <div class="service-icon">🎨</div>
            <div class="service-title">Design</div>
            <div class="service-text">
                Graphic Design<br>
                Branding<br>
                Social Media Creatives
            </div>
        </div>
        """))

    with tools2:
        st.html(textwrap.dedent("""
        <div class="service-card tools-card">
            <div class="service-icon">📈</div>
            <div class="service-title">Digital Growth</div>
            <div class="service-text">
                SEO Strategy<br>
                Content Strategy<br>
                Social Media
            </div>
        </div>
        """))

    with tools3:
        st.html(textwrap.dedent("""
        <div class="service-card tools-card">
            <div class="service-icon">⚙️</div>
            <div class="service-title">Technology</div>
            <div class="service-text">
                WordPress<br>
                Python<br>
                Automation
            </div>
        </div>
        """))

# =========================
# PORTFOLIO
# =========================


elif page == "Portfolio":

    st.markdown(
        '<div class="section-title">Featured Work</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">A selection of digital projects, creative work and technology solutions for brands and businesses.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # ROW 1 — Creative Design and Video Editing
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.image("assets/graphic_design.png", use_container_width=True)
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">🎨</div>
            <div class="project-title">Creative Design & Branding</div>
            <div class="project-text">
                Social media graphics, YouTube thumbnails,
                promotional designs and professional brand visuals.
            </div>
            <br>
            <b>Graphic Design · Branding · Social Media</b>
        </div>
        """))

    with col2:
        st.image("assets/seo_project.png", use_container_width=True)
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">🎬</div>
            <div class="project-title">Video Editing & Content</div>
            <div class="project-text">
                Engaging YouTube Shorts, Reels, educational videos
                and social media content designed for audience growth.
            </div>
            <br>
            <b>Video Editing · Shorts · Content Creation</b>
        </div>
        """))

    st.write("")

    # ROW 2 — SEO and Website Development
    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.image("assets/video_editing.jpg", use_container_width=True)
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">📈</div>
            <div class="project-title">SEO & Digital Growth</div>
            <div class="project-text">
                Keyword research, on-page optimization,
                off-page SEO and strategies to improve
                online visibility.
            </div>
            <br>
            <b>SEO · Keywords · Organic Growth</b>
        </div>
        """))

    with col4:
        st.image(
            "assets/Creative Website Development Workspace.png",
            use_container_width=True
        )
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">🌐</div>
            <div class="project-title">Website Development</div>
            <div class="project-text">
                Modern, responsive websites for businesses,
                personal brands and professional portfolios.
            </div>
            <br>
            <b>Web Design · Responsive Websites</b>
        </div>
        """))

    st.write("")

    # ROW 3 — WordPress and Social Media
    col5, col6 = st.columns(2, gap="large")

    with col5:
        st.image("assets/wordpress.png", use_container_width=True)
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">💻</div>
            <div class="project-title">WordPress Development</div>
            <div class="project-text">
                Professional website design, responsive layouts
                and user-friendly WordPress experiences.
            </div>
            <br>
            <b>WordPress · Web Design · Responsive Websites</b>
        </div>
        """))

    with col6:
        st.image(
            "assets/Modern Social Media Management Dashboard.png",
            use_container_width=True
        )
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">📱</div>
            <div class="project-title">Social Media Management</div>
            <div class="project-text">
                Content planning, post scheduling, audience
                engagement and brand growth strategies.
            </div>
            <br>
            <b>Social Media · Content Planning · Engagement</b>
        </div>
        """))

    st.write("")

    # ROW 4 — Python Automation
    col7, empty_col = st.columns(2, gap="large")

    with col7:
        st.image("assets/python-automation.png", use_container_width=True)
        st.html(textwrap.dedent("""
        <div class="project-card">
            <div class="service-icon">🐍</div>
            <div class="project-title">Python Automation</div>
            <div class="project-text">
                Smart automation solutions that reduce repetitive
                work and improve digital workflows.
            </div>
            <br>
            <b>Python · Automation · Productivity</b>
        </div>
        """))

    st.write("")

    st.markdown(
        '<div class="section-title">Have a project in mind?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">Let\'s turn your idea into a professional digital experience.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "🚀 Let's Work Together",
        use_container_width=True,
        on_click=go_to_contact
    )

# =========================
# CONTACT
# =========================

elif page == "Contact":

    st.markdown(
        '<div class="section-title">Let\'s Work Together</div>',
        unsafe_allow_html=True
    )

    st.html(textwrap.dedent("""
        <div class="section-text">
            Have a project, business idea or digital challenge?
            Tell me what you need and let's create something great together.
        </div>
        """))

    st.write("")

    col1, col2 = st.columns([0.8, 1.2])

    with col1:

        st.html(textwrap.dedent("""
<div class="service-card">

    <div class="service-icon">🚀</div>

    <div class="service-title">
        Let's Build Something Great
    </div>

    <div class="service-text">
        I'm available for freelance projects and digital growth work.
        <br><br>

        <b>SEO & Digital Growth</b><br>
        Improve your online visibility.
        <br><br>

        <b>Creative Design</b><br>
        Build a strong visual identity.
        <br><br>

        <b>Web & Automation</b><br>
        Create smarter digital workflows.
    </div>

</div>
"""))

    with col2:

        with st.form("contact_form"):

            st.markdown(
                '<div class="project-title">Send Me a Message</div>',
                unsafe_allow_html=True
            )

            st.write("")

            name = st.text_input(
                "Your Name",
                placeholder="Enter your name"
            )

            email = st.text_input(
                "Your Email",
                placeholder="Enter your email"
            )

            service = st.selectbox(
                "What service do you need?",
                [
                    "SEO & Digital Marketing",
                    "Graphic Design & Branding",
                    "Video Editing",
                    "WordPress Development",
                    "Social Media Management",
                    "Python Automation",
                    "Other"
                ]
            )

            message = st.text_area(
                "Tell me about your project",
                placeholder="Write a short description of your project..."
            )

            submitted = st.form_submit_button(
                "📩 Send Message",
                use_container_width=True
            )

            
            if submitted:
                if name.strip() and email.strip() and message.strip():
                    payload = {
                        "service_id": "service_yg83qhh",
                        "template_id": "template_xe5osmb",
                        "user_id": "MDv3zMI4GMQt2ID_V",
                        "accessToken": st.secrets["EMAILJS_PRIVATE_KEY"],
                        "template_params": {
                            "name": name.strip(),
                            "email": email.strip(),
                            "service": service,
                            "message": message.strip(),
                        },
                    }

                    request = urllib.request.Request(
                        "https://api.emailjs.com/api/v1.0/email/send",
                        data=json.dumps(payload).encode("utf-8"),
                        headers={
                          "Content-Type": "application/json",
                          "User-Agent": "Mozilla/5.0",
                        },
                        method="POST",
                    )

                    try:
                        with urllib.request.urlopen(
                            request, timeout=20
                        ) as response:
                            if response.status == 200:
                                st.success(
                                    "Thank you! Your message has been sent successfully."
                                )
                            else:
                                st.error(
                                    f"Email could not be sent. Status: {response.status}"
                                )

                    except urllib.error.HTTPError as error:
                        details = error.read().decode(
                            "utf-8", errors="replace"
                        )
                        st.error(
                            f"EmailJS error ({error.code}): {details}"
                        )

                    except Exception as error:
                        st.error(
                            f"Message could not be sent: {error}"
                        )

                else:
                    st.warning(
                        "Please fill in your name, email and message."
                    )

st.divider()

st.markdown(
    "<h3 style='text-align:center; color:#312E81;'>✨ Syeda Ume Farwa Bukhari</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#64748B;'>Digital Growth Specialist · Creative Designer · SEO &amp; Python Specialist</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#4F46E5; font-weight:700;'>Let's Connect</p>",
    unsafe_allow_html=True
)


social1, social2, social3 = st.columns(3)

with social1:
    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/farwa-bukhari-a3b1a7328/",
        use_container_width=True
    )

with social2:
    st.link_button(
        "📸 Instagram",
        "https://www.instagram.com/farwabukhari2/",
        use_container_width=True
    )

with social3:
    st.link_button(
        "✉️ Email Me",
        "mailto:farwabukhari5667@gmail.com",
        use_container_width=True
    )

st.caption("© 2026 Syeda Ume Farwa Bukhari. All Rights Reserved.")

