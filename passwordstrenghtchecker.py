import streamlit as st
import re

def check_password_strength(password):
    """Check the strength of the password."""
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&+=]", password):
        strength += 1

    return strength

def strength_label(strength):
    """Return strength label based on strength score."""
    if strength < 3:
        return "Weak", "red", "🔴"
    elif strength < 5:
        return "Moderate", "orange", "🟠"
    else:
        return "Strong", "green", "🟢"

# Streamlit app
st.title("Professional Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    strength = check_password_strength(password)
    label, color, icon = strength_label(strength)

    # Display strength meter with animation and icons
    st.markdown(f"""
    <style>
        .strength-meter {{
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 5px;
            overflow: hidden;
            position: relative;
        }}
        .strength-bar {{
            height: 20px;
            border-radius: 5px;
            transition: width 0.5s ease-in-out;
        }}
        .strength-label {{
            position: absolute;
            width: 100%;
            text-align: center;
            top: -25px;
            font-weight: bold;
            font-size: 16px;
            color: {color};
        }}
    </style>
    <div class="strength-meter">
        <div class="strength-label">{icon} {label}</div>
        <div class="strength-bar" style="width: {strength * 20}%; background-color: {color};"></div>
    </div>
    """, unsafe_allow_html=True)

    st.write(f"Strength: **{label}**")
