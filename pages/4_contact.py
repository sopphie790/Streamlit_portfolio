import streamlit as st
import base64
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Contact | Liza Jaime", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Function para sa Image Handling (Para sa Sidebar Logo)
def get_base64_img(image_path):
    full_path = os.path.join("images", image_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# --- 2. CUSTOM CSS (STRICTLY CONSISTENT WITH PROJECTS PAGE) ---
st.markdown("""
    <style>
    /* SIDEBAR - EXACT COPY FROM PROJECTS */
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
    .location-text { color: #000000; font-weight: bold; font-size: 14px; margin-top: 10px; }

    /* CONTACT PAGE SPECIFIC STYLING */
    .contact-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #FF69B4;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .contact-card:hover {
        transform: translateY(-5px);
        border-left: 5px solid #FFD700;
    }
    .contact-header {
        color: #FF69B4;
        font-weight: 900;
        font-size: 40px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    
    header { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (STRICTLY CONSISTENT) ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    logo_b64 = get_base64_img("logo1.png")
    if logo_b64:
        st.markdown(f'''
            <div class="sidebar-footer">
                <img src="data:image/png;base64,{logo_b64}" class="sidebar-logo">
                <div class="location-text">📍 Aroroy, Masbate, Philippines</div>
            </div>
        ''', unsafe_allow_html=True)

# --- 4. MAIN CONTENT ---
st.markdown('<div class="contact-header">📬 CONTACT ME</div>', unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("### ✉️ Let's Work Together")
    name = st.text_input("Name", placeholder="Your Full Name")
    email = st.text_input("Email", placeholder="jaimeliza790@gmail.com")
    message = st.text_area("Message", placeholder="Tell me about your project or photo editing needs...", height=150)
    
    if st.button("SEND MESSAGE", use_container_width=True):
        if name and email and message:
            st.success(f"Message sent successfully to jaimeliza790@gmail.com! ✅")
        else:
            st.error("Please complete all fields.")

with col2:
    st.markdown("### 📍 Quick Info")
    
    # Email Card
    st.markdown(f"""
        <div class="contact-card">
            <div style="font-weight: bold; color: #FF69B4; font-size: 12px;">GMAIL</div>
            <div style="font-size: 14px; color: #333; font-weight: bold;">jaimeliza790@gmail.com</div>
        </div>
    """, unsafe_allow_html=True)

    # Social Card
    st.markdown("""
        <div class="contact-card">
            <div style="font-weight: bold; color: #FF69B4; font-size: 12px;">FACEBOOK</div>
            <div style="font-size: 14px; color: #333; font-weight: bold;">Sopphie Lee Photo Studio</div>
        </div>
    """, unsafe_allow_html=True)

    # Business Card
    st.markdown("""
        <div class="contact-card">
            <div style="font-weight: bold; color: #FF69B4; font-size: 12px;">SERVICES</div>
            <div style="font-size: 14px; color: #333; font-weight: bold;">Web Dev | Photo Editing | VA</div>
        </div>
    """, unsafe_allow_html=True)

# Footer Social Buttons
st.markdown("<br>", unsafe_allow_html=True)
soc1, soc2, soc3 = st.columns(3)
with soc1:
    st.link_button("📘 FACEBOOK", "https://www.facebook.com/?ref=homescreenpwa", use_container_width=True)
with soc2:
    st.link_button("💻 GITHUB", "https://github.com/", use_container_width=True)
with soc3:
    st.link_button("📧 EMAIL ME", "mailto:jaimeliza790@gmail.com", use_container_width=True)