import streamlit as st
import os
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Katalog Sistem Analisis & Simulasi Data", layout="wide")

# --- DATA DASHBOARD (HARDCODED & AMAN) ---
# Jika ingin menambah dashboard baru, cukup tambahkan di dalam list ini
daftar_dashboard = [
    {
        "title": "Sensitivitas Minyak Indonesia",
        "desc": "Calculate fiscal impact of oil price and exchange rate changes",
        "url": "https://harga-minyak-dunia.streamlit.app/"
    },
    {
        "title": "Swasembada Energi Simulasi",
        "desc": "Simulate energy & economic impacts of vehicle electrification",
        "url": "https://elektrifikasi-kendaraan.streamlit.app/"
    },
    {
        "title": "Dashboard Dampak Ekonomi Jalan Jabar",
        "desc": "Calculate economic impact of West Java road projects",
        "url": "https://huggingface.co/spaces/aliftowew/dashboard-dampak-ekonomi-jalan-jabar"
    },
    {
        "title": "Dashboard Dampak Ekonomi KDKMP",
        "desc": "Dampak Ekonomi KDKMP",
        "url": "https://huggingface.co/spaces/aliftowew/Dashboard-Dampak-Ekonomi-KDKMP"
    },
    {
        "title": "Prediksi Pangan Indonesia",
        "desc": "Memprediksi harga pangan Indonesia",
        "url": "https://prediksi-pangan-indonesia.streamlit.app/"
    },
    {
        "title": "Kalkulator Kebijakan WFH",
        "desc": "Dashboard kalkulasi kebijakan WFH",
        "url": "https://kalkulator-kebijakan-wfh.streamlit.app/"
    },
    {
        "title": "Elastisitas PDB & Lapangan Kerja",
        "desc": "Dashboard analisis elastisitas PDB terhadap lapangan kerja",
        "url": "https://elastisitas-pdb-lapangan-kerja.streamlit.app/"
    },
    {
        "title": "Kalkulator Subsidi Listrik PSEL",
        "desc": "Dashboard analisis subsidi listrik PSEL",
        "url":"https://kalkulator-wte.streamlit.app/"
    }
    {
        "title": "Dashboard Solar B50",
        "desc": "Kalkulator analisis kebijakan Solar B50",
        "url":"https://solar-dashboard-fuo1.vercel.app/"
    }
]


# --- FUNGSI UNTUK MEMUAT GAMBAR RUMUS KE BASE64 ---
def get_base64_of_image_file(png_file):
    if not os.path.exists(png_file):
        return ""
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Pastikan nama file sesuai dengan gambar rumus di GitHub (image_5.png)
img_rumus_b64 = get_base64_of_image_file("image_5.png")


# --- CSS KUSTOM PROFESIONAL ---
st.markdown(f"""
<style>
    /* Menyembunyikan tombol menu default Streamlit di pojok kanan atas (Opsional untuk keamanan ekstra) */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Styling Card (Kotak Aplikasi) */
    .dashboard-card {{
        border-radius: 6px;
        padding: 24px;
        margin-bottom: 20px;
        color: black;
        text-decoration: none !important;
        display: block;
        transition: all 0.2s;
        height: 140px;
        background-color: white; 
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    .dashboard-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-decoration: none !important;
        color: black;
    }}
    .card-title {{ font-size: 1.15rem; font-weight: bold; margin-bottom: 10px; color: black !important; }}
    .card-desc {{ font-size: 0.9rem; color: #6c757d !important; line-height: 1.4; }}
    
    /* Styling Footer dengan Gambar Transparan & Background Teks */
    .footer-container {{
        margin-top: 50px;
        border-top: 1px solid #e2e8f0;
        /* Overlay putih agar gambar rumus transparan sekitar 40% */
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url(data:image/png;base64,{img_rumus_b64});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 60px 20px;
        border-radius: 6px;
        text-align: center;
    }}
    .tagline-box {{
        background-color: #ffffff; /* Kotak putih solid */
        padding: 12px 30px;
        border-radius: 30px; /* Tepian melengkung */
        display: inline-block;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
    }}
    .footer-text {{
        color: #1e293b !important; 
        font-size: 0.95rem;
        margin: 0;
        line-height: 1.5;
    }}
    .tagline-title {{
        font-weight: 700;
        font-size: 1.05rem;
    }}
</style>
""", unsafe_allow_html=True)


# --- TAMPILAN UTAMA ---
st.title("Katalog Sistem Analisis & Simulasi Data")
st.markdown("Pusat integrasi dashboard untuk perhitungan ekonomi, energi, dan kebijakan strategis.")
st.markdown("<br>", unsafe_allow_html=True)

# Grid Layout: 2 kolom
cols = st.columns(2)
for i, app in enumerate(daftar_dashboard):
    with cols[i % 2]:
        html_card = f"""
        <a href="{app['url']}" target="_blank" class="dashboard-card">
            <div class="card-title">{app['title']}</div>
            <div class="card-desc">{app['desc']}</div>
        </a>
        """
        st.markdown(html_card, unsafe_allow_html=True)


# --- FOOTER ---
st.markdown(
    """
    <div class="footer-container">
        <div class="tagline-box">
            <p class="footer-text">
                <span class="tagline-title">💡 Semua Bisa Dihitung</span><br>
                by Alif Towew
            </p>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)
