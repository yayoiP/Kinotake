import streamlit as st
import scratchattach as sa
cloud = sa.get_tw_cloud("1134389682")

st.title('きのこたけのこをひっくりかえすアプリ')
value=st.number_input("きのこの値",min_value=0,max_value=40000)
if st.button("実効"):
    cloud.set_var("きのこ", f"{value}")
