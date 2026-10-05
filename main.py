import streamlit as st

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
st.markdown("""
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
}

/* Portfolio */
.project-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #E2E8F0;
    margin-bottom: 20px;
}

.project-title {
    font-size: 20px;
    font-weight: 700;
    color: #111827;
}

.project-text {
    color: #64748B;
    line-height: 1.7;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    padding: 10px 25px;
}

/* Footer */
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
</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

st.sidebar.markdown(
    """
    <div style="
        padding: 10px 5px 20px 5px;
        text-align: center;
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
    """,
    unsafe_allow_html=True
)

st.sidebar.write("---")

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

page = st.sidebar.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = page


# =========================
# HOME
# =========================

if page == "Home":

    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1.25, 0.75])

    with col1:

        st.markdown(
            '<div class="section-title">Turning Ideas Into Digital Growth</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="section-text">
                I combine <b>creativity, technology and digital strategy</b>
                to create solutions that help brands stand out online.
                <br><br>
                Whether you need a professional website, better search visibility,
                engaging social media content or workflow automation,
                I focus on creating work that is both <b>beautiful and effective.</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        button1, button2 = st.columns(2)

        with button1:
            if st.button("🚀 Hire Me", use_container_width=True):
                st.session_state.page = "Contact"
                st.rerun()

        with button2:
            if st.button("📂 Explore My Work", use_container_width=True):
                st.session_state.page = "Portfolio"
                st.rerun()

    with col2:

        st.markdown(
            """
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
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.markdown(
        '<div class="section-title">What I Bring</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">6+</div>
            <div class="stat-text">Digital Skills</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">10+</div>
            <div class="stat-text">Creative Projects</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">5+</div>
            <div class="stat-text">Digital Services</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">100%</div>
            <div class="stat-text">Creative Focus</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">🎨</div>
                <div class="service-title">Creative Design</div>
                <div class="service-text">
                    Professional graphic design, branding,
                    social media creatives and visual content.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">📈</div>
                <div class="service-title">SEO & Growth</div>
                <div class="service-text">
                    Keyword research, on-page SEO,
                    off-page SEO and digital growth strategies.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">⚙️</div>
                <div class="service-title">Web & Automation</div>
                <div class="service-text">
                    WordPress websites, Python automation
                    and efficient digital workflows.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

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
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">🎨</div>
            <div class="project-title">Creative Design</div>
            <div class="project-text">
                Branding, social media creatives and
                professional visual content for businesses.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with project2:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">📈</div>
            <div class="project-title">SEO & Digital Growth</div>
            <div class="project-text">
                SEO strategies focused on improving
                visibility, traffic and online presence.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with project3:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">🐍</div>
            <div class="project-title">Python Automation</div>
            <div class="project-text">
                Smart automation solutions that simplify
                repetitive digital tasks and workflows.
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.write("")

    if st.button("📂 View All Projects", use_container_width=True):
        st.session_state.page = "Portfolio"
        st.rerun()
# =========================
# ABOUT
# =========================

elif page == "About Me":

    st.markdown(
        '<div class="section-title">About Me</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-text">
            I’m Syeda Ume Farwa Bukhari, a Digital Growth Specialist
            passionate about combining creativity, technology and strategy
            to help businesses build a stronger online presence.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    about1, about2 = st.columns([1.2, 0.8])

    with about1:

        st.markdown(
            """
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
            """,
            unsafe_allow_html=True
        )

    with about2:

        st.markdown(
            """
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
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.markdown(
        '<div class="section-title">My Approach</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-text">
            I believe great digital work comes from the right balance of
            creativity, strategy and technology. I focus on understanding
            the goal first, then creating a solution that is practical,
            visually strong and results-focused.
        </div>
        """,
        unsafe_allow_html=True
    )


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

            st.markdown(f"""
            <div class="service-card">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

        if i + 1 < len(services):

            with col2:
                icon, title, text = services[i + 1]

                st.markdown(f"""
                <div class="service-card">
                    <div class="service-icon">{icon}</div>
                    <div class="service-title">{title}</div>
                    <div class="service-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)


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
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">🎨</div>
            <div class="service-title">Design</div>
            <div class="service-text">
                Graphic Design<br>
                Branding<br>
                Social Media Creatives
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tools2:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">📈</div>
            <div class="service-title">Digital Growth</div>
            <div class="service-text">
                SEO Strategy<br>
                Content Strategy<br>
                Social Media
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tools3:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">⚙️</div>
            <div class="service-title">Technology</div>
            <div class="service-text">
                WordPress<br>
                Python<br>
                Automation
            </div>
        </div>
        """, unsafe_allow_html=True)


# =========================
# PORTFOLIO
# =========================

elif page == "Portfolio":

    st.markdown(
        '<div class="section-title">Featured Work</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">A selection of digital projects, creative work and technology solutions I can provide for brands and businesses.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">🎨</div>
            <div class="project-title">Creative Design & Branding</div>
            <div class="project-text">
                Social media graphics, YouTube thumbnails,
                promotional designs and professional brand visuals.
            </div>
            <br>
            <b>Graphic Design • Branding • Social Media</b>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">🎬</div>
            <div class="project-title">Video Editing & Content</div>
            <div class="project-text">
                Engaging YouTube Shorts, Reels, educational videos
                and social media content designed for audience growth.
            </div>
            <br>
            <b>Video Editing • Shorts • Content Creation</b>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">🔍</div>
            <div class="project-title">SEO & Digital Growth</div>
            <div class="project-text">
                Keyword research, on-page optimization,
                off-page SEO and strategies focused on improving
                online visibility.
            </div>
            <br>
            <b>SEO • Keywords • Organic Growth</b>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">🌐</div>
            <div class="project-title">Website Development</div>
            <div class="project-text">
                Modern and responsive websites for businesses,
                personal brands and professional portfolios.
            </div>
            <br>
            <b>WordPress • Web Design • Responsive</b>
        </div>
        """, unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    with col5:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">🐍</div>
            <div class="project-title">Python Automation</div>
            <div class="project-text">
                Smart automation solutions that reduce repetitive
                work and improve digital workflows.
            </div>
            <br>
            <b>Python • Automation • Productivity</b>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class="project-card">
            <div class="service-icon">📱</div>
            <div class="project-title">Social Media Management</div>
            <div class="project-text">
                Content planning, creative posting, engagement
                and strategies designed to build a stronger
                social media presence.
            </div>
            <br>
            <b>Social Media • Content • Growth</b>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

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

    if st.button("🚀 Let's Work Together", use_container_width=True):
        st.session_state.page = "Contact"
        st.rerun()


# =========================
# CONTACT
# =========================

elif page == "Contact":

    st.markdown(
        '<div class="section-title">Let\'s Work Together</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-text">
            Have a project, business idea or digital challenge?
            Tell me what you need and let's create something great together.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns([0.8, 1.2])

    with col1:

        st.markdown("""
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
""", unsafe_allow_html=True)

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

                if name and email and message:

                    st.success(
                        "Thank you! Your message has been received."
                    )

                else:

                    st.warning(
                        "Please fill in your name, email and message."
                    )


st.divider()

st.markdown("### ✨ Syeda Ume Farwa Bukhari")

st.caption(
    "Digital Growth Specialist • Creative Designer • SEO & Python Specialist"
)
st.write("")

st.markdown("**Let's Connect**")

st.write("💼 LinkedIn  •  🐙 GitHub  •  📸 Instagram")
st.caption(
    "© 2026 Syeda Ume Farwa Bukhari. All Rights Reserved."
)