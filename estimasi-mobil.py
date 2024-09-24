import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), 'estimasi-mobil.sav')
model = pickle.load(open(model_path, 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Miles Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM (Mile per Gallon) Mobil')
engineSize = st.number_input('Input Ukuran Mesin Mobil')

predict = ' '

if st.button('Estimasi Harga'):
    predict = model.predict(
      [[year, mileage, tax, mpg, engineSize]]
      )
    
    conversion_rate = 20272
    
    st.write ('Estimasi harga mobil bekas dalam GBP :', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR :', predict * conversion_rate)
    
# streamlit run "d:/College/Semester 3/Fundamen Sains Data/Tugas/2/estimasi-mobil/estimasi-mobil.py"

