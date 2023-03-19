import streamlit as st
from itertools import cycle

class FileProcessor:

    def __init__(self, key:str) -> None:
        self.__key = key.encode('ascii')
    
    @staticmethod
    def file_download(data:bytes) -> None:
        st.caption(f"{st.session_state['file'].name} is processed and is ready for download.")
        st.download_button(
            label="Download",
            data=data,
            file_name=f"Processed_{st.session_state['file'].name}",
            mime=st.session_state['file'].type)

    def process(self, data:bytes) -> bytes:
        with st.spinner(f"Processing file {st.session_state['file'].name}..."):
            processed_data = bytes(x ^ y for x, y in zip(data, cycle(self.__key)))
            self.file_download(processed_data)

if __name__ == "__main__":
    pass
