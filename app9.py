import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

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
        tulisan_penting='''
        <html>
        <head>
            <style>
                #konsep{
                    font-family:broadway;
                    font-size:20px;
                    color:red;
                    background-color:cyan;
                    transform:translate(0px);
                    animation-name:jalankan;
                    animation-duration:3s;
                    animation-iteration-count:infinite;
                    animation-direction: alternate;
                }
                @keyframes jalankan{
                    0%{color:red;transform:translate(0px)}
                    100%{color:black;transform:translate(100px)}
                }
            </style>
        </head>
        <body>
        <div id="konsep">Petunjuk sebelum mengupload data</div>
        <div style="text-align:center;margin:5px;background-color:orange;padding:5px;"><iframe src="https://res.cloudinary.com/ikip-siliwangi/image/upload/v1732108396/xiyvjxxfybupumrhjx3o.png" width="300" height="300"></iframe></div>
        <div style="font-family:'comic sans ms';font-size:20px;border:2px solid black;border-radius:10px;box-shadow:2px 2px 2px 2px blue">
            <ol>
                <li>perhatikan gambar di atas  ada 2 kolom, kolom A untuk nama siswa, dan kolom B untuk Nilai</li>
                <li>Nama kolom dibebaskan menurut pengguna</li>
                <li>Kolom hanya diisi pada kolom A dan B saja.</li>
            </ol>
        </div>
        </body>
        </html>
        '''
        st.components.v1.html(tulisan_penting,height=550)
        st.subheader("Upload file anda dengan extensi xlxs")
        upload = st.file_uploader("upload file anda")
        if upload:
            data = pd.read_excel(upload)
            st.table(data)
            st.subheader("Data Deskripsi")
            st.write(data.describe())
            st.subheader("Test Normalitas")
            st.markdown("Menggunakan Shapiro-wilks")
            st.table(sc.shapiro(data[data.keys()[1]]))
            st.markdown("Menggunakan Kolmogorov-smirnov")
            st.table(sc.kstest(data[data.keys()[1]], 'norm', args=(np.mean(data[data.keys()[1]]), np.std(data[data.keys()[1]], ddof=1))))
            st.subheader("Uji Rata-rata 1 sampel")
            pilih = st.radio('Pilih Uji Rata-rata',['Uji t 1 sampel','Uji Wilcoxon Signed-Rank Test'])
            nilai = st.text_input("Masukan nilai pembanding")
            if nilai:
                if pilih =="Uji t 1 sampel":
                    uji=sc.ttest_1samp(data[data.keys()[1]],float(nilai))
                    st.table(uji)
                else:
                    uji=sc.wilcoxon(data[data.keys()[1]]-float(nilai))
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
    with tab2:
        st.header("Uji 2 Sampel Dependen")
        st.markdown('''<h5>Uji dua sampel dependen (juga disebut sebagai paired sample test) digunakan untuk
membandingkan rata-rata dua kelompok data yang berpasangan (misalnya, pengukuran sebelum dan sesudah dari
individu yang sama). Berikut adalah langkah-langkah untuk melakukan uji ini:</h5>''',unsafe_allow_html=True)
        st.markdown('''<h4>Langkah 1: Formulasi Hipotesis</h4>''',unsafe_allow_html=True)
        st.markdown('''<h5><ul>
        <li>Hipotesis Nol (H₀): Tidak ada perbedaan rata-rata antara dua kelompok (selisih rata-rata = 0).</li>
        <li>Hipotesis Alternatif (H₁): Ada perbedaan rata-rata antara dua kelompok (selisih rata-rata ≠ 0).</li>
        </ul></h5>''',unsafe_allow_html=True)
        st.markdown('''<h4>Langkah 2: Tentukan Metode Uji</h4>''',unsafe_allow_html=True)
        st.markdown('''<h5>Metode yang sering digunakan untuk uji dua sampel dependen:<ul>
        <li>Uji t berpasangan (Paired t-test) Digunakan jika data berdistribusi normal.</li>
        <li>Uji Wilcoxon Signed-Rank Digunakan jika data tidak berdistribusi normal (non-parametrik)</li>
        </ul></h5>''',unsafe_allow_html=True)
        st.markdown('''<h4>Langkah 3: Persiapkan Data</h4>''',unsafe_allow_html=True)
        st.markdown('''<h5>Data harus terdiri dari dua kolom:<ul>
        <li>Kolom 1: Data kelompok pertama (misalnya, sebelum perlakuan).</li>
        <li>Kolom 2: Data kelompok kedua (misalnya, setelah perlakuan).</li>
        </ul></h5>''',unsafe_allow_html=True)
        st.markdown('''<h4>Langkah 4: Analisis Data</h4>''',unsafe_allow_html=True)
        st.markdown('''<h5>A. Uji Normalitas</h5>''',unsafe_allow_html=True)
        st.markdown('''<h6>Periksa apakah data selisih berdistribusi normal. Ini menentukan apakah Anda
menggunakan uji parametrik atau non-parametrik.
<ul>
<li>Hitung selisih: selisih=setelah−sebelum.</li>
<li>Lakukan uji normalitas pada data selisih menggunakan Shapiro-Wilk atau Kolmogorov-Smirnov.</li>
</ul></h6>''',unsafe_allow_html=True)
        st.markdown('''<h5>Python (Shapiro-Wilk):</h5>''',unsafe_allow_html=True)
        st.code('''
from scipy.stats import shapiro
# Misalnya selisih adalah array numpy
selisih = setelah - sebelum
stat, p = shapiro(selisih)
print("Statistik Shapiro-Wilk:", stat)
print("p-value:", p)

if p < 0.05:
    print("Data tidak terdistribusi normal (gunakan Wilcoxon)")
else:
    print("Data terdistribusi normal (gunakan Paired t-test)")

''')
        st.markdown('''<h5>B. Uji Paired t-test (Jika Data Normal)</h5>''',unsafe_allow_html=True)
        st.markdown('''<h6>Gunakan paired t-test untuk membandingkan dua kelompok:</h6>''',unsafe_allow_html=True)
        st.markdown('''<h5>Python (Paired t-test):</h5>''',unsafe_allow_html=True)
        st.code('''
from scipy.stats import ttest_rel

# Data
sebelum = [85, 78, 88, 95]
setelah = [90, 80, 85, 92]

# Paired t-test
stat, p = ttest_rel(sebelum, setelah)
print("Statistik t:", stat)
print("p-value:", p)

if p < 0.05:
    print("H0 ditolak: Ada perbedaan signifikan")
else:
    print("H0 diterima: Tidak ada perbedaan signifikan")

''')
        st.markdown('''<h5>C. Uji Wilcoxon (Jika Data Tidak Normal)</h5>''',unsafe_allow_html=True)
        st.markdown('''<h6>Gunakan Wilcoxon Signed-Rank Test jika data tidak normal.</h6>''',unsafe_allow_html=True)
        st.markdown('''<h5>Python (Wilcoxon Test):</h5>''',unsafe_allow_html=True)
        st.code('''
from scipy.stats import wilcoxon

# Wilcoxon Signed-Rank Test
stat, p = wilcoxon(sebelum, setelah)
print("Statistik Wilcoxon:", stat)
print("p-value:", p)

if p < 0.05:
    print("H0 ditolak: Ada perbedaan signifikan")
else:
    print("H0 diterima: Tidak ada perbedaan signifikan")

''')
        st.markdown('''<h4>Langkah 5: Interpretasi Hasil</h4>''',unsafe_allow_html=True)
        st.markdown('''<ol>
<li>p-value < 0.05: Tolak H₀, ada perbedaan signifikan antara dua kelompok.</li>
<li>p-value ≥ 0.05: Terima H₀, tidak ada perbedaan signifikan antara dua kelompok.</li>
</ol>''',unsafe_allow_html=True)
        st.markdown('''<h4>Langkah 6: Visualisasi (Opsional)</h4>''',unsafe_allow_html=True)
        st.markdown('''<h5>Untuk melihat perbedaan secara visual, Anda bisa membuat boxplot atau barplot.</h5>''',unsafe_allow_html=True)
        st.code('''
import matplotlib.pyplot as plt

plt.boxplot([sebelum, setelah], labels=["Sebelum", "Setelah"])
plt.title("Perbandingan Sebelum dan Setelah")
plt.ylabel("Nilai")
plt.show()
''')
        data = st.file_uploader("Masukan data excel 2 sampel dependen")
        if data:
            data1 = pd.read_excel(data)
            st.table(data1)
            st.subheader("Deskripsi Data")
            st.table(data1.describe())
            st.subheader("Uji Normalitas")
            bagian = st.columns(2)
            bagian[0].table(sc.shapiro(data1[data1.keys()[1]]))
            bagian[1].table(sc.shapiro(data1[data1.keys()[2]]))
            st.subheader("Uji Rata-rata")
            pilih = st.radio("pilih",["Uji t 2 sampel dependen","Uji Wilcoxon"])
            if pilih=="Uji t 2 sampel dependen":
                uji = sc.ttest_rel(data1[data1.keys()[1]],data1[data1.keys()[2]])
                st.table(uji)
            elif pilih=="Uji Wilcoxon":
                uji = sc.wilcoxon(data1[data1.keys()[1]],data1[data1.keys()[2]])
                st.table(uji)
            st.subheader("Gambar Plot")
            plt.boxplot([data1[data1.keys()[1]],data1[data1.keys()[2]]],labels=[data1.keys()[1],data1.keys()[2]])
            plt.title("Perbandingan sebelum dan sesudah")
            plt.ylabel("Nilai")
            st.pyplot(plt)
            
                
