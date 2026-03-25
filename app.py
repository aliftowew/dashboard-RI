import streamlit as st
import json
import os
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Katalog Sistem Analisis & Simulasi Data", layout="wide")

DATA_FILE = "dashboards.json"

# --- DATA DEFAULT (Sangat Formal & Tanpa Ikon di Judul) ---
default_data = [
    {
        "id": 1,
        "title": "Sensitivitas Minyak Indonesia",
        "desc": "Calculate fiscal impact of oil price and exchange rate changes",
        "url": "https://harga-minyak-dunia.streamlit.app/"
    },
    {
        "id": 2,
        "title": "Swasembada Energi Simulasi",
        "desc": "Simulate energy & economic impacts of vehicle electrification",
        "url": "https://huggingface.co/spaces/aliftowew/swasembada-energi-simulasi"
    },
    {
        "id": 3,
        "title": "Dashboard Dampak Ekonomi Jalan Jabar",
        "desc": "Calculate economic impact of West Java road projects",
        "url": "https://huggingface.co/spaces/aliftowew/dashboard-dampak-ekonomi-jalan-jabar"
    },
    {
        "id": 4,
        "title": "Dashboard Dampak Ekonomi KDKMP",
        "desc": "Dampak Ekonomi KDKMP",
        "url": "https://huggingface.co/spaces/aliftowew/Dashboard-Dampak-Ekonomi-KDKMP"
    },
    {
        "id": 5,
        "title": "Prediksi Pangan Indonesia",
        "desc": "Memprediksi harga pangan Indonesia",
        "url": "https://huggingface.co/spaces/aliftowew/prediksi-pangan-indonesia"
    },
    {
        "id": 6,
        "title": "Kalkulator Kebijakan WFH",
        "desc": "Dashboard kalkulasi kebijakan WFH",
        "url": "https://kalkulator-kebijakan-wfh.streamlit.app/"
    }
]

# --- FUNGSI MANAJEMEN DATA ---
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump(default_data, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

if 'dashboards' not in st.session_state:
    st.session_state.dashboards = load_data()

# --- FUNGSI UNTUK MEMUAT GAMBAR RUMUS KE BASE64 ---
def get_base64_of_image_file(png_file):
    if not os.path.exists(png_file):
        # Jika file tidak ada (misalnya di GitHub tapi belum di-upload),
        # kembalikan string kosong agar CSS tidak rusak
        return ""
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Asumsikan file gambar image_5.png berada di direktori yang sama dengan app.py
# Pastikan Anda meng-upload image_5.png ke repositori GitHub Anda!
img_rumus_b64 = get_base64_of_image_file("image_5.png")

# --- CSS KUSTOM PROFESIONAL (Minimalis, Teks Hitam, Footer Rumus) ---
st.markdown(f"""
<style>
    /* Styling untuk kotak aplikasi (card) - Putih bersih */
    .dashboard-card {{
        border-radius: 6px;
        padding: 24px;
        margin-bottom: 20px;
        color: black;
        text-decoration: none;
        display: block;
        transition: all 0.2s;
        height: 140px;
        background-color: white; /* Card tetap putih bersih */
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    .dashboard-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-decoration: none;
        color: black;
    }}
    .card-title {{ font-size: 1.15rem; font-weight: bold; margin-bottom: 10px; color: black !important; }}
    .card-desc {{ font-size: 0.9rem; color: #6c757d !important; line-height: 1.4; }}
    
    /* Styling untuk bagian footer dengan latar belakang rumus matematika */
    .footer-container {{
        margin-top: 50px;
        border-top: 1px solid #e2e8f0;
        background-image: url(data:image/png;base64,{img_rumus_b64});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 40px; /* Memberikan ruang agar teks tidak menempel */
        border-radius: 6px; /* Serasi dengan card */
    }}
    .footer {{
        text-align: center;
        color: #333 !important; /* Warna teks lebih gelap agar kontras dengan rumus */
        font-size: 0.95rem;
    }}
    .tagline {{
        font-weight: bold;
    }}
</style>
""", unsafe_allow_html=True)


# --- TAMPILAN UTAMA ---
st.title("Katalog Sistem Analisis & Simulasi Data")
st.markdown("Pusat integrasi dashboard untuk perhitungan ekonomi, energi, dan kebijakan strategis.")
st.markdown("<br>", unsafe_allow_html=True)

# Grid Layout: 2 kolom
cols = st.columns(2)
for i, app in enumerate(st.session_state.dashboards):
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
        <div class="footer">
            <span class="tagline">💡 Semua Bisa Dihitung</span><br>
            by Alif Towew
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)


# --- SIDEBAR: TAMBAH / EDIT DATA (Formal) ---
st.sidebar.markdown("### Manajemen Katalog")

with st.sidebar.expander("Tambah Dashboard Baru"):
    with st.form("add_form"):
        new_title = st.text_input("Judul Dashboard (Tanpa Emoji)")
        new_desc = st.text_area("Deskripsi Singkat")
        new_url = st.text_input("URL Link")
        
        if st.form_submit_button("Simpan Baru"):
            if new_title and new_url:
                new_id = max([d['id'] for d in st.session_state.dashboards] + [0]) + 1
                new_app = {
                    "id": new_id,
                    "title": new_title,
                    "desc": new_desc,
                    "url": new_url
                }
                st.session_state.dashboards.append(new_app)
                save_data(st.session_state.dashboards)
                st.success("Dashboard berhasil ditambahkan.")
                st.rerun()
            else:
                st.error("Judul dan URL wajib diisi.")

with st.sidebar.expander("Hapus Dashboard"):
    app_to_delete = st.selectbox("Pilih yang ingin dihapus", [app['title'] for app in st.session_state.dashboards])
    if st.button("Hapus"):
        st.session_state.dashboards = [app for app in st.session_state.dashboards if app['title'] != app_to_delete]
        save_data(st.session_state.dashboards)
        st.success(f"{app_to_delete} berhasil dihapus.")
        st.rerun()
