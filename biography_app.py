import streamlit as st
import os
import json

# Directory for saving user progress
SAVE_DIR = "biography_data"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Function to save progress
def save_progress(data):
    with open(f"{SAVE_DIR}/progress.json", "w") as f:
        json.dump(data, f)

# Function to load saved progress
def load_progress():
    try:
        with open(f"{SAVE_DIR}/progress.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Load previously saved progress
progress = load_progress()

# Streamlit App Configuration
st.set_page_config(page_title="Personalized Biography", page_icon="📖", layout="wide")

# Apply CSS for custom styles
st.markdown(
    """
    <style>
    /* Center-align title */
    .title {
        text-align: center;
        font-family: Arial, sans-serif;
    }

    /* Highlight section headers */
    .section-header {
        color: #2E86C1;
        font-size: 22px;
        font-weight: bold;
    }

    /* Align images */
    .profile-pic {
        display: block;
        margin: 0 auto;
    }

    /* Style sidebar */
    .css-1aumxhk { 
        background-color: #f8f9fa; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "✏️ Edit Biography"])

# Home Page
if page == "🏠 Home":
    st.markdown('<h1 class="title">Welcome to Your Personalized Biography!</h1>', unsafe_allow_html=True)
    st.write(
        """
        This app helps you create and organize your biography beautifully.
        Use the menu on the left to edit or view your biography details.
        """
    )
    st.markdown("---")

    if progress:
        st.subheader("✨ Your Biography Details")
        col1, col2 = st.columns([1, 3])
        with col1:
            if os.path.exists(f"{SAVE_DIR}/profile_picture"):
                st.image(f"{SAVE_DIR}/profile_picture", caption="Profile Picture", width=150, use_container_width="auto")
            else:
                st.info("No profile picture uploaded.")
        with col2:
            st.write(f"**Name:** {progress.get('name', 'N/A')}")
            st.write(f"**Age:** {progress.get('age', 'N/A')}")
            st.write(f"**Gender:** {progress.get('gender', 'N/A')}")
            st.write(f"**Course:** {progress.get('course', 'N/A')}")
            st.write(f"**University:** {progress.get('university', 'N/A')}")
            st.write(f"**Country:** {progress.get('country', 'N/A')}")
            st.write(f"**Nationality:** {progress.get('nationality', 'N/A')}")

        st.markdown("### 📝 About Me")
        st.write(progress.get("about_me", "N/A"))

        st.markdown("### 🎨 Hobbies")
        st.write(progress.get("hobbies", "N/A"))

        st.markdown("### 💬 Favorite Quotes")
        st.write(progress.get("favorite_quotes", "N/A"))

        st.markdown("### 🌟 Motto")
        st.write(progress.get("motto", "N/A"))

        st.markdown("### 📋 Future Plans")
        st.write(progress.get("future_plans", "N/A"))
    else:
        st.info("No biography data found. Please go to the 'Edit Biography' page to create your profile.")

# Edit Biography Page
elif page == "✏️ Edit Biography":
    st.markdown('<h1 class="title">Edit Your Biography</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown('<p class="section-header">🧑 Basic Information</p>', unsafe_allow_html=True)
    name = st.text_input("Name", progress.get("name", ""))
    age = st.number_input("Age", min_value=1, max_value=120, value=progress.get("age", 18))
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(progress.get("gender", "Male")))
    course = st.text_input("Course", progress.get("course", ""))
    university = st.text_input("Name of University", progress.get("university", ""))
    country = st.text_input("Country", progress.get("country", ""))
    nationality = st.text_input("Nationality", progress.get("nationality", ""))

    st.markdown('<p class="section-header">📸 Profile Picture</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload your profile picture", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        with open(f"{SAVE_DIR}/profile_picture", "wb") as f:
            f.write(uploaded_file.getbuffer())
    if os.path.exists(f"{SAVE_DIR}/profile_picture"):
        st.image(f"{SAVE_DIR}/profile_picture", caption="Current Picture", width=150)

    st.markdown('<p class="section-header">📝 About Me</p>', unsafe_allow_html=True)
    about_me = st.text_area("Tell us about yourself", progress.get("about_me", ""))

    st.markdown('<p class="section-header">🎨 Hobbies</p>', unsafe_allow_html=True)
    hobbies = st.text_area("List your hobbies", progress.get("hobbies", ""))

    st.markdown('<p class="section-header">💬 Favorite Quotes</p>', unsafe_allow_html=True)
    favorite_quotes = st.text_area("Your favorite quotes", progress.get("favorite_quotes", ""))

    st.markdown('<p class="section-header">🌟 Motto</p>', unsafe_allow_html=True)
    motto = st.text_input("Your motto in life", progress.get("motto", ""))

    st.markdown('<p class="section-header">📋 Future Plans</p>', unsafe_allow_html=True)
    future_plans = st.text_area("Your plans for the future", progress.get("future_plans", ""))

    # Save Button
    if st.button("💾 Save Biography"):
        progress = {
            "name": name,
            "age": age,
            "gender": gender,
            "course": course,
            "university": university,
            "country": country,
            "nationality": nationality,
            "about_me": about_me,
            "hobbies": hobbies,
            "favorite_quotes": favorite_quotes,
            "motto": motto,
            "future_plans": future_plans,
        }
        save_progress(progress)