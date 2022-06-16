import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from PIL import Image
import sqlite3
import warnings
warnings.filterwarnings('ignore')

bpk_icon = Image.open("assets/BPK.ico")
LOGO_IMAGE = "assets/BPK.png"
st.set_page_config(
    layout="centered", page_icon=bpk_icon, page_title="Index LHP BPK Perwakilan Sumsel", initial_sidebar_state="auto"
) #layout use wide instead of centered

col1, col2 = st.columns([2,5])

with col1:
    st.image(bpk_icon, width =150, use_column_width=True)

with col2:
    st.title("Index Laporan Hasil Pemeriksaan")
    st.subheader('BPK perwakilan Sumatera Selatan')
    #st.header("Kertas Kerja Pemeriksa")


with st.sidebar:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(bpk_icon, width=150, use_column_width=True)
    #st.sidebar.image(bpk_icon, width=50)
    with col2:
        st.write("Index LHP\n BPK perwakilan Sumsel")

    option = st.selectbox(
        'Data apa yang ingin anda cari?',
        ('Sumsel I', 'Sumsel II'))

    if option == 'Sumsel I':
        option_2 = st.selectbox(
        'Hasil Pemeriksaan',
        ('LHP', 'PDTT', 'Kinerja', 'Investigasi'))
    elif option == 'Sumsel II':
        option_2 = st.selectbox(
            'Hasil Pemeriksaan',
            ('LHP', 'PDTT', 'Kinerja', 'Investigasi'))

    year = st.slider(
        "Data Arsip tahun berapa yang anda cari?",
        2015, 2022, (2018, 2019))


st.write(option, option_2, year)

def tabel_arsip(df: pd.DataFrame):
    #tabel interaktif berisi index arsip digital KKP
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection

