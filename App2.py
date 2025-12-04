import streamlit as st
import torch
from torchvision import models, transforms
from PIL import Image
from product_recommendation import recommend_products

# ================= PAGE CONFIG =================
st.set_page_config(page_title="💆‍♀️ Skin Analyzer", layout="wide")

# ================= CUSTOM CSS =================
st.markdown("""
<style>
/* App background */
.stApp { background-color: #FFF7F8; }

/* Moving Gradient Title */
.moving-title {
    background: linear-gradient(270deg, #FF8A80, #FF4081, #FFC107, #8BC34A, #FF8A80);
    background-size: 1200% 1200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientAnimation 8s ease infinite, slide 12s linear infinite;
    display: inline-block;
}
@keyframes gradientAnimation {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}
@keyframes slide {
    0% {transform: translateX(100%);}
    100% {transform: translateX(-100%);}
}

/* Gradient Buttons */
.gradient-btn {
    background: linear-gradient(90deg, #FF8A80, #FF4081);
    padding: 12px 25px;
    border-radius: 12px;
    color: white !important;
    font-size: 18px;
    border: none;
    cursor: pointer;
    font-weight: 600;
    transition: 0.3s;
}
.gradient-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px #FF4081;
}

/* Animated Loader */
.loader {
    border: 6px solid #f3f3f3;
    border-top: 6px solid #C2185B;
    border-radius: 50%;
    width: 45px;
    height: 45px;
    animation: spin 0.8s linear infinite;
    margin: auto;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Product Cards */
.card {
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 12px;
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 12px rgba(255,64,129,0.3);
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR NAVIGATION =================
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to →",
    ["🏠 Home", "📸 Analyze Skin", "🧴 Recommended Products"]
)

# ================= DEVICE =================
device = "cuda" if torch.cuda.is_available() else "cpu"

# ================= LOAD MODEL FUNCTION =================
@st.cache_resource
def load_model(path):
    ckpt = torch.load(path, map_location=device)
    num_classes = len(ckpt["classes"])
    model = models.mobilenet_v2(weights=None)
    model.classifier[1] = torch.nn.Linear(1280, num_classes)
    model.load_state_dict(ckpt["model"])
    model.eval().to(device)
    return model, ckpt["classes"]

# Load models
skin_model, skin_classes = load_model("skin_type_model.pth")
issues_model, issues_classes = load_model("skin_issues_model.pth")

# ================= TRANSFORM =================
tfm = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])

# ================= PREDICTION FUNCTION =================
def predict(image):
    img = image.convert("RGB")
    x = tfm(img).unsqueeze(0).to(device)
    with torch.no_grad():
        st_pred = torch.softmax(skin_model(x), 1)
        st_index = st_pred.argmax(1).item()
        skin_type = skin_classes[st_index]

        si_pred = torch.sigmoid(issues_model(x)).cpu().numpy()[0]
        issues = [issues_classes[i] for i, p in enumerate(si_pred) if p > 0.4]

    if not issues:
        issues = ["clear healthy skin"]

    return skin_type, issues

# ================= HOME PAGE =================
if page == "🏠 Home":
    st.markdown("""
    <h1 style='text-align:center; font-size:50px; font-weight:900;'>
        💆‍♀️ <span class='moving-title'> Skin Analyzer & Product Recommendation System</span>
    </h1>
    """, unsafe_allow_html=True)
    st.write("""
    Welcome to the **AI Powered Skin Analyzer**!  
    Detect your skin type, skin issues, and get personalized product recommendations.
    """)

# ================= ANALYZE SKIN PAGE =================
elif page == "📸 Analyze Skin":
    st.header("📸 Skin Analyzer")
    mode = st.radio("Choose Input Mode", ["Upload Image", "Webcam Capture"])
    img = None

    if mode == "Upload Image":
        uploaded = st.file_uploader("Upload face image", type=["jpg", "png", "jpeg"])
        if uploaded:
            img = Image.open(uploaded)
            st.image(img, caption="Uploaded Image", use_container_width=True)
    else:
        cam = st.camera_input("Capture a photo")
        if cam:
            img = Image.open(cam)
            st.image(img, caption="Captured Image", use_container_width=True)

    if img is not None:
        st.markdown("<div class='loader'></div>", unsafe_allow_html=True)
        with st.spinner("Analyzing skin..."):
            skin_type, issues = predict(img)
        st.success("Analysis Complete!")
        st.subheader(f"🧴 Skin Type: **{skin_type.capitalize()}**")
        st.subheader("⚡ Skin Issues")
        for issue in issues:
            st.markdown(f"<div class='card'>- {issue}</div>", unsafe_allow_html=True)

        # Store results for product page
        st.session_state["skin_type"] = skin_type
        st.session_state["issues"] = issues

# ================= RECOMMENDED PRODUCTS PAGE =================
elif page == "🧴 Recommended Products":
    if "skin_type" not in st.session_state:
        st.warning("⚠ Please analyze your skin first!")
    else:
        st.header("🧴 Personalized Recommendations")
        skin_type = st.session_state["skin_type"]
        issues = st.session_state["issues"]
        morning, night = recommend_products(skin_type, [i.lower() for i in issues])

        st.subheader("🌞 Morning Routine")
        for step, name, use, price in morning:
            st.markdown(f"""
            <div class='card' style='background:#FFE3ED;'>
                <b>{step}:</b> {name}<br>
                🔎 <i>{use}</i><br>
                💰 <b>₹{price}</b>
            </div>
            """, unsafe_allow_html=True)

        st.subheader("🌙 Night Routine")
        for step, name, use, price in night:
            st.markdown(f"""
            <div class='card' style='background:#F3E5F5;'>
                <b>{step}:</b> {name}<br>
                🔎 <i>{use}</i><br>
                💰 <b>₹{price}</b>
            </div>
            """, unsafe_allow_html=True)
