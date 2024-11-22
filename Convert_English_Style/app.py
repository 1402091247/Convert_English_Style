
import streamlit as st

from pathlib import Path
from typing import  Union
from os import PathLike
from Convert import convert

@st.cache_data(max_entries=64)
def read_local_file(fin: Union[str, PathLike]) -> str:
    return Path(fin).read_text(encoding="utf-8")
def load_css(stem: str):
    """Load a given CSS file in streamlit. The given "name".css will be looked for in the css directory.
    :param stem: filename without extension to load
    """
    pfcss = Path(__file__).parent.joinpath(f"css/{stem}.css")
    st.markdown(f"<style>{read_local_file(pfcss)}</style>", unsafe_allow_html=True)

def main():
    load_css("convert")
    st.markdown("## ✨ Convert English Style")
    text_to_speech = st.text_area('📖 Enter text to convert:')
    out = ''
    src_lang_col, tgt_lang_col , swap_btn_col= st.columns((3, 3, 1))
    with src_lang_col:
        style = st.selectbox('Make your text:', ['Professional', 'Sociable', 'Summary'], key='style')
    with tgt_lang_col:
        degree = st.select_slider('convert degree', ["Low", "Medium", "High"], key='speed')
    with swap_btn_col:
        bt1 = st.markdown('<button class="custom-button">Convert</button>', unsafe_allow_html=True)
    if bt1 and text_to_speech:
        print('text_to_speech', text_to_speech)
        out = convert(text_to_speech, "{}_{}".format(style, degree))
    else:
        st.warning('Please make sure your text is not empty!')
    st.text_area('📖 Output after conversion:', out)



if __name__ == "__main__":
    main()