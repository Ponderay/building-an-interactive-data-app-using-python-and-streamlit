import pandas as pd
import plotly.express as px
import streamlit as st
import random

st.title("แอป Streamlit แรกของฉัน")
st.header("สวัสดีชาวโลก 👏")
st.write("นี่คือตัวอย่างของแอป Streamlit แบบง่าย ๆ")

# อ่านข้อมูล
df = pd.read_csv("../datasets/1642645053.csv", encoding="tis-620")
st.write(df)

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)
st.write(df)

# สไลเดอร์เลือกตัวเลข
number = st.slider("เลือกตัวเลข", 0, 100, 50)
st.write("ตัวเลขที่เลือกคือ ", number)

# วิทยุให้คะแนน
rating = st.radio(
    "คุณให้คะแนนคลาสนี้เท่าไร?",
    ("1", "2", "3", "4", "5")
)
st.write(f"คุณเลือก {rating}")

# กราฟ
df_grouped_by_species = df.groupby("species")["body_mass_g"].mean()
st.bar_chart(df_grouped_by_species)

fig = px.bar(df_grouped_by_species.reset_index(), x="species", y="body_mass_g")
st.plotly_chart(fig)

# Sidebar
with st.sidebar:
    st.write("นี่คือ Sidebar")
    option = st.selectbox(
        "คุณชอบตัวเลขไหนมากที่สุด?",
        ["1", "2", "3", "4", "5"]
    )

# มินิเกม: ทายตัวเลข
st.subheader("มินิเกม: ทายตัวเลข")
target_number = random.randint(1, 100)
guess = st.number_input("ลองทายตัวเลข (ระหว่าง 1 ถึง 100)", min_value=1, max_value=100, step=1)
if st.button("ตรวจคำตอบ"):
    if guess == target_number:
        st.success(f"ยินดีด้วย! คุณทายถูกแล้ว! ตัวเลขคือ {target_number}")
    else:
        st.warning(f"ลองใหม่อีกครั้ง! ตัวเลขที่ถูกต้องคือ {target_number}")
