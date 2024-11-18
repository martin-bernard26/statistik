import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as sc
import openpyxl

st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="✨",
    layout="wide",  # Menggunakan lebar penuh layar
    initial_sidebar_state="expanded"  # Sidebar terbuka secara default
)
tuliskan_html=f'''
    <html>
    <head>
        <style>
            #posisi{{
                display:flex;
                justify-content:center;
                align-items:center;
            }}
            #posisi1{{
                font-family:broadway;
                font-size:20px;
                border:1px solid black;
                width:300px;
                height:150px;
                text-align:center;
            }}
        </style>
    </head>
    <body>
        <div id="posisi">
        <div><img src='https://dosen.ikipsiliwangi.ac.id/wp-content/uploads/sites/6/2018/03/foto-martin-bernard1.jpg' width='100' height='150'></div>
        <div id="posisi1">Martin Bernard
        <div style="font-size:15px;font-family:'comic sans ms'">Dosen: Aplikasi Statistika</div>
        <div><img src='https://tse2.mm.bing.net/th?id=OIP.03vx1XM76ErNKfG7EASETgHaHa&pid=Api&P=0&h=220' width='100' height='100'></div>
        </div>
        </div>
    </body>
    </html>
'''
st.components.v1.html(tuliskan_html,height=150,width=400)
st.title("Aplikasi Satistik")

halaman = st.sidebar.selectbox("Uji 1 sampel",["Streamlit","Gradio","Google Colab"])

tab1, tab2 = st.tabs(["Uji 1 Sampel","Uji 2 Sampel dependen"])

