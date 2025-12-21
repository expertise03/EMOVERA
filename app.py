import streamlit as st
import altair as alt
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
import joblib
from io import StringIO
from track_utils import (
    create_page_visited_table, add_page_visited_details, view_all_page_visited_details,
    add_prediction_details, view_all_prediction_details, create_emotionclf_table, IST
)

# Load Model
pipe_lr = joblib.load(open("./models/emotion_classifier_pipe_lr.pkl", "rb"))

# Emotion mapping
emotions_emoji_dict = {
    "anger": "😠", "disgust": "🤮", "fear": "😨", "happy": "🤗",
    "joy": "😂", "neutral": "😐", "sad": "😔", "sadness": "😔",
    "shame": "😳", "surprise": "😮"
}

def predict_emotions(docx):
    return pipe_lr.predict([docx])[0]

def get_prediction_proba(docx):
    return pipe_lr.predict_proba([docx])

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Emovera", page_icon="✨", layout="wide")

# ---- GLASSMORPHISM & STYLE ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: radial-gradient(circle at 25% 25%, #0a0b0f 0%, #0d0f1a 100%);
    color: #FAFAFA;
}

/* Glass Sidebar */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 25px rgba(255, 0, 128, 0.2);
    border-radius: 0px 20px 20px 0px;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem;
}

[data-testid="stSidebar"] h2, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
    color: #EEE;
}

/* Sidebar radio buttons */
div[role="radiogroup"] > label {
    background: rgba(255,255,255,0.08);
    margin-bottom: 8px;
    padding: 10px 15px;
    border-radius: 12px;
    transition: 0.3s ease;
    cursor: pointer;
}
div[role="radiogroup"] > label:hover {
    background: rgba(255,255,255,0.15);
    transform: scale(1.02);
}

/* Glowing Title Bar */
.title-container {
    text-align: center;
    margin: 20px auto;
    padding: 20px;
    width: 90%;
    background: linear-gradient(90deg, rgba(121,40,202,0.6), rgba(255,0,128,0.6));
    border-radius: 16px;
    backdrop-filter: blur(12px);
    color: white;
    font-size: 32px;
    font-weight: 600;
    letter-spacing: 1px;
    box-shadow: 0 0 25px rgba(255,0,128,0.25);
}

