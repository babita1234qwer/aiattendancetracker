import streamlit as st

import segno
import io
from src.ui.base_layout import style_base_layout


@st.dialog("Share Class Link")

def share_subject_dialog(subject_name,subject_code):
    
    app_domain="http://localhost:8501"
    join_url=f"{app_domain}/?join-code={subject_code}"

    st.markdown(
    "<h5 style='color:white;'>Scan to Join</h5>",
    unsafe_allow_html=True
)

    qr=segno.make(join_url)

    out=io.BytesIO()

    qr.save(out, kind="png", scale=10, border=1, dark="black", light="white")
    col1,col2=st.columns(2)

    with col1:
        st.markdown(
          "<h5 style='color:white;'>Copy Link</h5>",
           unsafe_allow_html=True
           )
        st.code(join_url,language="text")
        st.code(subject_code,language="text")
        st.info("Copy this link to share on Watsapp")

    with col2:
            
                    


            st.image(out.getvalue(), caption="QR code for class join") 