tuliskan_ke_html='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Upload File ke Firebase Storage</title>
</head>
<body>
  <h1>Masukan Tugas Anda di sini ya...</h1>
  <input type="file" id="fileInput">
  <button id="uploadFile">Upload</button>
  <p id="uploadStatus"></p>

  <script type="module">
    // Import Firebase SDK
    import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
    import { getStorage, ref, uploadBytesResumable, getDownloadURL } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-storage.js";

    // Konfigurasi Firebase
    const firebaseConfig = {
        apiKey: "AIzaSyCIWubByRLqe8hBSstJmHZZBHIkjGHHG3g",
        authDomain: "latihan-eef99.firebaseapp.com",
        databaseURL: "https://latihan-eef99-default-rtdb.firebaseio.com",
        projectId: "latihan-eef99",
        storageBucket: "latihan-eef99.appspot.com",
        messagingSenderId: "543970413152",
        appId: "1:543970413152:web:1d34e4e7797e0567905105"
    };

    // Inisialisasi Firebase
    const app = initializeApp(firebaseConfig);
    const storage = getStorage(app);

    // Elemen HTML
    const fileInput = document.getElementById('fileInput');
    const uploadButton = document.getElementById('uploadFile');
    const uploadStatus = document.getElementById('uploadStatus');

    // Fungsi untuk upload file
    uploadButton.addEventListener('click', () => {
      const file = fileInput.files[0]; // Ambil file dari input
      if (!file) {
        alert('Pilih file terlebih dahulu!');
        return;
      }

      const storageRef = ref(storage, `uploads/${file.name}`); // Lokasi penyimpanan di Firebase Storage
      const uploadTask = uploadBytesResumable(storageRef, file);

      // Observasi status unggahan
      uploadTask.on(
        'state_changed',
        (snapshot) => {
          // Progress upload
          const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
          uploadStatus.textContent = `Upload sedang berlangsung: ${progress.toFixed(2)}%`;
        },
        (error) => {
          // Tangani error
          console.error('Error saat mengunggah:', error);
          uploadStatus.textContent = `Gagal mengunggah: ${error.message}`;
        },
        () => {
          // Berhasil upload
          getDownloadURL(uploadTask.snapshot.ref).then((url) => {
            console.log('File berhasil diunggah dan tersedia di URL:', url);
            uploadStatus.innerHTML = `Berhasil diunggah! <a href="${url}" target="_blank">Unduh file</a>`;
          });
        }
      );
    });
  </script>
