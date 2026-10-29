
import streamlit as st
import requests
import html
from gtts import gTTS
from io import BytesIO
from datetime import datetime

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Lingua | Language Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. LANGUAGES

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Japanese": "ja"
}

# 3. SESSION STATE

defaults = {
    "source": "English",
    "target": "Hindi",
    "input_text": "",
    "translated_text": "",
    "history": [],
    "audio": None,
    "theme_toggle": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def swap_languages():
    old_source = st.session_state.source
    old_target = st.session_state.target

    st.session_state.source = old_target
    st.session_state.target = old_source

    if st.session_state.translated_text:
        st.session_state.input_text = (
            st.session_state.translated_text
        )

    st.session_state.translated_text = ""
    st.session_state.audio = None


def load_sample():
    st.session_state.input_text = (
        "Hello! How are you today? "
        "Welcome to my language translator."
    )
    st.session_state.translated_text = ""
    st.session_state.audio = None


def clear_text():
    st.session_state.input_text = ""
    st.session_state.translated_text = ""
    st.session_state.audio = None

# 4. LIGHT AND DARK THEME

if st.session_state.theme_toggle:
    bg = "#0b1120"
    panel = "#151e30"
    foreground = "#f1f5f9"
    muted = "#aab8ce"
    field = "#101827"
    border = "#334155"
else:
    bg = "#f5f7ff"
    panel = "#ffffff"
    foreground = "#172033"
    muted = "#596780"
    field = "#ffffff"
    border = "#d7deec"

st.markdown(
    f"""
    <style>
    /* Main page */
    .stApp {{
        background: {bg} !important;
        color: {foreground} !important;
    }}

    [data-testid="stHeader"] {{
        background: {bg} !important;
    }}

    .block-container {{
        max-width: 100% !important;
        padding: 1.5rem clamp(1rem, 4vw, 4rem) 3rem !important;
    }}

    /* General text */
    .stApp p,
    .stApp label,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp [data-testid="stMarkdownContainer"] {{
        color: {foreground};
    }}

    .stApp [data-testid="stCaptionContainer"] {{
        color: {muted} !important;
    }}

    /* Input fields */
    .stApp textarea,
    .stApp input {{
        background-color: {field} !important;
        color: {foreground} !important;
        -webkit-text-fill-color: {foreground} !important;
        border-color: {border} !important;
        caret-color: {foreground} !important;
    }}

    .stApp textarea::placeholder,
    .stApp input::placeholder {{
        color: {muted} !important;
        -webkit-text-fill-color: {muted} !important;
    }}

    /* Dropdowns */
    .stApp [data-baseweb="select"] > div {{
        background-color: {field} !important;
        border-color: {border} !important;
    }}

    .stApp [data-baseweb="select"] * {{
        color: {foreground} !important;
    }}

    [data-baseweb="popover"],
    [data-baseweb="menu"] {{
        background-color: {panel} !important;
    }}

    /* Brand banner */
    .lingua-hero {{
        background: linear-gradient(
            120deg, #4338ca, #7c3aed, #a855f7
        );
        padding: clamp(24px, 4vw, 42px);
        border-radius: 24px;
        color: white !important;
        margin-bottom: 22px;
        box-shadow: 0 12px 35px rgba(79, 70, 229, 0.20);
    }}

    .brand-line {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}

    .brand-icon {{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 62px;
        height: 62px;
        flex-shrink: 0;
        border-radius: 19px;
        background: rgba(255, 255, 255, 0.18);
        font-size: 36px;
    }}

    .brand-name {{
        color: white !important;
        font-size: clamp(34px, 4vw, 48px);
        font-weight: 800;
        letter-spacing: -1.5px;
    }}

    .brand-quote {{
        color: white !important;
        font-size: clamp(17px, 2vw, 21px);
        font-weight: 600;
        margin-top: 18px;
        margin-bottom: 7px;
    }}

    .brand-subtitle {{
        color: white !important;
        font-size: 14px;
        opacity: 0.92;
    }}

    /* Translation result */
    .translation-panel {{
        background: {panel};
        color: {foreground} !important;
        border: 1px solid {border};
        border-radius: 18px;
        padding: 22px;
        min-height: 180px;
        overflow-wrap: anywhere;
        white-space: pre-wrap;
        font-size: 17px;
        line-height: 1.8;
    }}

    /* Buttons */
    .stButton > button,
    .stDownloadButton > button {{
        border-radius: 12px !important;
        min-height: 43px;
        font-weight: 600;
    }}

    /* Footer */
    .lingua-footer {{
        text-align: center;
        color: {muted} !important;
        padding: 18px 0;
        font-size: 13px;
    }}

    /* Small screens */
    @media (max-width: 700px) {{
        .block-container {{
            padding: 1rem !important;
        }}

        .lingua-hero {{
            border-radius: 18px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# 5. HEADER AND THEME SWITCH

header_col, theme_col = st.columns([5, 1])

with header_col:
    st.markdown(
        """
        <div class="lingua-hero">
            <div class="brand-line">
                <div class="brand-icon">🌐</div>
                <div class="brand-name">Lingua</div>
            </div>
            <div class="brand-quote">
                “Every language opens a new world.”
            </div>
            <div class="brand-subtitle">
                Translate naturally · Listen effortlessly ·
                Connect globally
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with theme_col:
    st.write("")
    st.write("")
    st.toggle(
        "🌙 Dark mode",
        key="theme_toggle"
    )

st.caption("✨ Your personal multilingual translation assistant")


# 6. LANGUAGE SELECTION

st.markdown("### 🌍 Choose your languages")

source_col, swap_col, target_col = st.columns([5, 1, 5])

with source_col:
    st.selectbox(
        "Translate from",
        options=list(LANGUAGES.keys()),
        key="source"
    )

with swap_col:
    st.write("")
    st.write("")
    st.button(
        "⇄ Swap",
        on_click=swap_languages,
        use_container_width=True
    )

with target_col:
    st.selectbox(
        "Translate to",
        options=list(LANGUAGES.keys()),
        key="target"
    )


# 7. INPUT AND OUTPUT PANELS

st.write("")

input_col, output_col = st.columns(2, gap="large")

with input_col:
    st.markdown("### 📝 Your text")

    st.text_area(
        "Enter text to translate",
        key="input_text",
        height=220,
        max_chars=450,
        placeholder="Type or paste your text here..."
    )

    char_count = len(st.session_state.input_text)
    st.caption(f"✍️ {char_count}/450 characters")

    sample_col, clear_col = st.columns(2)

    with sample_col:
        st.button(
            "✨ Try sample",
            on_click=load_sample,
            use_container_width=True
        )

    with clear_col:
        st.button(
            "🗑️ Clear",
            on_click=clear_text,
            use_container_width=True
        )

    translate_clicked = st.button(
        "🌍 Translate now",
        type="primary",
        use_container_width=True
    )

    if translate_clicked:
        text_to_translate = st.session_state.input_text.strip()
        source = st.session_state.source
        target = st.session_state.target

        if not text_to_translate:
            st.warning("Please enter some text first.")

        elif source == target:
            st.session_state.translated_text = text_to_translate
            st.session_state.audio = None

            st.session_state.history.insert(0, {
                "source": source,
                "target": target,
                "original": text_to_translate,
                "translation": text_to_translate,
                "time": datetime.now().strftime("%H:%M")
            })
            st.session_state.history = st.session_state.history[:10]

        else:
            try:
                with st.spinner("Translating your text..."):
                    response = requests.get(
                        "https://api.mymemory.translated.net/get",
                        params={
                            "q": text_to_translate,
                            "langpair": (
                                f"{LANGUAGES[source]}|{LANGUAGES[target]}"
                            )
                        },
                        timeout=20
                    )

                    response.raise_for_status()
                    data = response.json()

                    if data.get("responseStatus") != 200:
                        st.error(
                            data.get(
                                "responseDetails",
                                "The translation service returned an error."
                            )
                        )
                    else:
                        result = data.get(
                            "responseData", {}
                        ).get("translatedText", "").strip()

                        if not result:
                            st.error("No translation was returned.")
                        else:
                            st.session_state.translated_text = result
                            st.session_state.audio = None

                            st.session_state.history.insert(0, {
                                "source": source,
                                "target": target,
                                "original": text_to_translate,
                                "translation": result,
                                "time": datetime.now().strftime("%H:%M")
                            })

                            st.session_state.history = (
                                st.session_state.history[:10]
                            )

            except requests.RequestException:
                st.error(
                    "Unable to connect to the translation service. "
                    "Please check your internet connection and try again."
                )

            except (ValueError, KeyError):
                st.error(
                    "The translation service returned an unexpected response."
                )

with output_col:
    st.markdown("### 💬 Your translation")

    result = st.session_state.translated_text

    if result:
        st.markdown(
            f'<div class="translation-panel">{html.escape(result)}</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.caption("📋 Copy the translated text using the copy control below.")
        st.code(result, language=None)

        audio_col, download_col = st.columns(2)

        with audio_col:
            if st.button(
                "🔊 Generate speech",
                use_container_width=True
            ):
                try:
                    with st.spinner("Preparing your audio..."):
                        audio_buffer = BytesIO()

                        speech = gTTS(
                            text=result,
                            lang=LANGUAGES[st.session_state.target]
                        )

                        speech.write_to_fp(audio_buffer)
                        st.session_state.audio = audio_buffer.getvalue()

                except Exception:
                    st.error(
                        "Unable to generate speech. "
                        "Check your internet connection and language support."
                    )

        with download_col:
            st.download_button(
                "📄 Download text",
                data=result,
                file_name="lingua_translation.txt",
                mime="text/plain",
                use_container_width=True
            )

        if st.session_state.audio:
            st.markdown("#### 🎧 Listen to your translation")
            st.audio(
                st.session_state.audio,
                format="audio/mp3"
            )

            st.download_button(
                "⬇️ Download MP3 audio",
                data=st.session_state.audio,
                file_name="lingua_speech.mp3",
                mime="audio/mpeg",
                use_container_width=True
            )

    else:
        st.markdown(
            """
            <div class="translation-panel">
                <strong>✨ Your translation will appear here.</strong>
                <br><br>
                Choose your languages, enter your text, and press
                <strong>Translate now</strong> to get started.
                <br><br>
                🔊 You can also listen to the translation.
            </div>
            """,
            unsafe_allow_html=True
        )

# 8. RECENT TRANSLATIONS

st.divider()
st.markdown("## 🕘 Recent translations")
st.caption("Your latest 10 translations in this session.")

if st.session_state.history:
    for index, item in enumerate(st.session_state.history):
        with st.expander(
            f"{item['source']} → {item['target']}  |  {item['time']}"
        ):
            st.markdown("**Original text**")
            st.write(item["original"])

            st.markdown("**Translated text**")
            st.write(item["translation"])

            st.download_button(
                "⬇️ Download this translation",
                data=item["translation"],
                file_name=f"translation_{index + 1}.txt",
                mime="text/plain",
                key=f"history_download_{index}"
            )

            if st.button(
                "↩️ Use this translation",
                key=f"history_use_{index}"
            ):
                st.session_state.input_text = item["original"]
                st.session_state.source = item["source"]
                st.session_state.target = item["target"]
                st.session_state.translated_text = item["translation"]
                st.session_state.audio = None
                st.rerun()

    if st.button("🧹 Clear history"):
        st.session_state.history = []
        st.rerun()
else:
    st.info(
        "Your translations will appear here after you translate some text."
    )

# 9. FOOTER

st.markdown(
    """
    <div class="lingua-footer">
        🌐 Lingua — Every language opens a new world.<br>
        Built with Python · Streamlit · MyMemory API · gTTS
    </div>
    """,
    unsafe_allow_html=True
)