with tab1:
    if halaman=="Streamlit":
        st.header("Uji 1 Sampel")
        st.markdown('''Sebelum melakukan uji t satu sampel, penting untuk memastikan bahwa data sampel mengikuti distribusi normal,
karena uji t satu sampel membutuhkan asumsi normalitas pada data. Berikut adalah langkah-langkah
dari uji normalitas hingga melakukan uji t satu sampel:''')
        html1="<h2>Uji Normalitas</h2>"
        st.components.v1.html(html1, height=50)
        html2=f'''
            <ul>
                <li>Tujuan: Memastikan data sampel mengikuti distribusi normal.</li>
                <li>Alat Uji:
                    <ul>
                        <li>Shapiro-Wilk Test: Cocok untuk sampel kecil (<50).</li>
                        <li>Kolmogorov-Smirnov Test atau Lilliefors Test: Cocok untuk sampel besar.</li>
                        
                    </ul>
                </li>
                <li>Hipotesis:
                    <ul>
                        <li>H0: Data mengikuti distribusi normal.</li>
                        <li>H1: Data tidak mengikuti distribusi normal.</li>
                    </ul>
                </li>
                <li>Keputusan:
                    <ul>
                        <li>Jika p-value < αα, tolak H0 (data tidak normal).</li>
                        <li>Jika p-value ≥≥ αα, gagal tolak H0 (data normal).</li>
                    </ul>
                </li>
            </ul>
            '''
        st.components.v1.html(html2,height=100)
        st.code('''
                from scipy import stats

# Data sampel
data = [85, 90, 88, 75, 95]

# Uji Shapiro-Wilk
stat, p_value = stats.shapiro(data)
alpha = 0.05

print(f"Shapiro-Wilk Test Statistic: {stat}")
print(f"p-value: {p_value}")

if p_value < alpha:
    print("Data tidak berdistribusi normal.")
else:
    print("Data berdistribusi normal.")

            ''')
        html3="<h2>Menentukan Hipotesis Uji t Satu Sampel</h2>"
        st.components.v1.html(html3, height=50)
        html4=f'''
            <head>
                <script>
                MathJax = {{
                tex: {{
                    inlineMath: [['$', '$'], ['\\[', '\\]']]
                }}
            }};
            </script>
            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
            </script>
            </head>
            <body>
            <ul>
                <li>Hipotesis nol (H0): Rata-rata sampel $(\\bar{{X}})$ sama dengan nilai pembanding atau rata-rata populasi (μ0).</li>
                <li>Hipotesis alternatif (H1): Rata-rata sampel tidak sama dengan nilai pembanding (μ0​).</li>
            </ul>
            </body>
            '''
        st.components.v1.html(html4,height=90)
        html5="<h2>Menentukan Tingkat Signifikansi (α)</h2>"
        st.components.v1.html(html5, height=60)
        html6=f'''
            <ul>
                <li>Tentukan tingkat signifikansi, biasanya α=0.05.</li>
            </ul>
            '''
        st.components.v1.html(html6,height=50)
        html7="<h2>Menentukan Tingkat Signifikansi (α)</h2>"
        st.components.v1.html(html7, height=50)
        html8=f'''
            <ul>
                <li>Tentukan tingkat signifikansi, biasanya α=0.05.</li>
            </ul>
            '''
        st.components.v1.html(html8,height=50)
        st.code('''
    from scipy import stats

# Data sampel
data = [85, 90, 88, 75, 95]
nilai_pembanding = 80
alpha = 0.05

# Uji Normalitas (Shapiro-Wilk)
stat, p_value_normalitas = stats.shapiro(data)
print(f"Shapiro-Wilk Test Statistic: {stat}, p-value: {p_value_normalitas}")

if p_value_normalitas < alpha:
    print("Data tidak berdistribusi normal. Pertimbangkan uji non-parametrik.")
else:
    print("Data berdistribusi normal. Lanjutkan dengan uji t satu sampel.")

    # Uji t satu sampel
    t_stat, p_value_ttest = stats.ttest_1samp(data, nilai_pembanding)
    print(f"t-statistik: {t_stat}")
    print(f"p-value uji t satu sampel: {p_value_ttest}")

    # Kesimpulan uji t satu sampel
    if p_value_ttest < alpha:
        print("Tolak H0: Rata-rata sampel berbeda secara signifikan dari nilai pembanding.")
    else:
        print("Gagal tolak H0: Tidak ada perbedaan signifikan antara rata-rata sampel dan nilai pembanding.")

    ''')
        html8="<h2>Menghitung Statistik Sampel</h2>"
        st.components.v1.html(html8, height=50)
        html9=f'''
            <head>
                <script>
                MathJax = {{
                tex: {{
                    inlineMath: [['$', '$'], ['\\[', '\\]']]
                }}
            }};
            </script>
            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
            </script>
            </head>
            <body>
            <ul>
                <li>Kumpulkan data, lalu hitung rata-rata sampel $(\\bar{{x}})$, standar deviasi sampel (s), dan jumlah sampel (n).</li>
            </ul>
            </body>
            '''
        st.components.v1.html(html9,height=50)
        html10="<h2>Menghitung Statistik Sampel</h2>"
        st.components.v1.html(html10, height=50)
        html11=f'''
            <head>
                 <style>
                li:first-child{{
                font-size:20px;
                }}
                </style>
                <script>
                MathJax = {{
                tex: {{
                    inlineMath: [['$', '$'], ['\\[', '\\]']]
                }}
            }};
            </script>
            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
            </script>
            </head>
            <body>
            <ul>
                <li>Rumus t:
                    $t=\\frac{{\\bar{{X}}-\\mu_{{0}}}}{{\\frac{{s}}{{\\sqrt{{n}}}}}}$
                </li>
            </ul>
            </body>
            '''
        st.components.v1.html(html11,height=100)
        st.subheader("Upload file anda dengan extensi xlxs")
        upload = st.file_uploader("upload file anda")
        if upload:
            data = pd.read_excel(upload)
            st.table(data)
            st.subheader("Data Deskripsi")
            st.write(data.describe())
            st.subheader("Test Normalitas")
            st.markdown("Menggunakan Shapiro-wilks")
            st.table(sc.shapiro(data['Nilai']))
            st.markdown("Menggunakan Kolmogorov-smirnov")
            st.table(sc.kstest(data['Nilai'], 'norm', args=(np.mean(data['Nilai']), np.std(data['Nilai'], ddof=1))))
            st.subheader("Uji Rata-rata 1 sampel")
            pilih = st.radio('Pilih Uji Rata-rata',['Uji t 1 sampel','Uji Wilcoxon Signed-Rank Test'])
            nilai = st.text_input("Masukan nilai pembanding")
            if nilai:
                if pilih =="Uji t 1 sampel":
                    uji=sc.ttest_1samp(data['Nilai'],float(nilai))
                    st.table(uji)
                else:
                    uji=sc.wilcoxon(data['Nilai']-float(nilai))
                    st.table(uji)
    elif halaman=="Gradio":
        st.header("Rumus python di Gradio")
        st.markdown("<h5>Uji Normalitas</h5>",unsafe_allow_html=True)
        st.code('''
import gradio as gr
import pandas as pd
from scipy.stats import shapiro

def uji_normalitas(file, column_name):
    # Membaca file Excel
    try:
        df = pd.read_excel(file.name)
    except Exception as e:
        return f"Error membaca file: {e}"
    
    # Memastikan kolom yang diminta ada
    if column_name not in df.columns:
        return f"Kolom '{column_name}' tidak ditemukan dalam file Excel."
    
    # Mengambil data dari kolom yang diminta
    try:
        data = df[column_name].dropna().astype(float)  # Mengabaikan nilai kosong dan mengonversi ke float
    except ValueError:
        return "Kolom mengandung nilai non-numerik. Pastikan semua data di kolom adalah angka."
    
    # Melakukan uji normalitas Shapiro-Wilk
    stat, p_value = shapiro(data)
    
    # Interpretasi hasil
    if p_value > 0.05:
        hasil = "Data berdistribusi normal (Gagal tolak H₀)"
    else:
        hasil = "Data tidak berdistribusi normal (Tolak H₀)"
    
    return (
        f"Statistik Shapiro-Wilk: {stat:.4f}\n"
        f"P-Value: {p_value:.4f}\n"
        f"Kesimpulan: {hasil}"
    )

# Membuat antarmuka Gradio
demo = gr.Interface(
    fn=uji_normalitas,
    inputs=[
        gr.File(label="Upload File Excel", file_types=[".xls", ".xlsx"]),
        gr.Textbox(label="Nama Kolom Data", placeholder="Masukkan nama kolom (case-sensitive)"),
    ],
    outputs="text",
    title="Uji Normalitas Data 1 Sampel",
    description="Unggah file Excel dan pilih kolom untuk menguji normalitas data menggunakan uji Shapiro-Wilk."
)

demo.launch()

                ''')
        st.markdown("<h5>Uji t 1 sampel</h5>",unsafe_allow_html=True)
        st.code('''
import gradio as gr
import pandas as pd
from scipy.stats import ttest_1samp

def one_sample_t_test(file, column_name, population_mean):
    # Membaca data dari file Excel
    try:
        df = pd.read_excel(file.name)
    except Exception as e:
        return f"Error membaca file: {e}"
    
    # Memastikan kolom yang diminta ada
    if column_name not in df.columns:
        return f"Kolom '{column_name}' tidak ditemukan dalam file Excel."
    
    # Mengambil data dari kolom yang diminta
    try:
        data = df[column_name].dropna().astype(float)  # Mengabaikan nilai kosong dan mengonversi ke float
    except ValueError:
        return "Kolom mengandung nilai non-numerik. Pastikan semua data di kolom adalah angka."
    
    # Melakukan uji 1 sampel
    t_stat, p_value = ttest_1samp(data, float(population_mean))
    
    # Interpretasi hasil
    interpretasi = "Gagal tolak H₀" if p_value > 0.05 else "Tolak H₀"
    
    return (
        f"Rata-rata sampel: {data.mean():.2f}\n"
        f"T-Statistik: {t_stat:.2f}\n"
        f"P-Value: {p_value:.4f}\n"
        f"Kesimpulan: {interpretasi}"
    )

# Membuat antarmuka Gradio
demo = gr.Interface(
    fn=one_sample_t_test,
    inputs=[
        gr.File(label="Upload File Excel", file_types=[".xls", ".xlsx"]),
        gr.Textbox(label="Nama Kolom Data", placeholder="Masukkan nama kolom (case-sensitive)"),
        gr.Number(label="Rata-rata Populasi (µ₀)", placeholder="Masukkan nilai rata-rata populasi"),
    ],
    outputs="text",
    title="Uji 1 Sampel dari File Excel",
    description="Unggah file Excel, pilih kolom data, dan masukkan rata-rata populasi untuk melakukan uji 1 sampel."
)

demo.launch()

                ''')
        st.markdown("<h5>Uji 1 sampel Wilcoxon</h5>",unsafe_allow_html=True)
        st.code('''
import gradio as gr
import pandas as pd
from scipy.stats import wilcoxon

def uji_wilcoxon(file, column_name, median_value):
    # Membaca file Excel
    try:
        df = pd.read_excel(file.name)
    except Exception as e:
        return f"Error membaca file: {e}"
    
    # Memastikan kolom yang diminta ada
    if column_name not in df.columns:
        return f"Kolom '{column_name}' tidak ditemukan dalam file Excel."
    
    # Mengambil data dari kolom yang diminta
    try:
        data = df[column_name].dropna().astype(float)  # Mengabaikan nilai kosong dan mengonversi ke float
    except ValueError:
        return "Kolom mengandung nilai non-numerik. Pastikan semua data di kolom adalah angka."
    
    # Melakukan uji Wilcoxon terhadap nilai median yang diberikan
    try:
        median_value = float(median_value)
    except ValueError:
        return "Masukkan nilai median yang valid."
    
    stat, p_value = wilcoxon(data - median_value)
    
    # Interpretasi hasil
    if p_value > 0.05:
        hasil = "Gagal menolak H₀ (Tidak ada perbedaan signifikan)"
    else:
        hasil = "Tolak H₀ (Ada perbedaan signifikan)"
    
    return (
        f"Statistik Uji Wilcoxon: {stat:.2f}\n"
        f"P-Value: {p_value:.4f}\n"
        f"Kesimpulan: {hasil}"
    )

# Membuat antarmuka Gradio
demo = gr.Interface(
    fn=uji_wilcoxon,
    inputs=[
        gr.File(label="Upload File Excel", file_types=[".xls", ".xlsx"]),
        gr.Textbox(label="Nama Kolom Data", placeholder="Masukkan nama kolom (case-sensitive)"),
        gr.Number(label="Nilai Median yang Diharapkan", placeholder="Masukkan nilai median yang diinginkan"),
    ],
    outputs="text",
    title="Uji Wilcoxon 1 Sampel",
    description="Unggah file Excel dan pilih kolom untuk melakukan uji Wilcoxon terhadap median yang diharapkan."
)

demo.launch()

                ''')
    if halaman=="Google Colab":
        st.header("Rumus python di Google Colab")
        st.markdown("<h5>Upload data dari Excel</h5>",unsafe_allow_html=True)
        st.code('''
from google.colab import files
uploaded = files.upload()
                ''')
        st.markdown("<h5>Membaca File Excel dengan Pandas</h5>",unsafe_allow_html=True)
        st.code('''
import pandas as pd

# Membaca file Excel (ganti 'nama_file.xlsx' dengan nama file yang di-upload)
df = pd.read_excel('nama_file.xlsx')

# Lihat beberapa data pertama untuk memastikan
df.head()
                ''')
        
        st.markdown("<h5>Membaca File Excel dengan Pandas</h5>",unsafe_allow_html=True)
        st.code('''
from scipy.stats import shapiro

# Misalnya data yang diuji ada pada kolom 'nilai' (sesuaikan dengan nama kolom Anda)
nilai = df['nilai']  # Ganti 'nilai' dengan nama kolom data Anda

# Uji Shapiro-Wilk
stat, p_value = shapiro(nilai)

print("Statistik Shapiro-Wilk:", stat)
print("p-value:", p_value)

# Interpretasi hasil
if p_value < 0.05:
    print("H0 ditolak: Data tidak terdistribusi normal")
else:
    print("H0 diterima: Data terdistribusi normal")
                ''')
        st.markdown("<h5>Uji Normalitas</h5>",unsafe_allow_html=True)
        st.code('''
from scipy.stats import shapiro

# Misalnya data yang diuji ada pada kolom 'nilai' (sesuaikan dengan nama kolom Anda)
nilai = df['nilai']  # Ganti 'nilai' dengan nama kolom data Anda

# Uji Shapiro-Wilk
stat, p_value = shapiro(nilai)

print("Statistik Shapiro-Wilk:", stat)
print("p-value:", p_value)

# Interpretasi hasil
if p_value < 0.05:
    print("H0 ditolak: Data tidak terdistribusi normal")
else:
    print("H0 diterima: Data terdistribusi normal")
                ''')
        st.markdown("<h5>Uji t 1 sampel</h5>",unsafe_allow_html=True)
        st.code('''
from scipy import stats

# Misalnya data yang diuji ada pada kolom 'nilai' dan Anda ingin menguji apakah rata-rata sama dengan nilai tertentu (misalnya 70)
nilai = df['nilai']  # Sesuaikan nama kolom dengan data Anda
nilai_tes = 70  # Nilai yang ingin diuji

# Uji t 1 sampel
t_stat, p_value = stats.ttest_1samp(nilai, nilai_tes)

print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpretasi hasil
if p_value < 0.05:
    print("H0 ditolak, rata-rata berbeda dari", nilai_tes)
else:
    print("H0 diterima, rata-rata tidak berbeda secara signifikan dari", nilai_tes)
                ''')
        st.markdown("<h5>Uji Wilcoxon 1 sampel</h5>",unsafe_allow_html=True)
        st.code('''
from scipy.stats import wilcoxon

# Misalnya data yang diuji ada pada kolom 'nilai' (ganti dengan nama kolom Anda)
nilai = df['nilai']  # Ganti 'nilai' dengan nama kolom data Anda

# Nilai yang ingin diuji terhadap median (misalnya 50)
nilai_tes = 50

# Menghitung perbedaan antara nilai sampel dan nilai yang diuji
perbedaan = nilai - nilai_tes

# Uji Wilcoxon
stat, p_value = wilcoxon(perbedaan)

print("Statistik Uji Wilcoxon:", stat)
print("p-value:", p_value)

# Interpretasi hasil
if p_value < 0.05:
    print("H0 ditolak: Data memiliki perbedaan signifikan dengan", nilai_tes)
else:
    print("H0 diterima: Data tidak memiliki perbedaan signifikan dengan", nilai_tes)

                ''')
        
    
                 
