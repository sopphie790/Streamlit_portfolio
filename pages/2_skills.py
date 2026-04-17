import streamlit as st
import base64
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Skills | Liza Jaime", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Function para sa Image Handling
def get_base64_img(image_path):
    full_path = os.path.join("images", image_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    /* SIDEBAR - Original (Consistent with Home) */
    [data-testid="stSidebar"] {
        background-color: #FFC0CB !important;
        position: relative;
        overflow: hidden;
    }

    [data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(circle, #FFD700 1px, transparent 1.5px),
            radial-gradient(circle, #FFFACD 1.2px, transparent 1.8px);
        background-size: 50px 50px, 90px 90px;
        animation: floatStars 20s linear infinite;
        opacity: 0.9;
    }

    @keyframes floatStars {
        from { background-position: 0 0; }
        to { background-position: 0 -500px; }
    }

    [data-testid="stSidebarNav"] li {
        background-color: rgba(255, 255, 255, 0.75) !important; 
        border-radius: 50px !important;
        margin: 12px 20px !important;
        border: 2px solid #FFD700 !important;
        z-index: 1;
    }

    [data-testid="stSidebarNav"] span {
        color: #000000 !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }

    [data-testid="stSidebarNav"] li svg { display: none !important; }

    .sidebar-footer { text-align: center; margin-top: 20px; z-index: 1; position: relative; }
    .sidebar-logo { width: 150px; border-radius: 10px; border: 2px solid #FFD700; }
    .location-text { color: #000000; font-weight: bold; font-size: 14px; }

    /* SKILLS CONTENT STYLING */
    .skills-title {
        font-size: 85px;
        font-weight: 900;
        color: #333;
        margin-bottom: 0;
    }

    .pink-line-short {
        border-top: 8px solid #FF69B4;
        box-shadow: 0px 5px 15px rgba(255, 105, 180, 0.6);
        border-radius: 10px;
        width: 45%;
        margin: 10px 0 25px 0;
    }

    .stProgress > div > div > div > div {
        background-color: #FF69B4 !important;
    }

    /* --- FIXED FRAME DESIGN --- */
    .inverted-frame-wrapper {
        display: flex;
        flex-direction: column;
        align-items: flex-end; /* Nakadikit sa kanan */
        margin-top: 50px; /* Inadjust para hindi dikit sa title */
        width: 100%;
    }

    .inverted-frame-3d {
        border: 8px solid #FF69B4;
        /* Exact shape: Quarter circle at bottom-left */
        border-radius: 0 0 0 350px !important; 
        width: 320px; 
        height: 320px;
        overflow: hidden;
        box-shadow: -10px 10px 20px rgba(0,0,0,0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        background: white;
    }
    
    .centered-profile-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .photo-editor-top {
        color: #FF69B4;
        font-weight: 900;
        letter-spacing: 3px;
        font-size: 18px;
        margin-bottom: 10px;
        text-align: center;
        width: 320px; /* Kapantay ng frame */
    }

    header { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR CONTENT (Consistent) ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    logo_b64 = get_base64_img("logo1.png")
    if logo_b64:
        st.markdown(f'<div class="sidebar-footer"><img src="data:image/png;base64,{logo_b64}" class="sidebar-logo"><div class="location-text">📍 Aroroy, Masbate, Philippines</div></div>', unsafe_allow_html=True)

# --- 4. HERO SECTION ---
st.markdown('<h1 class="skills-title">SKILLS</h1>', unsafe_allow_html=True)
st.markdown('<div class="pink-line-short"></div>', unsafe_allow_html=True)

# Main layout columns
col_skills, col_img = st.columns([1.2, 1], gap="large")

with col_skills:
    st.write("### ⚡ **Technical Skills**")
    
    # --- PROGRAMMING (Progress Bars) ---
    st.markdown('<h4 style="color: #FF69B4;">💻 Programming</h4>', unsafe_allow_html=True)
    col_py, col_bar_py = st.columns([0.5, 2])
    col_py.write("Python")
    col_bar_py.progress(85)

    col_hc, col_bar_hc = st.columns([0.5, 2])
    col_hc.write("HTML/CSS")
    col_bar_hc.progress(80)

    col_js, col_bar_js = st.columns([0.5, 2])
    col_js.write("JavaScript")
    col_bar_js.progress(70)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- DESIGN (Progress Bars) ---
    st.markdown('<h4 style="color: #FF69B4;">🎨 Design</h4>', unsafe_allow_html=True)
    col_ui, col_bar_ui = st.columns([0.5, 2])
    col_ui.write("UI/UX Design")
    col_bar_ui.progress(80)

    col_cn, col_bar_cn = st.columns([0.5, 2])
    col_cn.write("Canva / Editing")
    col_bar_cn.progress(90)

    # --- ADDED PROFESSIONAL DESIGN SKILLS ---
    col_ph, col_bar_ph = st.columns([0.5, 2])
    col_ph.write("Photography")
    col_bar_ph.progress(75)

    col_br, col_bar_br = st.columns([0.5, 2])
    col_br.write("Branding")
    col_bar_br.progress(85)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- TOOLS & SOFT SKILLS (Compact Cards) ---
    st.write("### 🛠 **Tools & Soft Skills**")
    
    def compact_info_card(title, description, icon="🔹"):
        st.markdown(f"""
            <div style="
                background-color: white; 
                padding: 10px 15px; 
                border-radius: 10px; 
                border-left: 5px solid #FF69B4; 
                box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
                margin-bottom: 8px;
            ">
                <div style="font-size: 14px; font-weight: 800; color: #333;">{icon} {title.upper()}</div>
                <div style="color:#555; font-size:12px; margin-top:2px;">{description}</div>
            </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        compact_info_card("Development Tools", "VS Code, Streamlit, GitHub, Git,", icon="🛠")
        compact_info_card("Virtual Assistance", "Client Management, Administrative Tasks", icon="VA")
        compact_info_card("Data Entry", "Accuracy, Spreadsheet Management", icon="📊")
    with c2:
        compact_info_card("Content Creation", "Social Media, Blog Writing, Marketing", icon="✍️")
        compact_info_card("SEO", "Basic SEO & Social Media Optimization", icon="📈")
        compact_info_card("Team Leadership", "Organizing, Communicating, Supervising", icon="🏆")

with col_img:
    st.markdown('<div class="inverted-frame-wrapper">', unsafe_allow_html=True)
    st.markdown('<p class="photo-editor-top">PHOTO EDITOR</p>', unsafe_allow_html=True)
    img_b64 = get_base64_img("profile.png")
    if img_b64:
        st.markdown(f'''
            <div class="inverted-frame-3d">
                <img src="data:image/png;base64,{img_b64}" class="centered-profile-img">
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="inverted-frame-3d"><p style="text-align:center; padding-top:140px;">Profile Not Found</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)