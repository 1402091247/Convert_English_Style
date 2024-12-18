
import streamlit as st

from pathlib import Path
from typing import  Union
from os import PathLike
from Convert import convert
'''
https://convertstyle.streamlit.app/
'''
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
    st.markdown("## ✨ 中文生成器v1.0")
    text_to_speech = st.text_area('📖 输入内容:')
    out = ''
    src_lang_col, multi_select, tgt_lang_col , swap_btn_col= st.columns((2, 2, 2, 1))
    # with src_lang_col:
    #     style = st.selectbox('Make your text:', ['Professional', 'Sociable', 'Summary'], key='style')
    # if style == 'Professional':
    #     with multi_select:
    #         profession_list = st.selectbox('Select profession:', ['None','Energy',' Materials', 'Industrials', 'Consumer Discretionary',
    #                                                       'Consumer Staples', 'Health Care','Financials', 'Information Technology',
    #                                                       'Communication Services', 'Real Estate'], key='lang')
    # else:
    #     with multi_select:
    #         profession_list = st.selectbox('Select profession:',
    #                                        ['None'], key='lang')
    # with tgt_lang_col:
    #     degree = st.select_slider('Degree of Conversion', ["Low", "Medium", "High"], key='speed')
    with swap_btn_col:
        # bt1 = st.markdown('<button class="custom-button" onclick = "alert(点击)">Convert</button>', unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            .custom-button {
                padding: 7px 14px; /* 内边距 */
                margin: 25px 2px;
                border: none; /* 边框 */
                border-radius: 5px; /* 圆角 */
                font-size: 16px; /* 字体大小 */
                }
            .custom-button:hover {
                background-color: #45a049; /* 悬停时的背景颜色 */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        bt1 = st.button("生成",key="custom-button")
    if bt1 and text_to_speech:
        print('text_to_speech', text_to_speech)
        out = convert(text_to_speech)
    else:
        st.warning('确保你的内容不为空!')
    st.text_area('📖 输出：:', out)


if __name__ == "__main__":
    main()