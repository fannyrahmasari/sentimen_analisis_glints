import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# Load save model
model_fraud = pickle.load(open('model_sentimen_glints.sav', 'rb'))

tfidf = TfidfVectorizer
# loaded_voc = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))

# Judul Halaman
st.title ("Analisis Sentimen Aplikasi Glints")

clean_text = st.text_input('Masukan Teks Komentar')

fraud_detection = ''

if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(model_fraud.fit_transform([clean_text]))

    if (predict_fraud == 0):
        fraud_detection = 'Komentar Negatif'
    if (predict_fraud == 1):
        fraud_detection = 'Komentar Positif'
    else:
        fraud_detection = 'Komentar tidak diketahui'
st.success(fraud_detection)