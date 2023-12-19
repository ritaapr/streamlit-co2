import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('prediksi_co2.sav','rb'))

df = pd.read_excel("CO2 dataset.xlsx")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

st.title('CO2 EMISSION PREDICTION')

# Slider untuk rentang tahun 2014-2044
year_slider_1_29 = st.slider("Geser ke tahun yang ingin Anda prediksi!", 2014, 2044, step=1)

# Konversi nilai slider 
year_slider_2014_2044 = year_slider_1_29 - 2013

# Gunakan nilai tahun yang dihasilkan untuk prediksi
if st.button("Predict"):
    year = year_slider_2014_2044
    pred = model.forecast(year)
    pred = pd.DataFrame(pred, columns=['CO2'])

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['CO2'].plot(style='--', color='gray', legend=True, label='known')
        pred['CO2'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)
