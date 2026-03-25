import streamlit as st
import json
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Katalog Dashboard Analisis", layout="wide")

DATA_FILE = "dashboards.json"

# --- DATA DEFAULT (Tanpa Emoji) ---
default_data = [
    {
        "id": 1,
        "title": "Sensitivitas Minyak Indonesia",
        "desc": "Kalkulasi dampak fiskal dari perubahan harga minyak dan nilai tukar",
        "url": "https://harga-minyak-dunia.streamlit.app/",
        "color_class": "bg-navy"
    },
    {
        "id": 2,
        "title": "Simulasi Swasembada Energi",
        "desc": "Simulasi dampak ekonomi dan energi dari elektrifikasi kendaraan",
        "url": "https://huggingface.co/spaces/aliftowew/swasembada-energi-simulasi",
        "color_class": "bg-teal"
    },
    {
        "id": 3,
        "title": "Dampak Ekonomi Jalan Jawa Barat",
        "desc": "Kalkulasi dampak ekonomi dari proyek infrastruktur jalan di Jawa Barat",
        "url": "https://huggingface.co/spaces/aliftowew/dashboard-dampak-ekonomi-jalan-jabar",
        "color_class": "bg-slate"
    },
    {
        "id": 4,
        "title": "Dashboard Dampak Ekonomi KDKMP",
        "desc": "Analisis dan proyeksi dampak ekonomi KDKMP",
        "url": "https://huggingface.co/spaces/aliftowew/Dashboard-Dampak-Ekonomi-KDKMP",
        "color_class": "bg-maroon"
    },
    {
        "id": 5,
        "title": "Prediksi Pangan Indonesia",
        "desc": "Sistem prediksi fluktuasi harga pangan nasional",
        "url": "https://huggingface.co/spaces/aliftowew/prediksi-pangan-indonesia",
        "color_class": "bg-forest"
    },
    {
        "id": 6,
        "title": "Kalkulator Kebijakan WFH",
        "desc": "Dashboard kalkulasi dan analisis efisiensi kebijakan WFH",
        "url": "https://kalkulator-kebijakan-wfh.streamlit.app/",
        "color_class": "bg-charcoal"
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

# --- CSS KUSTOM PROFESIONAL ---
st.markdown("""
<style>
    .dashboard-card {
        border-radius: 6px;
        padding: 24px;
        margin-bottom: 20px;
        text-decoration: none;
        display: block;
        transition: all 0.2s ease-in-out;
        height: 140px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .dashboard-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        text-decoration: none;
    }
    .card-title { 
        font-size: 1.15rem; 
        font-weight: 600; 
        margin-bottom: 10px;
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .card-desc { 
        font-size: 0.9rem; 
        color: #f1f5f9 !important;
        line-height: 1.4;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Palet Warna Solid Profesional */
    .bg-navy { background-color: #1e3a8a; }
    .bg-teal { background-color: #0f766e; }
    .bg-slate { background-color: #475569; }
    .bg-maroon { background-color: #831843; }
    .bg-forest { background-color: #166534; }
    .bg-charcoal { background-color: #334155; }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
        color: #64748b;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)


# --- TAMPILAN UTAMA ---
st.markdown("## Katalog Sistem Analisis & Simulasi Data")
st.markdown("Pusat integrasi dashboard untuk perhitungan ekonomi, energi, dan kebijakan strategis.")
st.markdown("<br>", unsafe_allow_html=True)

# Grid Layout
cols = st.columns(2)
for i, app in enumerate(st.session_state.dashboards):
    with cols[i % 2]:
        html_card = f"""
        <a href="{app['url']}" target="_blank" class="dashboard-card {app['color_class']}">
            <div class="card-title">{app['title']}</div>
            <div class="card-desc">{app['desc']}</div>
        </a>
        """
        st.markdown(html_card, unsafe_allow_html=True)


# --- FOOTER ---
st.markdown(
    """
    <div class="footer">
        💡 <strong>Semua Bisa Dihitung</strong><br>
        by Alif Towew
    </div>
    """, 
    unsafe_allow_html=True
)


# --- SIDEBAR MANAJEMEN ---
st.sidebar.markdown("### Manajemen Dashboard")

with st.sidebar.expander("Tambah Dashboard Baru"):
    with st.form("add_form"):
        new_title = st.text_input("Judul Dashboard")
        new_desc = st.text_area("Deskripsi Singkat")
        new_url = st.text_input("URL Link")
        new_color = st.selectbox("Pilih Warna Label", ["bg-navy", "bg-teal", "bg-slate", "bg-maroon", "bg-forest", "bg-charcoal"])
        
        if st.form_submit_button("Simpan Data"):
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
                st.success("Data berhasil ditambahkan.")
                st.rerun()
            else:
                st.error("Judul dan URL wajib diisi.")

with st.sidebar.expander("Hapus Dashboard"):
    app_to_delete = st.selectbox("Pilih data yang akan dihapus", [app['title'] for app in st.session_state.dashboards])
    if st.button("Hapus Data"):
        st.session_state.dashboards = [app for app in st.session_state.dashboards if app['title'] != app_to_delete]
        save_data(st.session_state.dashboards)
        st.success(f"'{app_to_delete}' telah dihapus dari sistem.")
        st.rerun()
