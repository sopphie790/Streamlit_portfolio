import streamlit as st
import base64
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Projects | Liza Jaime", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Function para sa Image Handling (Gagamitin pa rin para sa Sidebar Logo)
def get_base64_img(image_path):
    full_path = os.path.join("images", image_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# --- 2. CUSTOM CSS (SIDEBAR CONSISTENCY & NEW SHOWCASE DESIGN) ---
st.markdown("""
    <style>
    /* SIDEBAR - STRICTLY CONSISTENT WITH HOME/ABOUT/SKILLS */
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

    /* 3D IMAGE SHOWCASE STYLE */
    .showcase-container {
        perspective: 1000px;
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* In-apply ang 3D effect sa Streamlit image component */
    .stImage img {
        width: 100%;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        border: 4px solid white;
    }
    
    .stImage img:hover {
        transform: translateY(-10px) rotateX(5deg);
        box-shadow: 0 15px 35px rgba(255, 105, 180, 0.4);
    }

    /* COMPACT EDU-CARD */
    .compact-edu-card {
        background-color: white;
        padding: 15px;
        border-radius: 0 0 15px 15px;
        border-left: 5px solid #FF69B4;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-top: -15px;
        margin-bottom: 30px;
        position: relative;
        z-index: 1;
    }
    .compact-title {
        color: #FF69B4;
        font-weight: 900;
        font-size: 18px;
        margin-bottom: 5px;
        text-transform: uppercase;
        display: block;
    }
    .compact-desc {
        font-size: 14px;
        color: #666;
        line-height: 1.3;
    }

    /* TABS STYLING */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: white !important;
        border: 2px solid #FF69B4 !important;
        border-radius: 30px !important;
        padding: 8px 20px !important;
        font-weight: bold !important;
        color: #FF69B4 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF69B4 !important;
        color: white !important;
    }

    header { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (CONSISTENT) ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    logo_b64 = get_base64_img("logo1.png")
    if logo_b64:
        st.markdown(f'<div class="sidebar-footer"><img src="data:image/png;base64,{logo_b64}" class="sidebar-logo"><div class="location-text">📍 Aroroy, Masbate, Philippines</div></div>', unsafe_allow_html=True)

# Optimized Helper for Gallery (Direct file reading to avoid crash)
def render_gallery_item(img_name):
    img_path = os.path.join("images", img_name)
    if os.path.exists(img_path):
        st.markdown('<div class="showcase-container">', unsafe_allow_html=True)
        st.image(img_path, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Original Base64 Helper for Projects and Certs (Limited use to avoid memory issues)
def render_3d_only_b64(img_name):
    img_b64 = get_base64_img(img_name)
    if img_b64:
        st.markdown(f'<div class="showcase-container"><img src="data:image/png;base64,{img_b64}" class="img-3d"></div>', unsafe_allow_html=True)

def render_project_compact_b64(title, desc, img_name):
    img_b64 = get_base64_img(img_name)
    if img_b64:
        st.markdown(f'''
            <div class="showcase-container">
                <img src="data:image/png;base64,{img_b64}" class="img-3d" style="border-radius: 15px 15px 0 0;">
                <div class="compact-edu-card">
                    <div class="compact-title">{title}</div>
                    <div class="compact-desc">{desc}</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

# --- 4. MAIN CONTENT ---
st.markdown('<h1 style="font-size: 50px; color: #FF69B4; font-weight: 900;">PORTFOLIO SHOWCASE</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💻 Project Development", "🎨 Photo Editing & VA", "🏆 Certificates"])

# --- TAB 1: 2 COLUMNS ---
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        render_project_compact_b64("🏢 Brgy Information System", "The Barangay Information Management System is a web-based project I developed... This project reflects my growth and passion as a future web developer.", "BIMS.png")
        render_project_compact_b64("💼 Employee Management", "Every line of code and every pixel in this Employee Management System was driven by a commitment to excellence.", "EMPLOYEE_SYSTEM.png")
    with col2:
        # --- DOCUFLOW SYSTEM ---
        render_project_compact_b64(
            "📄 DocuFlow System", 
            """Building on the momentum of the Employee Management System, I developed DocuFlow as a comprehensive final project for Web-Dev 101 under the mentorship of Ma’am Daisy Jean Castillo. This platform was designed to bridge the gap between administrative complexity and operational efficiency, focusing on secure document tracking and seamless approval workflows.""", 
            "DOCUFLOW.png"
        )

        # --- FITQUEST: DAILY HEALTH ADVENTURE ---
        render_project_compact_b64(
            "🎮 Fitquest: Daily Health Adventure", 
            """Developed for our Software Engineering subject under the instruction of Sir Jerard Sopsop, Fitquest is a mobile-inspired solution that gamifies personal wellness. This project demonstrates my ability to apply Software Engineering principles—from requirement analysis to system design—into a functional tool that promotes a healthier lifestyle. By merging health tracking with an 'adventure' mechanic, Fitquest transforms routine physical activities into an engaging digital experience, showcasing my versatility in creating user-centric applications across different domains.""", 
            "mobile_game.png"
        )
# --- TAB 2: PHOTO EDITING (ANG PAGBABAGO AY DITO LANG) ---
with tab2:
    # 3-column distribution for the 44+ images
    p_col1, p_col2, p_col3 = st.columns(3)
    
    # List of all images to display
    col1_images = ["PORTRAIT.jpg"] + [f"image{i}.png" for i in range(1, 13)]
    col2_images = ["LOGO.png"] + [f"image{i}.png" for i in range(13, 30)]
    col3_images = ["VA.png"] + [f"image{i}.png" for i in range(30, 42)]

    with p_col1:
        for img in col1_images: render_gallery_item(img)
    with p_col2:
        for img in col2_images: render_gallery_item(img)
    with p_col3:
        for img in col3_images: render_gallery_item(img)

# --- TAB 3: 3 COLUMNS ---
# --- TAB 3: 3 COLUMNS (3D CERTIFICATES STYLE) ---
with tab3:
    # 3-column layout para sa Certificates
    c_col1, c_col2, c_col3 = st.columns(3)
    
    # Listahan ng iyong certificates
    # Pinagsama-sama ko na dito ang lahat ng files mo para sa loop
    cert_list = [
        "CERTIFICATE1.jpg", "CERTIFICATE2.png", "CERTIFICATE3.png", 
        "CERTIFICATE4.png", "CERTIFICATE5.png", "CERTIFICATE6.png", 
        "CERTIFICATE7.png", "STARMAKER.png", "CERTIFICATE8.png", 
        "CERTIFICATE9.png", "CERTIFICATE10.png"
    ]
    
    # Automatic Distribution Loop para maging 3D card style
    for index, cert_name in enumerate(cert_list):
        # Pinipili nito ang column (0, 1, o 2)
        target_col = [c_col1, c_col2, c_col3][index % 3]
        with target_col:
            # Gagamitin ang optimized function para sa 3D effect at mabilis na loading
            render_gallery_item(cert_name)