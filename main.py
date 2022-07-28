# frontend/main.py

import requests
import streamlit as st
from utils import *

OUTPUT = {
    "mask" : "segmentation mask",
    "boxes" : "bounding boxes"
}

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Style transfer web app")

# displays a file uploader widget
imageSrc = st.sidebar.file_uploader("Sélectionner une image")
# displays the select widget for the styles

outputDisplay = ("segmentation mask", "bounding boxes")
outputVerb = ("mask", "boxes")

output = st.sidebar.multiselect("Choix du type de résultat", outputVerb, format_func=lambda x: OUTPUT[x])

# displays a button
if st.sidebar.button("Traiter l'image"):
    if imageSrc is not None and output is not None:
        st.image(imageSrc, width=512)
        files = {"file": imageSrc.getvalue()}
        for out in output:
            res = requests.post(f"https://oc8segment.azurewebsites.net/{out}", files=files)
            st.image(res.content, width=512)


