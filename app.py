import streamlit as st
import json
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import openai

# STEP 1: Load and preprocess data
with open("data/message.txt", "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]
df = pd.DataFrame(data)
df["text"] = df["first_table"] + " > " + df["second_table"] + " > " + df["third_table"] + "\n" + df["contents"]

# STEP 2: Generate or load embeddings
@st.cache_resource
def embed_texts(texts):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return np.array(model.encode(texts))

embeddings = embed_texts(df["text"].tolist())
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# STEP 3: UI - Keyword selection (예시 + 직접 입력)
st.title("📘 ADsP 연관 문제 생성기")

st.markdown("**아래 예시 중 선택하거나, 직접 키워드를 입력하세요.**")

sample_keywords = sorted(set(df["third_table"]))[:20] + [
    "DIKW 피라미드", "정형/비정형 데이터", "ERP", "CRM", "SQL SELECT", "데이터 마트 vs 웨어하우스"
]

col1, col2 = st.columns([2, 3])
with col1:
    selected_example = st.selectbox("예시 키워드", sample_keywords)
with col2:
    custom_query = st.text_input("또는 직접 입력:", placeholder="예: 정량적 데이터, CRM, SELECT문 등")

query = custom_query if custom_query.strip() else selected_example

# STEP 4: 임베딩 검색
if query:
    st.subheader("🔍 유사 항목 추천")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding).astype("float32"), k=3)

    for i in I[0]:
        st.markdown(f"**{df.iloc[i]['third_table']}**")
        st.markdown(df.iloc[i]["contents"])
        st.markdown("---")

    # STEP 5: GPT 문제 생성
    with st.spinner("GPT가 새로운 문제를 만드는 중입니다..."):
        combined_text = "\n\n".join(df.iloc[i]["text"] for i in I[0])

        prompt = f"""다음 내용을 참고하여 ADsP 스타일의 객관식 문제를 새로 만들어줘. 문제는 1개, 4지선다형 보기와 정답을 포함해줘.\n\n{combined_text}"""

        openai.api_key = st.secrets["OPENAI_API_KEY"]  # streamlit secrets 사용
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        st.subheader("🆕 생성된 문제")
        st.write(response.choices[0].message.content)