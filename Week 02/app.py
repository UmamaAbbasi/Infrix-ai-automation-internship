import streamlit as st

st.set_page_config(
    page_title="Infrix AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.title {
    text-align: center;
    color: #38bdf8;
    font-size: 55px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 40px;
}

.question-box {
    display: flex;
    justify-content: center;
}

.result-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #38bdf8;
    margin-top: 10px;
    color: white;
    font-size: 18px;
}

.stTextInput > div > div > input {
    text-align: center;
    font-size: 18px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">🤖 Infrix AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Chatbot Using Scraped Website Data</div>',
    unsafe_allow_html=True
)
with st.sidebar:
    st.title("📌 Project Info")

    st.write("""
    **Intern:** Your Name

    **Company:** Infrix

    **Task:** Week 2

    **Project:** AI-Powered Chatbot
    """)
# Load Data
try:
    with open("training_data.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

    # Center Input
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        question = st.text_input(
            "Ask Your Question",
            placeholder="Type life, love, success ..."
        )

    if question:

        results = []

        for line in data:
            if question.lower() in line.lower():
                results.append(line)

        st.write("")

        if results:

            st.success(
                f"Found {len(results)} matching result(s)"
            )

            for result in results[:5]:

                st.markdown(
                    f"""
                    <div class="result-card">
                    {result}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:
            st.error("No relevant information found.")

except FileNotFoundError:

    st.error(
        "training_data.txt not found. Run web_scrapper.py first."
    )