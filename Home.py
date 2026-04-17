import streamlit as st
import base64
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="About Me | Liza Jaime", 
    layout="wide", 
    initial_sidebar_state="expanded"  # Pinipilit nitong laging nakalabas ang sidebar sa simula
)

# Function para sa Image Handling
def get_base64_img(image_path):
    full_path = os.path.join("images", image_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# --- 2. CUSTOM CSS (Sidebar, Buttons, & Floating Gold Stars) ---
st.markdown("""
    <style>
    /* SIDEBAR - Pink Background with Floating Gold Glitter Stars */
    [data-testid="stSidebar"] {
        background-color: #FFC0CB !important;
        position: relative;
        overflow: hidden;
    }

    /* Floating Gold Stars Animation */
    [data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(circle, #FFD700 1px, transparent 1.5px),
            radial-gradient(circle, #FFFACD 1.2px, transparent 1.8px),
            radial-gradient(circle, #DAA520 1px, transparent 1.5px);
        background-size: 50px 50px, 90px 90px, 70px 70px;
        background-position: 0 0, 30px 50px, 15px 10px;
        animation: floatStars 20s linear infinite;
        opacity: 0.9;
        z-index: 0;
    }

    @keyframes floatStars {
        from { background-position: 0 0, 30px 50px, 15px 10px; }
        to { background-position: 0 -500px, 30px -540px, 15px -490px; }
    }

    /* BUTTONS: BLACK & BOLD TEXT (Readable) */
    [data-testid="stSidebarNav"] li {
        background-color: rgba(255, 255, 255, 0.75) !important; 
        border-radius: 50px !important;
        margin: 12px 20px !important;
        border: 2px solid #FFD700 !important; /* Gold Border para sa buttons */
        transition: 0.3s ease-in-out;
        z-index: 1;
    }

    [data-testid="stSidebarNav"] li:hover {
        background-color: rgba(255, 255, 255, 0.95) !important;
        transform: scale(1.05);
        box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.5);
    }

    [data-testid="stSidebarNav"] span {
        color: #000000 !important; /* BLACK TEXT */
        font-weight: 900 !important; /* EXTRA BOLD */
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    [data-testid="stSidebarNav"] li svg {
        display: none !important;
    }

    /* OVAL PROFILE FRAME */
    .profile-frame {
        border: 6px solid #FF69B4 !important;
        border-radius: 200px !important;
        width: 350px !important;
        height: 500px !important;
        overflow: hidden !important; 
        display: flex !important;
        align-items: center !important; 
        justify-content: center !important;
        margin: auto !important;
        box-shadow: 0px 15px 35px rgba(255, 105, 180, 0.4);
    }
    .profile-img { width: 100% !important; height: 100% !important; object-fit: cover !important; }

    /* 3D PINK LINE */
    .pink-line-3d {
        border-top: 8px solid #FF69B4;
        box-shadow: 0px 5px 12px rgba(255, 105, 180, 0.5);
        border-radius: 10px; margin: 25px 0;
    }

    /* LOGO & LOCATION STYLING */
    .sidebar-footer {
        text-align: center;
        margin-top: 20px;
        z-index: 1;
        position: relative;
    }
    .sidebar-logo {
        width: 150px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 2px solid #FFD700; /* Gold border for logo */
    }
    .location-text {
        color: #000000;
        font-weight: bold;
        font-size: 14px;
        text-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
    }

    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR CONTENT (Nav, Logo, & Location) ---
with st.sidebar:
    # Space for the Nav links at the top
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Photo Editing Logo Section
    logo_b64 = get_base64_img("logo1.png")
    if logo_b64:
        st.markdown(f'''
            <div class="sidebar-footer">
                <img src="data:image/png;base64,{logo_b64}" class="sidebar-logo">
                <div class="location-text">📍 Aroroy, Masbate, Philippines</div>
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="sidebar-footer"><div class="location-text">📍 Aroroy, Masbate, Philippines</div></div>', unsafe_allow_html=True)

# --- 4. MAIN CONTENT ---
col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    img_b64 = get_base64_img("profile.png") 
    if img_b64:
        st.markdown(f'''
            <div class="profile-frame">
                <img src="data:image/profile.png;base64,{img_b64}" class="profile-img">
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="profile-frame"><p style="color: #FF69B4; margin-top: 230px; text-align: center;">Image Not Found</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<br><br><br>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 85px; font-weight: 900; color: #FF69B4; margin-bottom: 0;">LIZA JAIME</h1>', unsafe_allow_html=True)
    st.markdown('<div class="pink-line-3d"></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; color: #FF69B4; letter-spacing: 2px; margin-top: -10px;">STUDENT DEVELOPER | DESIGNER | VA | PHOTO EDITOR</p>', unsafe_allow_html=True)
    st.markdown('''
        <p style="font-size: 18px; color: #555; line-height: 1.8; text-align: justify; max-width: 550px;">
        Welcome to my portfolio dashboard. I am a passionate and driven BS Computer Science student 
        with a strong interest in technology and creative digital services.
        </p>
    ''', unsafe_allow_html=True)