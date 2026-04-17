import streamlit as st
import base64
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="About Me | Liza Jaime", 
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
    /* CONSISTENT SIDEBAR STYLE (From Home) */
    [data-testid="stSidebar"] { background-color: #FFC0CB !important; position: relative; overflow: hidden; }
    [data-testid="stSidebar"]::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(circle, #FFD700 1px, transparent 1.5px), radial-gradient(circle, #FFFACD 1.2px, transparent 1.8px);
        background-size: 50px 50px, 90px 90px; animation: floatStars 20s linear infinite; opacity: 0.9;
    }
    @keyframes floatStars { from { background-position: 0 0; } to { background-position: 0 -500px; } }
    [data-testid="stSidebarNav"] li { background-color: rgba(255, 255, 255, 0.75) !important; border-radius: 50px !important; margin: 12px 20px !important; border: 2px solid #FFD700 !important; }
    [data-testid="stSidebarNav"] span { color: #000000 !important; font-weight: 900 !important; text-transform: uppercase; }
    [data-testid="stSidebarNav"] li svg { display: none !important; }
    .sidebar-footer { text-align: center; margin-top: 20px; z-index: 1; position: relative; }
    .sidebar-logo { width: 150px; border-radius: 10px; border: 2px solid #FFD700; }
    .location-text { color: #000000; font-weight: bold; font-size: 14px; }

    /* CONTENT STYLING */
    .about-title { font-size: 85px; font-weight: 900; color: #FF69B4; margin-bottom: 0; }
    .pink-line-short { border-top: 8px solid #FF69B4; box-shadow: 0px 5px 15px rgba(255, 105, 180, 0.6); border-radius: 10px; width: 45%; margin: 10px 0 25px 0; }
    
    /* LIFTED FRAME ADJUSTMENT - PINASIMPLE PARA SA MEMORY */
    .fan-frame-container { 
        position: relative; 
        width: 100%; 
        max-width: 450px; 
        margin: auto; 
        margin-top: -160px; 
    } 

    .fan-frame-3d { 
        border: 8px solid #FF69B4; 
        border-radius: 400px 0 0 0 !important; 
        width: 350px; 
        height: 450px; 
        overflow: hidden !important; /* Pinaka-importante para hindi lumabas ang image */
        box-shadow: -15px 15px 30px rgba(0,0,0,0.2); 
        margin: auto; 
        display: block;
        background-color: white;
    }

    /* Target direct images para sa st.image */
    .fan-frame-3d img { 
        width: 100% !important; 
        height: 100% !important; 
        object-fit: cover !important; 
        border-radius: 400px 0 0 0; 
    }

    .photo-editor-top { 
        text-align: center; 
        color: #FF69B4; 
        font-weight: 900; 
        letter-spacing: 5px; 
        font-size: 24px; 
        margin-bottom: 5px; 
    }
    /* CUSTOM BUTTONS (Replacing Tabs) */
    div.stButton > button {
        background-color: #FF69B4 !important; color: white !important;
        border-radius: 20px !important; width: 100% !important;
        font-weight: bold !important; border: 2px solid #FFD700 !important;
        transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #FF1493 !important; transform: scale(1.05); }

    header { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR CONTENT ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    logo_b64 = get_base64_img("logo1.png")
    if logo_b64:
        st.markdown(f'<div class="sidebar-footer"><img src="data:image/png;base64,{logo_b64}" class="sidebar-logo"><div class="location-text">📍 Aroroy, Masbate, Philippines</div></div>', unsafe_allow_html=True)

# --- 4. HERO SECTION ---
st.markdown('<h1 class="about-title">ABOUT ME</h1>', unsafe_allow_html=True)
st.markdown('<div class="pink-line-short"></div>', unsafe_allow_html=True)

# Main layout columns
col_text, col_img = st.columns([1.2, 1], gap="large")

with col_text:
    st.write("""
    I am a Bachelor of Science in Computer Science student passionate about building real-world systems and creative digital services.
    """)
    
    # --- 5. NAVIGATION BUTTONS (REPLACING TABS) ---
    st.write("### **MY INFORMATION**")
    btn_col1, btn_col2, btn_col3 = st.columns(3)
    btn_col4, btn_col5, btn_col6 = st.columns(3)

    # State management for buttons
    if 'about_page' not in st.session_state:
        st.session_state.about_page = 'Education'

    if btn_col1.button("🎓 Education"): st.session_state.about_page = 'Education'
    if btn_col2.button("💼 Experience"): st.session_state.about_page = 'Experience'
    if btn_col3.button("🎯 Goals"): st.session_state.about_page = 'Goals'
    if btn_col4.button("🏆 Achievements"): st.session_state.about_page = 'Achievements'
    if btn_col5.button("🎨 Hobbies"): st.session_state.about_page = 'Hobbies'

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 6. DYNAMIC CONTENT AREA ---
    
    # Compact Card Function (Reusable for all sections)
    def info_card(title, subtitle, date="", description="", icon="🔹"):
        desc_html = f'<div style="color:#555; font-size:13px; margin-top:5px; line-height:1.4;">{description}</div>' if description else ""
        date_html = f'<span style="font-size: 11px; color: #FF69B4; font-weight: bold;">🗓 {date}</span>' if date else ""
        
        st.markdown(f"""
            <div style="
                background-color: #ffffff; 
                padding: 12px 18px; 
                border-radius: 10px; 
                border-left: 5px solid #FF69B4; 
                box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
                margin-bottom: 10px;
            ">
                <div style="display: flex; justify-content: space-between; align-items: baseline;">
                    <span style="font-size: 13px; font-weight: 800; color: #333;">{icon} {title.upper()}</span>
                    {date_html}
                </div>
                <div style="font-size: 14px; color: #FF69B4; font-weight: 700; margin-top: 2px;">{subtitle}</div>
                {desc_html}
            </div>
        """, unsafe_allow_html=True)

    if st.session_state.about_page == 'Education':
        st.markdown('<h3 style="color: #FF69B4; font-weight: 800;">🎓 Education</h3>', unsafe_allow_html=True)
        info_card("College", "DEBESMSCAT", "2023 - Present", "Bachelor of Science in Computer Science")
        info_card("Senior High", "Nabongsoran High School", "2022 – 2023", icon="🏫")
        info_card("Junior High", "Luy-a Nationalized High School", "2008 – 2009", icon="🏫")

    elif st.session_state.about_page == 'Experience':
        st.markdown('<h3 style="color: #FF69B4; font-weight: 800;">💼 Work Experience</h3>', unsafe_allow_html=True)
        info_card("Virtual Assistant", "US-Based Client", "Contractual", "Handled administrative tasks and client communication.")
        info_card("Photo Editor", "Sopphie Lee Photo Studio", "Freelance", "Specialized in wedding, debut, and family portrait restoration.")
        info_card("Team Leader", "StarMaker Community", "Online", "Managed groups, organized activities, and led singing competitions.")

    elif st.session_state.about_page == 'Goals':
        st.markdown('<h3 style="color: #FF69B4; font-weight: 800;">🎯 Professional Goals</h3>', unsafe_allow_html=True)
        info_card("Technical", "Full-Stack Development", "Priority", "Build scalable web systems like Barangay Management Systems.")
        info_card("Creative", "UI/UX & Branding", "Continuous", "Enhance skills in modern interfaces and visual identity.")
        info_card("Career", "Client-Based Projects", "Long-term", "Expand freelancing and build a strong professional portfolio.")

    elif st.session_state.about_page == 'Achievements':
        st.markdown('<h3 style="color: #FF69B4; font-weight: 800;">🏆 Certifications</h3>', unsafe_allow_html=True)
        info_card("HTML Essentials", "Cisco Networking Academy", "Mar 2025", "Foundational certification in web structure.")
        info_card("CSS Essentials", "Cisco Networking Academy", "Apr 2025", "Certification in modern web styling and layout.")
        info_card("Computer Hardware", "JS Institute", "Completed", "Basics of hardware maintenance and troubleshooting.")

    elif st.session_state.about_page == 'Hobbies':
        st.markdown('<h3 style="color: #FF69B4; font-weight: 800;">🎨 Personal Hobbies</h3>', unsafe_allow_html=True)
        info_card("Restoration", "Photo Editing", "Daily", "Restoring old family photos and creative graphic design.")
        info_card("Development", "Exploring Frameworks", "Weekly", "Learning Streamlit and Python for real-world applications.")
        info_card("Leadership", "Team Coordination", "Active", "Singing and managing online communities.")
with col_img:
    st.markdown('<div class="fan-frame-container">', unsafe_allow_html=True)
    st.markdown('<p class="photo-editor-top">PHOTO EDITOR</p>', unsafe_allow_html=True)
    img_b64 = get_base64_img("profile1.png")
    if img_b64:
        st.markdown(f'''
            <div class="fan-frame-3d">
                <img src="data:image/png;base64,{img_b64}" class="fan-img">
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)