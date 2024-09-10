import streamlit as st 
import joblib as jb
import numpy as np
import time

scaler = jb.load("scaler.pkl")
model = jb.load("model.pkl")

st.title("MÔ HÌNH DỰ ĐOÁN GIÁ NHÀ")

st.divider()
# give info

floor = st.number_input("Nhập số tầng bạn muốn", value=0 , step = 1)
Area = st.number_input("Nhập diện tích đất bạn muốn (Diện tích m²):",value=0, step = 1000)
district = st.number_input("Nhập mã quận của bạn muốn tìm (Hoàng Mai:1, Hai Bà Trưng:2, Đống Đa:3,Thanh Xuân:4,Q. Cầu Giấy:5):",value=0, step = 10)

X =[floor,Area,district ]
st.divider()
predict_button = st.button("Click here for the result")
st.divider()

if predict_button:
    with st.status("Searching for data..."):
        st.write("Loanding data...")
        time.sleep(2.5)
        st.write("DONE!")
        time.sleep(1)
        
    X1 = np.array(X)
    X_arr  = scaler.transform([X1])
    prediction  = model.predict(X_arr)[0]
    st.write(f"Giá nhà dự kiến (tỷ) là {prediction:.2f}")



else:
    "ERROR!!"
