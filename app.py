import streamlit as st

st.set_page_config(page_title="🌱 Growth Mindset Challenge", page_icon="⭐", layout="wide")

# CSS for Sidebar, Rating Stars, and Footer
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #80bfff; /* Lighter blue */
    }
    .star {
        font-size: 30px;
        cursor: pointer;
    }
    .footer {
        background-color: #d3e0ea;
        padding: 10px;
        text-align: center;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar My left content 
st.sidebar.header("🌟 Navigation")
st.sidebar.write("Navigate through the app:")
page = st.sidebar.selectbox("Choose a section:", ["Home", "Today's Quote", "Challenge", "Reflection", "Achievements"])

st.sidebar.header("🛠️ Tools")
st.sidebar.text_input("🔍 Search for insights")
st.sidebar.slider("🌡️ Set your mindset level", 0, 100, 50)

# Main Content
st.title("🌟 Growth Mindset Challenge: Web App with Streamlit")
st.write("💡 Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection.")

if page == "Home": #if user select Home  
    st.header("🚀 Welcome to Your Growth Journey")

elif page == "Today's Quote": #if user select Todays Quote
    st.header("📜 Today's Growth Mindset Quote")
    st.write('✨ "Success is not final, failure is not fatal: it is the courage to continue that counts."')

elif page == "Challenge": #if user select Challenge
    st.header("🔥 What's Your Challenge Today?")
    user_input = st.text_input("✍️ Describe your challenge you're facing:")
    if user_input:
        st.success(f"💪 You're facing: {user_input}. Keep pushing forward toward your goal! 🚀")
    else:
        st.warning("⚡ Tell us about your challenge.")

elif page == "Reflection": #if user select Reflection
    st.header("🧠 Reflect on Your Learning")
    reflection = st.text_area("📖 Write your reflection here:")
    if reflection:
        st.success(f"🎯 Great Insight! Your reflection: {reflection}")
    else:
        st.info("🧐 Reflecting on past experiences helps you grow! Share your difficulties.")

elif page == "Achievements": #if user select Achievement
    st.header("🏆 Celebrate Your Wins!")
    achievement = st.text_input("🎉 Share something you've recently accomplished:")
    if achievement:
        st.success(f"👏 Amazing! You achieved: {achievement} 🎊")
    else:
        st.info("🥇 Big or small, every achievement counts! Share one now.")

st.write("💖 Keep believing in yourself. Growth is a journey, not a destination. 🌍")

# Rating Section
st.header("⭐ Rate Your Experience")
rating = st.radio("How would you rate this app?", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
st.write(f"Your rating: {rating}")

# Footer 
st.markdown("<div class='footer'>🔨 Built by Syed Ahsan</div>", unsafe_allow_html=True)
