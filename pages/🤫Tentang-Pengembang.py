import streamlit as st


st.set_page_config(
    page_title="Tentang-Pengembang",
    page_icon="👋",
)

st.title("Halo Semuanya !👋")
st.title("Kami dari Kelompok 2")
st.title("Yang Terdiri dari 3 Mahasiswa")

tab1, tab2, tab3 = st.tabs(["Okhi Sahrul Barkah", "Farid Ghozali", "Afirza Lucky Pradana"])

with tab1:
   st.write("Belum Ada Foto")

with tab2:
   st.image("farid.png")
    
with tab3:
   st.write("Belum Ada Foto")