/* Button Glow */
div.stButton > button:first-child {
    background: linear-gradient(90deg, #FF0080, #7928CA);
    color: #FFF;
    border: none;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    font-weight: 600;
    box-shadow: 0 0 15px rgba(255,0,128,0.3);
    transition: all 0.3s ease-in-out;
}
div.stButton > button:first-child:hover {
    transform: scale(1.04);
    box-shadow: 0 0 25px rgba(255,0,128,0.5);
}

/* Text Areas */
textarea {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: white !important;
}

/* Dataframes */
div[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 10px;
}

/* Expanders */
.streamlit-expanderHeader {
    font-weight: 600;
    font-size: 16px;
    color: #FFF;
}

/* Scrollbars */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-thumb { background: #7928CA; border-radius: 6px; }
</style>
""", unsafe_allow_html=True)

# ---- MAIN APP ----
def main():
    st.markdown("<div class='title-container'>✨ Emovera</div>", unsafe_allow_html=True)

    menu = ["🏠 Home", "📂 File Analysis", "📊 Monitor", "ℹ️ About"]
    choice = st.sidebar.radio("Navigation", menu)

    create_page_visited_table()
    create_emotionclf_table()

    # ---------------- HOME ----------------
    if choice == "🏠 Home":
        add_page_visited_details("Home", datetime.now(IST))
        st.markdown("### ✨ Emotion Detection in Text")
        st.markdown("Enter text and let the model reveal the underlying emotion — powered by NLP & ML.")
        
        with st.form(key='emotion_clf_form'):
            raw_text = st.text_area("📝 Enter your text here:", height=150)
            submit_text = st.form_submit_button(label='Analyze Emotion 💡')

        if submit_text and raw_text.strip():
            with st.spinner("🔍 Analyzing emotion..."):
                prediction = predict_emotions(raw_text)
                probability = get_prediction_proba(raw_text)
                add_prediction_details(raw_text, prediction, np.max(probability), datetime.now(IST))

            col1, col2 = st.columns(2)

            with col1:
                st.success("### 🧠 Result")
                st.markdown(f"**Prediction:** {prediction} {emotions_emoji_dict[prediction]}")
                st.markdown(f"**Confidence:** `{np.max(probability):.2f}`")
                st.write(f"**Original Text:** {raw_text}")

            with col2:
                st.info("### 📊 Probability Chart")
                proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["Emotion", "Probability"]
                fig = alt.Chart(proba_df_clean).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                    x=alt.X('Emotion', sort='-y'),
                    y='Probability',
                    color=alt.Color('Emotion', scale=alt.Scale(scheme='dark2'))
                )
                st.altair_chart(fig, use_container_width=True)

    # ---------------- FILE ANALYSIS ----------------
    elif choice == "📂 File Analysis":
        add_page_visited_details("File Analysis", datetime.now(IST))
        st.markdown("### 📁 Batch Emotion Analysis")
        st.write("Upload a `.txt` file — each line is treated as a separate comment for emotion analysis.")

        uploaded_file = st.file_uploader("Upload Text File", type=['txt'])
        if uploaded_file:
            file_content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
            lines = [line.strip() for line in file_content.split("\n") if line.strip()]
            if not lines:
                st.warning("⚠️ The file is empty.")
            else:
                st.info(f"📄 Loaded **{len(lines)}** comments. Processing...")
                results = []
                progress = st.progress(0)
                for i, line in enumerate(lines):
                    pred = predict_emotions(line)
                    proba = get_prediction_proba(line)
                    conf = np.max(proba)
                    results.append([line, pred, conf])
                    add_prediction_details(line, pred, conf, datetime.now(IST))
                    progress.progress((i + 1) / len(lines))
                df_results = pd.DataFrame(results, columns=["Text", "Predicted Emotion", "Confidence"])
                st.success("✅ Analysis Complete!")
                st.dataframe(df_results)

                csv = df_results.to_csv(index=False).encode('utf-8')
                st.download_button("💾 Download Results", data=csv, file_name="emotion_results.csv", mime="text/csv")

                emotion_counts = df_results["Predicted Emotion"].value_counts().reset_index()
                emotion_counts.columns = ["Emotion", "Count"]
                col1, col2 = st.columns(2)
                with col1:
                    chart = alt.Chart(emotion_counts).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                        x='Emotion', y='Count', color='Emotion')
                    st.altair_chart(chart, use_container_width=True)
                with col2:
                    pie = px.pie(emotion_counts, values='Count', names='Emotion', title='Emotion Distribution')
                    st.plotly_chart(pie, use_container_width=True)

    # ---------------- MONITOR ----------------
    elif choice == "📊 Monitor":
        add_page_visited_details("Monitor", datetime.now(IST))
        st.markdown("### 📈 App Metrics Dashboard")

        with st.expander("🕒 Page Visits"):
            page_visited_details = pd.DataFrame(view_all_page_visited_details(), columns=['Page Name', 'Time of Visit'])
            st.dataframe(page_visited_details)
            pg_count = page_visited_details['Page Name'].value_counts().rename_axis('Page Name').reset_index(name='Counts')
            col1, col2 = st.columns(2)
            with col1:
                c = alt.Chart(pg_count).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                    x='Page Name', y='Counts', color='Page Name')
                st.altair_chart(c, use_container_width=True)
            with col2:
                p = px.pie(pg_count, values='Counts', names='Page Name', title='Page Visits')
                st.plotly_chart(p, use_container_width=True)

        with st.expander("🎯 Prediction Metrics"):
            df_emotions = pd.DataFrame(view_all_prediction_details(), columns=['Rawtext', 'Prediction', 'Probability', 'Time_of_Visit'])
            st.dataframe(df_emotions)
            prediction_count = df_emotions['Prediction'].value_counts().rename_axis('Prediction').reset_index(name='Counts')
            pc = alt.Chart(prediction_count).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                x='Prediction', y='Counts', color='Prediction')
            st.altair_chart(pc, use_container_width=True)

    # ---------------- ABOUT ----------------
    else:
        add_page_visited_details("About", datetime.now(IST))

        # ===== Custom CSS for Styling =====
        st.markdown("""
            <style>
            .glass-card {
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(12px);
                border-radius: 15px;
                padding: 25px;
                border: 1px solid rgba(255, 255, 255, 0.15);
                box-shadow: 0px 4px 25px rgba(0,0,0,0.15);
            }
            .title-text {
                background: linear-gradient(90deg, #8e44ad, #3498db);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 34px;
                font-weight: 800;
            }
            .emoji-badge {
                font-size: 28px;
                margin-right: 8px;
            }
            .hover-box:hover {
                transform: scale(1.03);
                transition: 0.2s ease-in-out;
            }
            </style>
        """, unsafe_allow_html=True)

        # ===== Header =====
        st.markdown('<p class="title-text">ℹ️ About Emovera</p>', unsafe_allow_html=True)

        # ===== Main Info Card =====
        with st.container():
            st.markdown('<div class="glass-card hover-box">', unsafe_allow_html=True)
            st.write("""
            **Emovera** is an AI-powered emotion intelligence platform that goes beyond numeric ratings like CSAT  
            and star reviews. Instead of asking *"How satisfied are you?"* — we ask **"How do you feel?"**

            Our system detects emotions inside customer comments in real time, unlocking deeper insight into the 
            experiences and emotional states customers have while interacting with any product or service.
            """)
            st.markdown("</div>", unsafe_allow_html=True)

        # ===== Expandable Emotion List =====
        with st.expander("🧠 What Emotions Do We Detect? Click to reveal"):
            st.write("""
            | Emotion | Emoji |
            |---------|-------|
            | Happy | 😄 |
            | Neutral | 😐 |
            | Angry | 😡 |
            | Sad | 😢 |
            | Surprised | 😮 |
            | Trust | 🤝 |
            | Confusion | 😕 |
            | Regret | 😔 |
            | Love | ❤️ |
            """)

        # ===== Highlight Section =====
        st.markdown('<div class="glass-card hover-box">', unsafe_allow_html=True)
        st.subheader("🚀 Why Emovera?")
        st.write("""
        - Numbers show **satisfaction**, but emotions show **truth**
        - Reveals hidden patterns behind complaints & praise  
        - Helps companies respond with emotion-aware strategies  
        - Converts raw feedback → **Emotion Analytics Dashboard**  
        - Builds stronger customer relationships based on empathy  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        # ===== Animated Tagline =====
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='text-align:center; font-weight:700; background: linear-gradient(90deg, #ff6a88, #ff99ac); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>"
            "This is not just sentiment analysis — this is Emotion Intelligence."
            "</h3>",
            unsafe_allow_html=True
        )


if __name__ == '__main__':
    main()
