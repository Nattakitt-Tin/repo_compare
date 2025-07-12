import streamlit as st
from features import git_compare_page, thai_id_page

st.set_page_config(page_title="Multi Feature App", layout="wide")

page = st.sidebar.selectbox(
    "เลือกฟีเจอร์",
    ("Home", "Git Compare", "Thai ID Generator"),
)

if page == "Home":
    st.title("🛠 Multi Feature App")
    st.write("เลือกฟีเจอร์จากแถบด้านซ้ายเพื่อเริ่มใช้งาน")
elif page == "Git Compare":
    git_compare_page.show()
elif page == "Thai ID Generator":
    thai_id_page.show()
