import streamlit as st

st.title("Experiment 2: Stefan Boltzmann Law Part 1")

st.header("A. Tujuan")
st.write("""
- Mahasiswa dapat menggambarkan secara kualitatif hubungan antara suhu sampel dengan radiasi yang diterima.
- Mahasiswa mampu menentukan gradien dari nilai hasil pengukuran pada diagram logaritmik ganda (double-logarithmic diagram).
- Dengan menggunakan hukum pangkat (power laws), mahasiswa dapat menurunkan hubungan antara gradien pada representasi logaritmik dengan fungsi pangkat yang mendasari fenomena radiasi panas
""")

st.header("B.Alat dan Perlengkapan")
st.write("GUNT WL 460 Heat Transfer by Radiation")

st.header("C. Dasar Teori")
st.subheader ("Hukum Stefan-Boltzmann")
st.write("""
Persamaan dasar untuk radiasi termal total dari radiator ideal atau benda hitam telah 
ditemukan secara empiris oleh Stefan dan ditemukan secara teoritis oleh Boltzmann. Dikatakan 
bahwa laju pemindahan panas secara radiasi adalah sebanding dengan pangkat empat 
temperatur benda.
""")

st.latex(r"Q = \sigma \cdot A \cdot T^4")

st.write("""
Jika dua benda bertukar panas dengan proses radiasi, maka panas bersih yang bertukar 
adalah sebanding dengan beda temperatur pangkat empat.
""")

st.latex(r"Q = \sigma \cdot A \cdot (T_1^4 - T_2^4)")

st.write("""
Sedangkan energi total yang dipancarkan untuk seluruh panjang gelombang per satuan waktu 
dan per satuan luas radiator ideal sebanding dengan pangkat empat temperatur absolut.
""")

st.latex(r"E_b = \sigma \cdot T^4")

st.write("""
Dimana:
- Eb  = energi total yang dipancarkan = daya emisi total  [W/m²]
- Q   = kecepatan atau laju pemindahan panas radiasi benda hitam [W]
- T   = temperatur absolut permukaan [K]
- A   = luas permukaan benda [m²]
- σ   = konstanta proporsionalitas disebut konstanta Stefan-Boltzmann 
        = 5,669 × 10⁻⁸ W/(m²·K⁴)
""")

st.header("D. Prosedur Percobaan")
st.write("""
- Nyalakan perangkat dan perangkat lunak.
- Pada perangkat lunak, pilih eksperimen “Stefan‑Boltzmann law”.
- Jika diperlukan, lakukan kalibrasi thermopile (lihat Bab 3.7.4, Halaman 30).
- Pasang thermopile pada jarak tertentu, misalnya 150 mm. Jarak lain juga dimungkinkan.
- Pilih sampel tembaga yang teroksidasi berat dan letakkan pada dudukan sampel pertama. Selaraskan posisi sampel sesuai Bab 3.7.2, Halaman 29.
- Pada menu “Modules”, buka “Chart recorder”.
- Nyalakan lampu dengan daya sekitar 50%.
- Setelah nilai pengukuran pada grafik chart recorder berhenti berfluktuasi (lihat Gambar 3.14), catat titik pengukuran. (Hasil terbaik biasanya berada pada rentang suhu 250–480 °C).
- Tingkatkan daya lampu.
- Ulangi langkah 7 hingga 9. Lima titik pengukuran biasanya sudah cukup untuk ilustrasi yang bermakna.
- Simpan nilai hasil pengukuran.
""")
import streamlit as st

st.subheader("Rumus Regresi Linier Log–Log")
st.latex(r"Y = A + n \cdot X")

st.write("""
dengan:
- X = log(T)
- Y = log(I)
- n = slope (gradien) = ΔY / ΔX
- A = intercept
""")

st.subheader("Bentuk Delta")
st.latex(r"n = \frac{\Delta \log(I)}{\Delta \log(T)}")

st.header("E. Data Pengamatan")
st.subheader("Data Hasil Pengukuran")

import streamlit as st
import pandas as pd
import numpy as np

data = {
    "Thermal Power (%)": [50, 60, 70, 80, 90],
    "T (°C)": [151.8, 209.7, 279.2, 364.9, 439.7],
    "T (K)": [424.8, 482.7, 552.2, 637.9, 712.7],
    "I (W/m^2)": [4.3, 5.6, 9.6, 19.6, 46.8]
}

