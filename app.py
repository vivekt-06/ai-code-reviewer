import streamlit as st
from reviewer import review_code

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🔍",
    layout="wide",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    code, pre, .stTextArea textarea { font-family: 'JetBrains Mono', monospace !important; }

    .main { background: #0d1117; }
    .stApp { background: #0d1117; color: #e6edf3; }

    .header-box {
        background: linear-gradient(135deg, #161b22 0%, #1f2937 100%);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 28px 32px;
        margin-bottom: 24px;
    }
    .header-box h1 { font-size: 2rem; font-weight: 700; color: #58a6ff; margin: 0; }
    .header-box p  { color: #8b949e; margin: 6px 0 0; font-size: 0.95rem; }

    .review-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px 24px;
        margin-bottom: 16px;
    }

    .score-ring {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        line-height: 1;
    }

    .score-label {
        font-size: 0.8rem;
        color: #8b949e;
        text-align: center;
        margin-top: 4px;
    }

    .stTextArea textarea {
        background: #0d1117 !important;
        border: 1px solid #30363d !important;
        color: #e6edf3 !important;
        border-radius: 8px !important;
        font-size: 0.88rem !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #238636, #2ea043) !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 28px !important;
        font-weight: 600 !important;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-box">
    <h1>🔍 AI Code Reviewer</h1>
    <p>Paste your code and get instant feedback — bugs, performance, security, and improvements.</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Settings")

    language = st.selectbox("Language", [
        "Python", "JavaScript", "Java", "C++", "C", "Go", "Rust", "Other"
    ])

    review_depth = st.select_slider(
        "Review Depth",
        options=["Quick", "Standard", "Deep"],
        value="Standard"
    )

    st.markdown("### 🎯 Focus Areas")
    check_bugs = st.checkbox("🐛 Bugs", True)
    check_perf = st.checkbox("⚡ Performance", True)
    check_style = st.checkbox("🎨 Style", True)
    check_security = st.checkbox("🔒 Security", True)
    check_refactor = st.checkbox("♻️ Refactor Code", True)

    focus_areas = []
    if check_bugs: focus_areas.append("bugs")
    if check_perf: focus_areas.append("performance")
    if check_style: focus_areas.append("style")
    if check_security: focus_areas.append("security")

# ── Layout ─────────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Your Code")
    code_input = st.text_area("Paste code here", height=400)

    submitted = st.button("🚀 Review Code")

with col2:
    st.subheader("📊 Results")

    if submitted:
        if not code_input.strip():
            st.warning("Paste some code first.")
        else:
            with st.spinner("Analyzing..."):
                result = review_code(
                    code=code_input,
                    language=language,
                    focus_areas=focus_areas,
                    depth=review_depth,
                    include_refactor=check_refactor
                )

            if "error" in result:
                st.error(result["error"])
            else:
                score = result.get("score", 0)

                st.markdown(f"### ⭐ Score: {score}/100")
                st.write(result.get("summary", ""))

                if result.get("bugs"):
                    st.subheader("🐛 Bugs")
                    for item in result["bugs"]:
                        st.write(f"- {item}")

                if result.get("performance"):
                    st.subheader("⚡ Performance")
                    for item in result["performance"]:
                        st.write(f"- {item}")

                if result.get("style"):
                    st.subheader("🎨 Style")
                    for item in result["style"]:
                        st.write(f"- {item}")

                if result.get("security"):
                    st.subheader("🔒 Security")
                    for item in result["security"]:
                        st.write(f"- {item}")

                if check_refactor and result.get("refactored_code"):
                    st.subheader("♻️ Refactored Code")
                    st.code(result["refactored_code"])

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Minor Project — AI Code Reviewer")