import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Birthday Surprise 🎉",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS for a more professional look
st.markdown("""
    <style>
    .main {
        background-color: #0f0f1a;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #ff4b6e;
    }
    .card {
        background: linear-gradient(135deg, #ff4b6e, #6a5acd);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-top: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    }
    .message {
        font-size: 18px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🎉 Birthday Surprise Experience 🎉</div>", unsafe_allow_html=True)

st.write("Enter your name to unlock something magical ✨")

name = st.text_input("Your name 💖")

if name:

    # Celebration effects
    st.balloons()
    st.toast("🎂 Surprise Unlocked!")

    # Loading effect (feels premium)
    with st.spinner("Preparing something special for you... 💫"):
        time.sleep(2)

    st.success(f"Welcome {name}! Today is all about YOU 🎉")

    # Beautiful card
    st.markdown(f"""
    <div class='card'>
        <h2>💖 Happy Birthday {name}! 💖</h2>
        <p class='message'>
            You are not just special… you are <b>extraordinary</b> 🌟<br><br>
            May your life be filled with success, love and endless happiness 🎂✨<br><br>
            The world is better because you are in it 🌍💫
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Animated wishes section
    st.subheader("💌 Special Wishes Just For You")

    wishes = [
        "🌟 May your dreams become reality",
        "🎯 May you achieve everything you work for",
        "💖 May happiness follow you everywhere",
        "🚀 May your future be brighter than ever"
    ]

    for w in wishes:
        st.info(w)
        time.sleep(0.5)

    st.markdown("---")

    # Final surprise section
    st.subheader("🎁 Final Surprise")

    st.write(f"""
    💫 Bro, aaj tumhari birthday hai and I just wanna say that kai tumnai hamesha kisi bari sister ki tarah mujhe guide kia hai aur ha maybe sometimes mainai mind kiya likin in the end mujhe realize howa kai you were right not hamesha but most of the time 😭

    🎂 Mai chahti hon kai yeh birthday tumharai liyai special ho warna merai aur Fatima kai honai ka faida kia? 👉👈 

    🌈 Hamesha hasti raho and mujhe roast karti raho mai enjoy karti hon tumhari best timing wali roasting ko 😅

    💖 Tum ek bohat achii dost ho 🥹 aur mai aaj wo kehna chahti hon jo mai most of time bol nhi pati I am so sorry aghr tumhai meri baat ka kabhi bura laga ho 🥲
    """)

    # Extra effects
    st.snow()
    st.success("🎉 END OF SURPRISE! HOPE YOU SMILED 😊")
