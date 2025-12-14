# EMOVERA
# 🌟 Emovera – Emotion-Based Customer Feedback Analysis

Emovera is an AI-powered emotion classification system that analyzes customer comments and identifies **emotional states instead of numeric ratings**. Traditional feedback metrics like star ratings or CSAT scores quantify satisfaction but fail to explain *how customers truly feel*. Emovera bridges this gap by converting textual feedback into **actionable emotional insights**.

By detecting emotions such as **Happy 😄, Neutral 😐, Angry 😡, Sad 😢, Surprised 😮, Trust 🤝, Confusion 😕, Regret 😔, and Love ❤️**, Emovera enables businesses to make **human-centered decisions** based on real emotional signals.

---

## 🚀 Features

* 🧠 **Emotion-Based Classification** – Identifies customer emotions from textual feedback
* 📊 **Beyond Ratings** – Works independently of star ratings or CSAT scores
* 🤖 **AI / NLP Powered** – Uses trained machine learning models for emotion detection
* 📈 **Emotional Trend Analysis** – Helps track changes in customer emotions over time
* 🔍 **Actionable Insights** – Reveals hidden frustration, loyalty, or confusion
* 🌐 **Extensible Architecture** – Easily integrable with dashboards or APIs

---

## 🛠️ Installation

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/expertise03/emovera.git
cd emovera
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Application

```bash
streamlit run app.py
```

```
App Running Port
http://localhost:8501


### Basic Workflow

1. Input customer feedback text
2. Text is preprocessed and cleaned
3. Trained emotion classification model analyzes the text
4. Detected emotion is returned with its label

Example:

```text
Input  : "The service was slow and frustrating"
Output : Angry 😡
```

---

## 🧩 Project Architecture

```
┌──────────────────────┐
│  Customer Feedback   │
│   (Text Comments)    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Text Preprocessing  │
│ (Cleaning, Tokenize) │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Emotion ML Model     │
│ (Trained Classifier) │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Emotion Prediction   │
│ (Happy, Angry, etc.) │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Business Insights    │
│ Human-Centered CX    │
└──────────────────────┘
```

---

## 📂 Project Structure

```
emotion-classifier-main/
|
emotion-classifier-main/
│
├── data/               # Dataset files
├── images/             # Images & visuals
├── models/             # Trained ML models
│
├── app.py              # Main application entry point
├── track_utils.py      # Utility functions
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── .gitignore          # Git ignore rules
```

---

## 🎯 Applications

* Customer Experience (CX) Analytics
* Product Feedback Analysis
* Social Media Sentiment & Emotion Detection
* Customer Support Optimization
* Brand Trust & Loyalty Measurement

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

✨ *Emovera helps you understand not just what

## 🧠 How It Works

1. User enters text (or uploads CSV)
2. NLP model processes the input
3. The system predicts emotional class from 8–10 labels
4. Results appear in UI with:
   - Emotion tag
   - Probability score
   - Emoji visualization
5. Download results as CSV for further use

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit + Custom CSS (Glass UI) |
| Backend | Python |
| ML Model | Scikit-learn / Transformers (custom trained) |
| Data | Preprocessed customer review dataset |
| Logging | SQLite / CSV logs |
| Deployment | Streamlit Cloud / Local runtime |
<img width="1919" height="946" alt="Screenshot 2025-12-14 203530" src="https://github.com/user-attachments/assets/2580da9b-caa4-45aa-bce9-21313ae3bdef" />

<img width="1912" height="951" alt="Screenshot 2025-12-14 203514" src="https://github.com/user-attachments/assets/b269bc6c-ac6c-40a2-940a-735683f797fc" />

<img width="1908" height="964" alt="Screenshot 2025-12-14 203222" src="https://github.com/user-attachments/assets/4e60e86f-fc22-4e15-b000-76d868deddc3" />

<img width="1909" height="902" alt="Screenshot 2025-12-14 203237" src="https://github.com/user-attachments/assets/39687e49-bcb3-42cd-be76-37987578f687" />

<img width="1906" height="968" alt="Screenshot 2025-12-14 203301" src="https://github.com/user-attachments/assets/9016d5bc-019a-4bb3-9ca0-e272f1b31fcf" />

<img width="1904" height="912" alt="Screenshot 2025-12-14 203328" src="https://github.com/user-attachments/assets/732a8609-1612-43a4-ae9f-7d16c37aef6e" />

<img width="1917" height="954" alt="Screenshot 2025-12-14 203412" src="https://github.com/user-attachments/assets/7446b17b-3b26-4033-ae58-63fab16221cb" />