</body>
</html>
'''
st.components.v1.html(tuliskan_ke_html)
tuliskan_ke_html1='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #judul{
            font-family:"bauhaus 93";
            font-size:40px;
            color:green;
            text-shadow:2px 2px 2px red;
        }
        .samakan{
            font-family:'comic sans ms';
            font-size:15px;
            font-weight:bold;
        }
        .gambar{
            border:2px solid black;
            justify-content: center;
            align-items: center;
        }
        #kirim{
            font-family:Elephant;
            font-size:15px;
            width:100px;
            margin-bottom:5px;
        }
    </style>
</head>
<body>
    <div id="judul">Ruang Diskusi</div>
    <div class="samakan">Nama: <input id="nama" type="text"></div>
    <div class="samakan">Diskusi atau masukan:</div>
    <div><textarea id="pendapat" cols="50" rows="10"></textarea></div>
    <div ><button id="kirim" >Kirim</button></div>
    <div><table id="dataTable"></table></div>
        <script type="module">
            // Import Firebase modules
            import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
            import { getDatabase, ref, set, get, update, remove, onValue } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";
        
            // Firebase configuration
            const firebaseConfig = {
                apiKey: "AIzaSyCkgVmk75UTkos2y1Mrc7d3-sxShMfbeJQ",
                authDomain: "natural-ethos-423713-e0.firebaseapp.com",
                databaseURL: "https://natural-ethos-423713-e0-default-rtdb.firebaseio.com",
                projectId: "natural-ethos-423713-e0",
                storageBucket: "natural-ethos-423713-e0.firebasestorage.app",
                messagingSenderId: "41833960811",
                appId: "1:41833960811:web:6218d6ac2f3538c704e82e",
            };
        
            // Initialize Firebase
            const app = initializeApp(firebaseConfig);
            const db = getDatabase(app);

            var kirim = document.getElementById("kirim")
            var dataTable = document.getElementById("dataTable")
            kirim.addEventListener("click",()=>{
                var nama = document.getElementById("nama").value 
                var pendapat = document.getElementById("pendapat").value 
                const uniqueKey = Date.now();
                if(nama && pendapat){
                set(ref(db,"diskusi/"+uniqueKey),{
                    nama:nama,
                    pendapat:pendapat
                    tanggal:uniqueKey.toISOString()
                })
                .then(() => {
                    alert('Data added successfully');
                })
                .catch((error) => {
                    console.error("Error adding data:", error);
                });
                }else{
                    alert("Nama atau Pendapat masih kosong")
                }
            })
            onValue(ref(db, 'diskusi'), (snapshot) => {
                    dataTable.innerHTML = '';
                    const data = snapshot.val();
                    for (let key in data) {
                        const row = `
                        <tr style="margin:5px;background-color:orange;padding:5px;">
                        <td style="border:1px solid black;background-color:cyan">${data[key].nama}</td>
                        <td style="border:1px solid black;background-color:cyan">${data[key].tanggal}</td>
                        <td style="border:1px solid black;background-color:yellow">${data[key].pendapat}</td>
                        <td>
                        <button onclick="updateData('${key}')">Update</button>
                        <button onclick="deleteData('${key}')">Delete</button>
                        </td>
                        </tr>`;
                        dataTable.innerHTML += row;
                    }
                });
                window.updateData = (key) => {
                const namaBaru = prompt("Masukan nama baru:");
                const pendapatBaru = prompt("Masukan Pendapat Baru:");
                const uniqueKey = Date.now().toISOString();
                if (namaBaru && pendapatBaru) {
                    update(ref(db, 'diskusi/' + key), { nama: namaBaru, pendapat: pendapatBaru })
                .then(() => {
                alert('Data updated successfully');
                })
                .catch((error) => {
                console.error("Error updating data:", error);
                 });
            }
            };
            // Delete data from Firebase
    window.deleteData = (key) => {
      if (confirm("Are you sure you want to delete this data?")) {
        remove(ref(db, 'diskusi/' + key))
          .then(() => {
            alert('Data deleted successfully');
          })
          .catch((error) => {
            console.error("Error deleting data:", error);
          });
      }
    };
  </script>

        </script>
</body>
</html>
'''    
st.components.v1.html(tuliskan_ke_html1,height=1000,width=600)                  
    
                 
