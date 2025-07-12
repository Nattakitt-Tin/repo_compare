import streamlit as st
from features import git_compare_page, thai_id_page
from features import login_manager

st.set_page_config(page_title="Multi Feature App", layout="wide")

pages = ["Home", "Git Compare", "Thai ID Generator"]
selected_page = st.sidebar.selectbox("เลือกฟีเจอร์", pages)

if selected_page == "Home":
    st.title("🛠 Multi Feature App")
    if login_manager.is_logged_in():
        st.success("Logged in")
        st.write("เลือกฟีเจอร์จากแถบด้านซ้ายเพื่อเริ่มใช้งาน")
    else:
        login_manager.login_form()
elif selected_page == "Git Compare":
    if login_manager.require_login():
        git_compare_page.show()
elif selected_page == "Thai ID Generator":
    if login_manager.require_login():
        thai_id_page.show()