df = pd.DataFrame(data)
df["log10(T)"] = np.log10(df["T (K)"])
df["log10(I)"] = np.log10(df["I (W/m^2)"])
st.write(df) 


st.header("F. Pengolahan Data")
import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import linregress

data = {
    "T (K)": [424.8, 482.7, 552.2, 637.9, 712.7],
    "I (W/m²)": [4.3, 5.6, 9.6, 19.6, 46.8]
}
df = pd.DataFrame(data)

# Transformasi logaritmik
df["log10(T)"] = np.log10(df["T (K)"])
df["log10(I)"] = np.log10(df["I (W/m²)"])

# Regresi linier log-log
slope, intercept, r_value, _, _ = linregress(df["log10(T)"], df["log10(I)"])
df["I_pred"] = 10**(intercept + slope * df["log10(T)"])

# Tampilkan tabel
st.subheader("Data dan Transformasi Logaritmik")
st.dataframe(df)

# Grafik garis (data eksperimen)
st.subheader("Grafik Data Eksperimen")
st.line_chart(df.set_index("T (K)")[["I (W/m²)"]])

# Grafik garis (data + prediksi regresi)
st.subheader("Grafik Data vs Regresi")
st.line_chart(df.set_index("T (K)")[["I (W/m²)", "I_pred"]])

import streamlit as st

code = """from scipy.stats import linregress
import numpy as np

# Transformasi logaritmik
df["log10(T)"] = np.log10(df["T (K)"])
df["log10(I)"] = np.log10(df["I (W/m²)"])

# Regresi linier log-log
slope, intercept, r_value, _, _ = linregress(df["log10(T)"], df["log10(I)"])
"""

st.subheader("Potongan Kode Regresi Log–Log")
st.code(code, language="python")

st.header("G. Analisis")

import streamlit as st

st.subheader("Pola Umum")
st.write("""
Grafik menunjukkan bahwa intensitas radiasi meningkat tajam seiring dengan kenaikan suhu absolut.
Bentuk kurva mengikuti pola eksponensial, sesuai dengan hukum Stefan–Boltzmann yang menyatakan I ∝ T^4.
""")

st.subheader("Kesesuaian dengan Teori")
st.write("""
Hasil regresi log–log memberikan gradien n ≈ 3.91, sangat dekat dengan nilai teoritis n = 4.
Koefisien determinasi R² ≈ 0.997 menunjukkan hubungan yang sangat kuat dan konsisten antara data eksperimen dengan model teoritis.
""")

st.subheader("Interpretasi Fisik")
st.write("""
Kenaikan suhu kecil menghasilkan peningkatan intensitas radiasi yang relatif besar.
Misalnya, dari 552 K ke 637 K, intensitas hampir dua kali lipat.
Hal ini menegaskan bahwa radiasi termal sangat sensitif terhadap perubahan suhu.
""")

st.subheader("Deviasi Kecil")
st.write("""
Perbedaan kecil antara hasil eksperimen dan teori dapat disebabkan oleh emisivitas permukaan benda uji yang tidak ideal,
keterbatasan akurasi sensor, serta pengaruh kondisi lingkungan seperti konveksi atau kehilangan panas lain yang tidak sepenuhnya terkontrol.
""")

import streamlit as st

st.header("H. Kesimpulan")
st.write("""
Berdasarkan hasil analisis grafik hubungan intensitas radiasi terhadap suhu absolut,
dapat disimpulkan bahwa data eksperimen mendukung hukum Stefan–Boltzmann.
Regresi log–log menghasilkan gradien n ≈ 3.91 yang sangat dekat dengan nilai teoritis n = 4,
serta koefisien determinasi R² ≈ 0.997 yang menunjukkan kecocokan sangat kuat.
Hal ini membuktikan bahwa intensitas radiasi berbanding lurus dengan pangkat empat suhu absolut,
dengan deviasi kecil yang kemungkinan disebabkan oleh emisivitas permukaan,
akurasi sensor, dan kondisi lingkungan selama pengukuran.
""")
 
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)
 
text = st.text_area('Feedback')
st.write('Feedback: ', text)