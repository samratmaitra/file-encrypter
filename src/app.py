import streamlit as st
from file_processor import FileProcessor

def load_page() -> list:
    st.header("File Encryption / Decryption Util")
    with st.form("frm_main", clear_on_submit=True):
        file = st.file_uploader("Choose File:", accept_multiple_files=False)
        secret_key = st.text_input("Enter secret key:", type="password")
        btn_submit = st.form_submit_button("Submit")
        if btn_submit:
            if file and secret_key:
                st.session_state['file'] = file
                st.session_state['secret_key'] = secret_key
                return btn_submit
            else:
                st.warning("Choose Files and Provide Secret Key.")

if __name__ == "__main__":
    if load_page():
        fp = FileProcessor(st.session_state['secret_key'])
        ip_data = st.session_state['file'].getvalue()
        fp.process(ip_data)
