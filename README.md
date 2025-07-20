
## 📘 ADsP 연관 문제 생성기

이 프로젝트는 ADsP 시험을 준비하는 수험생을 위해, 기존 개념에 기반한 **유사 항목 추천** 및 **GPT를 활용한 새로운 문제 자동 생성** 기능을 제공합니다.

![streamlit preview](https://img.shields.io/badge/Streamlit-Enabled-brightgreen)
![OpenAI GPT](https://img.shields.io/badge/OpenAI-GPT4o-blue)
![Embedding](https://img.shields.io/badge/SentenceTransformer-MiniLM--L6--v2-lightgrey)

---

### 🔧 주요 기능

* 📚 **ADsP 핵심 개념 검색**: 키워드 기반 또는 예시 선택 기반 검색
* 🔍 **의미 유사도 기반 연관 항목 추천**: 임베딩 + FAISS 검색
* 🧠 **GPT 문제 자동 생성**: 선택한 항목을 바탕으로 GPT-4o가 문제 출제

---

### 📁 프로젝트 구조

```
ads_exam_generator/
├── app.py                       # Streamlit 메인 앱
├── data/
│   └── message.txt              # ADsP 개념 설명 데이터 (JSONL 형식)
├── .streamlit/
│   └── secrets.toml             # OpenAI API 키 보관 (숨김 폴더)
└── requirements.txt             # 설치 필요한 라이브러리 목록
```

---

### 🚀 설치 및 실행 방법

#### 1. 설치

```bash
git clone <your-repo-url>
cd ads_exam_generator
pip install -r requirements.txt
```

#### 2. OpenAI 키 설정

`.streamlit/secrets.toml` 파일을 생성하고 아래처럼 작성하세요:

```toml
OPENAI_API_KEY = "your-openai-key"
```

> 🔒 `.streamlit/` 폴더는 숨김 폴더이므로 탐색기에서 보이지 않을 수 있습니다.
> 보는 법 
📍 Windows
탐색기에서 폴더 열기

상단 메뉴 → [보기] → [숨긴 항목] 체크

📍 macOS
bash
복사
편집
⌘ Command + Shift + .

#### 3. 앱 실행

```bash
streamlit run app.py
```

---

### 💡 사용 예시

1. \*\*“정량적 데이터”\*\*를 입력하거나 예시 키워드에서 선택
2. 유사한 개념 3개 표시
3. GPT가 해당 개념을 바탕으로 새로운 문제를 자동 생성
4. 생성된 문제 확인

---

### 📦 requirements.txt

```txt
streamlit
pandas
numpy
sentence-transformers
faiss-cpu
openai
```

---

### 🧠 사용 모델

* 텍스트 임베딩: `sentence-transformers/all-MiniLM-L6-v2`
* 문제 생성: `OpenAI GPT-4o` (chat API)

---

### 📮 기여

Pull Request와 Issue 모두 환영합니다.
ADsP 외에도 SQLD, 빅데이터 분석기사 등으로 확장 가능성이 있습니다.

---


