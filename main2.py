# library
import streamlit as st

st.title ('APLIKASI SERBAGUNA ')

         
# write
st.write('Ini adalah Website buatan mimiperi')
st.subheader('khusus cat lovers yang mau ngitung :cat:')

animals = st.radio (
    " What/'s your pet",
    ('Dog', 'cat', 't-rex'))

if animals == 'cat':
    st.write (' kamu cat lovers')
else :
    st.write ('kamu tidak bisa masuk sircle ini')
    
picture = st.camera_input ('Take a picture : KAMI BUTUH BUKTI')

if picture :
    st.image(picture)
    
# input bilangan pertama 
number1 = st.number_input (' Masukan bilangan yng kamu mau ')
st.write(f'Bilangan yang kamu mau {number1}')

# input bilangan kedua
number2 = st.number_input (' Masukan bilangan seccond choise kmu ')
st.write(f'Bilangan seccond choise kamu {number2}')

# hasil tambah
hasil = number1 + number2

if st.button ('hitung') : 
    st.write(f'hasil tambah antara {number1} dan {number2} adalah {hasil} good chooise :sunglasses:')
else :
    st.write ('silikan tekan hasil pilihan mu :question:')





