import streamlit as st
import json
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Hub Dashboard Alif", page_icon="🚀", layout="wide")

DATA_FILE = "dashboards.json"

# --- DATA DEFAULT ---
# Data awal berdasarkan dashboard yang sudah kamu buat
default_data = [
    {
        "id": 1,
        "title": "Sensitivitas Minyak Indonesia 🥚",
        "desc": "Calculate fiscal impact of oil price and exchange rate changes",
        "url": "https://harga-minyak-dunia.streamlit.app/",
        "color_class": "bg-pink-purple"
    },
    {
        "id": 2,
        "title": "Swasembada Energi Simulasi ⚡",
        "desc": "Simulate energy & economic impacts of vehicle electrification",
        "url": "https://huggingface.co/spaces/aliftowew/swasembada-energi-simulasi",
        "color_class": "bg-blue-green"
    },
    {
        "id": 3,
        "title": "Dashboard Dampak Ekonomi Jalan Jabar 😸",
        "desc": "Calculate economic impact of West Java road projects",
        "url": "https://huggingface.co/spaces/aliftowew/dashboard-dampak-ekonomi-jalan-jabar",
        "color_class": "bg-purple"
    },
    {
        "id": 4,
        "title": "Dashboard Dampak Ekonomi KDKMP 🚀",
        "desc": "Dampak Ekonomi KDKMP",
        "url": "https://huggingface.co/spaces/aliftowew/Dashboard-Dampak-Ekonomi-KDKMP",
        "color_class": "bg-red"
    },
    {
        "id": 5,
        "title": "Prediksi Pangan Indonesia 👀",
        "desc": "Memprediksi harga pangan Indonesia",
        "url": "https://huggingface.co/spaces/aliftowew/prediksi-pangan-indonesia",
        "color_class": "bg-orange"
    },
    {
        "id": 6,
        "title": "Kalkulator Kebijakan WFH 🪨",
        "desc": "Dashboard kalkulasi kebijakan WFH",
        "url": "https://kalkulator-kebijakan-wfh.streamlit.app/",
        "color_class": "bg-dark"
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

# Load data ke session_state agar reaktif
if 'dashboards' not in st.session_state:
    st.session_state.dashboards = load_data()

# --- CSS KUSTOM UNTUK CARDS ---
st.markdown("""
<style>
    .dashboard-card {
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        color: white;
        text-decoration: none;
        display: block;
        transition: transform 0.2s;
        height: 150px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .dashboard-card:hover {
        transform: scale(1.02);
        color: white;
        text-decoration: none;
    }
    .card-title { font-size: 1.2rem; font-weight: bold; margin-bottom: 8px; }
    .card-desc { font-size: 0.9rem; opacity: 0.9; }
    
    /* Gradien warna mirip gambar */
    .bg-dark { background: linear-gradient(135deg, #51556b, #403e5c); }
    .bg-pink-purple { background: linear-gradient(135deg, #c74c6e, #714ab0); }
    .bg-purple { background: linear-gradient(135deg, #714ab0, #a04791); }
    .bg-red { background: linear-gradient(135deg, #c42d2d, #a32222); }
    .bg-orange { background: linear-gradient(135deg, #d4801e, #b36612); }
    .bg-blue-green { background: linear-gradient(135deg, #3782a6, #2d9472); }
</style>
""", unsafe_allow_html=True)


# --- TAMPILAN UTAMA ---
st.title("Koleksi Dashboard & Aplikasi")
st.write("Kumpulan platform simulasi, perhitungan ekonomi, dan prediksi.")

# Menampilkan cards dalam grid
cols = st.columns(2) # Bagi menjadi 2 kolom
for i, app in enumerate(st.session_state.dashboards):
    with cols[i % 2]:
        # Membuat HTML card yang bisa diklik
        html_card = f"""
        <a href="{app['url']}" target="_blank" class="dashboard-card {app['color_class']}">
            <div class="card-title">{app['title']}</div>
            <div class="card-desc">{app['desc']}</div>
        </a>
        """
        st.markdown(html_card, unsafe_allow_html=True)


# --- SIDEBAR: TAMBAH / EDIT DATA ---
st.sidebar.header("⚙️ Kelola Dashboard")

with st.sidebar.expander("➕ Tambah Dashboard Baru"):
    with st.form("add_form"):
        new_title = st.text_input("Judul Dashboard")
        new_desc = st.text_area("Deskripsi Singkat")
        new_url = st.text_input("URL Link")
        new_color = st.selectbox("Pilih Warna", ["bg-dark", "bg-pink-purple", "bg-purple", "bg-red", "bg-orange", "bg-blue-green"])
        
        if st.form_submit_button("Simpan Baru"):
            if new_title and new_url:
                new_id = max([d['id'] for d in st.session_state.dashboards] + [0]) + 1
                new_app = {
                    "id": new_id,
                    "title": new_title,
                    "desc": new_desc,
                    "url": new_url,
                    "color_class": new_color
                }
                st.session_state.dashboards.append(new_app)
                save_data(st.session_state.dashboards)
                st.success("Berhasil ditambahkan!")
                st.rerun()
            else:
                st.error("Judul dan URL wajib diisi.")

with st.sidebar.expander("✏️ Hapus Dashboard"):
    app_to_delete = st.selectbox("Pilih yang ingin dihapus", [app['title'] for app in st.session_state.dashboards])
    if st.button("Hapus"):
        st.session_state.dashboards = [app for app in st.session_state.dashboards if app['title'] != app_to_delete]
        save_data(st.session_state.dashboards)
        st.success(f"{app_to_delete} berhasil dihapus!")
        st.rerun()
