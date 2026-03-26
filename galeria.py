
import streamlit as st
import requests
import time

# ── Page config ───────────────────────────────────────────
st.set_page_config(
    page_title="Аниме Галерия",
    page_icon="🌸",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Raleway:wght@300;400;600;700&display=swap');

/* Background */
.stApp {
    background: #0a0a12;
    color: #f0eaff;
}
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 40% at 20% 10%, rgba(123,94,167,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 80% 80%, rgba(224,64,160,0.13) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; }

/* Global text */
body, .stApp, p, label, div {
    font-family: 'Raleway', sans-serif !important;
    color: #f0eaff;
}

/* Header */
.anime-header {
    text-align: center;
    padding: 30px 0 10px;
}
.anime-header .label {
    font-size: 11px;
    letter-spacing: 6px;
    text-transform: uppercase;
    color: #00d4ff;
    margin-bottom: 10px;
    font-weight: 300;
}
.anime-header h1 {
    font-family: 'Cinzel Decorative', serif !important;
    font-size: clamp(28px, 4vw, 52px);
    background: linear-gradient(135deg, #e040a0, #7b5ea7, #00d4ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 30px rgba(224,64,160,0.4));
    margin: 0;
}
.anime-header .sub {
    color: #888aaa;
    font-size: 13px;
    letter-spacing: 3px;
    font-weight: 300;
    margin-top: 6px;
}
.header-line {
    width: 120px;
    height: 1px;
    background: linear-gradient(90deg, transparent, #e040a0, transparent);
    margin: 16px auto;
}

/* Tabs override */
.stTabs [data-baseweb="tab-list"] {
    background: #12121e !important;
    border: 1px solid #2a2a45 !important;
    border-radius: 16px !important;
    padding: 5px !important;
    gap: 4px !important;
    justify-content: center;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #888aaa !important;
    border-radius: 12px !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    border: none !important;
    padding: 10px 28px !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #e040a0, #7b5ea7) !important;
    color: white !important;
    box-shadow: 0 0 24px rgba(224,64,160,0.35) !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none !important; }
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* Search input */
.stTextInput > div > div > input {
    background: #181828 !important;
    border: 1px solid #2a2a45 !important;
    border-radius: 12px !important;
    color: #f0eaff !important;
    font-family: 'Raleway', sans-serif !important;
    padding: 12px 18px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #e040a0 !important;
    box-shadow: 0 0 0 3px rgba(224,64,160,0.15) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #e040a0, #7b5ea7) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    padding: 10px 24px !important;
    transition: all 0.25s !important;
    box-shadow: 0 0 24px rgba(224,64,160,0.35) !important;
    width: 100%;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 32px rgba(224,64,160,0.5) !important;
}

/* Anime card */
.anime-card {
    background: #181828;
    border: 1px solid #2a2a45;
    border-radius: 18px;
    overflow: hidden;
    transition: all 0.3s;
    margin-bottom: 20px;
    position: relative;
}
.anime-card:hover {
    border-color: #e040a0;
    box-shadow: 0 0 24px rgba(224,64,160,0.35), 0 20px 60px rgba(0,0,0,0.5);
    transform: translateY(-4px);
}
.anime-card img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    display: block;
}
.anime-card-body {
    padding: 14px 16px 16px;
}
.anime-card-title {
    font-size: 14px;
    font-weight: 700;
    color: #f0eaff;
    margin-bottom: 8px;
    line-height: 1.3;
}
.anime-card-meta {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    margin-bottom: 8px;
}
.tag {
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 6px;
    font-weight: 600;
}
.tag-score { background: rgba(255,215,0,0.15); color: #ffd700; }
.tag-genre { background: rgba(123,94,167,0.2); color: #b89ee0; }
.tag-eps   { background: rgba(0,212,255,0.12); color: #00d4ff; }
.anime-desc {
    font-size: 11px;
    color: #888aaa;
    line-height: 1.6;
    margin-top: 6px;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Search result card */
.search-card {
    background: #181828;
    border: 1px solid #2a2a45;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 16px;
    transition: border-color 0.3s;
}
.search-card:hover { border-color: #e040a0; }
.search-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}
.search-card-body { padding: 10px 12px 12px; }
.search-card-title {
    font-size: 12px;
    font-weight: 700;
    color: #f0eaff;
    margin-bottom: 4px;
    line-height: 1.3;
}
.search-card-score { font-size: 11px; color: #ffd700; margin-bottom: 6px; }
.search-card-desc {
    font-size: 10px;
    color: #888aaa;
    line-height: 1.5;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-bottom: 8px;
}

/* Section title */
.section-title {
    font-family: 'Cinzel Decorative', serif !important;
    font-size: 15px;
    background: linear-gradient(135deg, #e040a0, #00d4ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 6px;
}
.count-badge {
    display: inline-block;
    background: linear-gradient(135deg, #e040a0, #7b5ea7);
    color: white;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* Selectbox */
.stSelectbox > div > div {
    background: #181828 !important;
    border: 1px solid #2a2a45 !important;
    border-radius: 12px !important;
    color: #f0eaff !important;
}

/* Success / warning */
.stSuccess, .stWarning, .stInfo {
    border-radius: 12px !important;
    font-family: 'Raleway', sans-serif !important;
}

/* Divider */
hr { border-color: #2a2a45 !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0a12; }
::-webkit-scrollbar-thumb { background: #7b5ea7; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ── Jikan API helpers ─────────────────────────────────────
JIKAN = "https://api.jikan.moe/v4"

@st.cache_data(show_spinner=False)
def fetch_anime_by_id(mal_id: int):
    try:
        r = requests.get(f"{JIKAN}/anime/{mal_id}", timeout=10)
        if r.status_code == 200:
            return r.json().get("data")
    except Exception:
        pass
    return None

@st.cache_data(show_spinner=False)
def search_jikan(query: str):
    try:
        r = requests.get(f"{JIKAN}/anime", params={"q": query, "limit": 12, "sfw": True}, timeout=10)
        if r.status_code == 200:
            return r.json().get("data", [])
    except Exception:
        pass
    return []

def get_img(anime):
    return (anime.get("images", {}).get("jpg", {}).get("large_image_url")
            or anime.get("images", {}).get("jpg", {}).get("image_url", ""))

def get_score(anime):
    s = anime.get("score")
    return f"⭐ {s}" if s else ""

def get_genre(anime):
    g = anime.get("genres", [])
    return g[0]["name"] if g else ""

def get_eps(anime):
    e = anime.get("episodes")
    return f"{e} еп." if e else ""

def get_desc(anime, max_chars=200):
    s = anime.get("synopsis", "") or ""
    return s[:max_chars] + ("..." if len(s) > max_chars else "")

# ── Session state ─────────────────────────────────────────
PRELOAD_IDS = [16498, 1535, 11061, 38000, 1, 20]

if "collection" not in st.session_state:
    st.session_state.collection = []
    st.session_state.loaded = False

if not st.session_state.loaded:
    with st.spinner("🌸 Зарежда аниме..."):
        for i, mid in enumerate(PRELOAD_IDS):
            anime = fetch_anime_by_id(mid)
            if anime:
                st.session_state.collection.append(anime)
            if i < len(PRELOAD_IDS) - 1:
                time.sleep(0.35)
    st.session_state.loaded = True

# ── Header ────────────────────────────────────────────────
st.markdown("""
<div class="anime-header">
  <div class="label">✦ моята колекция ✦</div>
  <h1>Аниме Галерия</h1>
  <div class="sub">アニメ・ギャラリー</div>
  <div class="header-line"></div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────
tab_gallery, tab_search = st.tabs(["🎌  Галерия", "🔍  Търсене"])

# ════════════════════════════════════════════════════════════
# GALLERY TAB
# ════════════════════════════════════════════════════════════
with tab_gallery:
    col_left, col_right = st.columns([3, 1])
    with col_left:
        st.markdown('<div class="section-title">Моята Колекция</div>', unsafe_allow_html=True)
    with col_right:
        n = len(st.session_state.collection)
        st.markdown(f'<div class="count-badge" style="float:right">{n} аниме</div>', unsafe_allow_html=True)

    if not st.session_state.collection:
        st.info("🌸 Галерията е празна. Намери аниме чрез търсене!")
    else:
        # Remove widget
        names = [a["title"] for a in st.session_state.collection]
        rem_col1, rem_col2 = st.columns([3, 1])
        with rem_col1:
            remove_name = st.selectbox("Избери аниме за премахване", names, label_visibility="collapsed")
        with rem_col2:
            if st.button("✕ Премахни"):
                st.session_state.collection = [
                    a for a in st.session_state.collection if a["title"] != remove_name
                ]
                st.success(f"✕ {remove_name} е премахнато!")
                st.rerun()

        st.markdown("<hr>", unsafe_allow_html=True)

        # Gallery grid — 3 columns
        cols = st.columns(3)
        for idx, anime in enumerate(st.session_state.collection):
            img   = get_img(anime)
            score = get_score(anime)
            genre = get_genre(anime)
            eps   = get_eps(anime)
            desc  = get_desc(anime)
            tags  = ""
            if score: tags += f'<span class="tag tag-score">{score}</span>'
            if genre: tags += f'<span class="tag tag-genre">{genre}</span>'
            if eps:   tags += f'<span class="tag tag-eps">{eps}</span>'

            with cols[idx % 3]:
                st.markdown(f"""
                <div class="anime-card">
                    <img src="{img}" alt="{anime['title']}">
                    <div class="anime-card-body">
                        <div class="anime-card-title">{anime['title']}</div>
                        <div class="anime-card-meta">{tags}</div>
                        <div class="anime-desc">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# SEARCH TAB
# ════════════════════════════════════════════════════════════
with tab_search:
    st.markdown('<div class="section-title">🔍 Търси Аниме</div>', unsafe_allow_html=True)

    s_col1, s_col2 = st.columns([4, 1])
    with s_col1:
        query = st.text_input("Търси", placeholder="напр. Naruto, One Piece, Bleach...", label_visibility="collapsed")
    with s_col2:
        search_btn = st.button("🔍 Търси")

    if search_btn and query:
        with st.spinner("Търся..."):
            results = search_jikan(query)

        if not results:
            st.warning("Няма резултати. Опитай друго търсене.")
        else:
            st.markdown(f"**{len(results)} резултата за** *{query}*")
            st.markdown("<hr>", unsafe_allow_html=True)

            res_cols = st.columns(4)
            for i, anime in enumerate(results):
                img   = get_img(anime)
                score = get_score(anime) or "N/A"
                desc  = get_desc(anime, 120)
                in_col = any(a["mal_id"] == anime["mal_id"] for a in st.session_state.collection)

                with res_cols[i % 4]:
                    st.markdown(f"""
                    <div class="search-card">
                        <img src="{img}" alt="{anime['title']}">
                        <div class="search-card-body">
                            <div class="search-card-title">{anime['title']}</div>
                            <div class="search-card-score">{score}</div>
                            <div class="search-card-desc">{desc}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    if in_col:
                        st.success("✓ В колекцията")
                    else:
                        if st.button(f"+ Добави", key=f"add_{anime['mal_id']}"):
                            st.session_state.collection.insert(0, anime)
                            st.success(f"🌸 {anime['title']} добавено!")
                            st.rerun()
