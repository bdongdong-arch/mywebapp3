import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")

import streamlit as st

st.set_page_config(
    page_title="MBTI 여행지 추천",
    page_icon="✈️",
    layout="centered",
)

# ---------------- 데이터 ----------------
MBTI_DATA = {
    "INTJ": {"emoji": "🧠", "place": "아이슬란드", "desc": "고요한 자연 속에서 깊이 사색할 수 있는 곳이에요. 계획적인 당신에게 완벽한 여정이 될 거예요."},
    "INTP": {"emoji": "🔭", "place": "스위스 취리히", "desc": "정교하고 지적인 도시. 박물관과 도서관을 자유롭게 탐구할 수 있어요."},
    "ENTJ": {"emoji": "🏙️", "place": "뉴욕", "desc": "야망과 에너지가 넘치는 도시. 리더십을 발휘하며 새로운 기회를 탐색해보세요."},
    "ENTP": {"emoji": "💡", "place": "베를린", "desc": "자유롭고 실험적인 분위기. 토론과 새로운 아이디어가 넘치는 도시예요."},
    "INFJ": {"emoji": "🌸", "place": "교토", "desc": "고요한 사찰과 정원에서 내면의 평화를 찾아보세요."},
    "INFP": {"emoji": "🎨", "place": "포르투", "desc": "감성적이고 예술적인 골목길. 당신의 상상력을 자극할 도시예요."},
    "ENFJ": {"emoji": "🤝", "place": "코펜하겐", "desc": "따뜻한 공동체 문화와 사람 중심의 도시 디자인이 인상적이에요."},
    "ENFP": {"emoji": "🌈", "place": "바르셀로나", "desc": "자유분방하고 창의적인 에너지가 가득한 곳. 즉흥적인 여행이 잘 어울려요."},
    "ISTJ": {"emoji": "🏛️", "place": "빈", "desc": "전통과 질서가 살아있는 우아한 도시. 체계적인 일정 여행에 딱이에요."},
    "ISFJ": {"emoji": "🍵", "place": "체코 프라하", "desc": "아늑하고 편안한 분위기. 안정감을 느끼며 여유롭게 둘러보세요."},
    "ESTJ": {"emoji": "📋", "place": "싱가포르", "desc": "효율적이고 깔끔한 도시. 계획대로 착착 진행되는 여행을 즐길 수 있어요."},
    "ESFJ": {"emoji": "🎉", "place": "발리", "desc": "사람들과 어울리기 좋은 따뜻한 휴양지. 함께하는 즐거움이 커져요."},
    "ISTP": {"emoji": "🧗", "place": "뉴질랜드", "desc": "액티비티와 모험이 가득한 대자연. 손으로 직접 부딪히며 즐겨보세요."},
    "ISFP": {"emoji": "🌿", "place": "발리 우붓", "desc": "자연과 예술이 어우러진 감성적인 공간. 자유로운 영혼에게 어울려요."},
    "ESTP": {"emoji": "🏄", "place": "호주 골드코스트", "desc": "액티브하고 짜릿한 경험이 가득한 곳. 지금 이 순간을 즐기세요."},
    "ESFP": {"emoji": "🎊", "place": "리우데자네이루", "desc": "축제 같은 활기찬 분위기. 사람들과 어울리며 신나게 즐겨보세요."},
}

# ---------------- 스타일 ----------------
st.markdown(
    """
    <style>
    .main {
        background-color: #FFF9F5;
    }
    .title-text {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #FF6F61;
        margin-bottom: 0px;
    }
    .subtitle-text {
        text-align: center;
        color: #8A8A8A;
        font-size: 1rem;
        margin-bottom: 30px;
    }
    .result-card {
        background: linear-gradient(135deg, #FFE8E0 0%, #FFF3E9 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        margin-top: 20px;
    }
    .result-emoji {
        font-size: 3rem;
    }
    .result-place {
        font-size: 1.8rem;
        font-weight: 800;
        color: #444444;
        margin: 10px 0;
    }
    .result-desc {
        font-size: 1rem;
        color: #666666;
        line-height: 1.6;
    }
    div.stButton > button {
        background-color: #FF6F61;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        font-weight: 700;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #FF8A75;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- 화면 구성 ----------------
st.markdown('<p class="title-text">✈️ MBTI 여행지 추천</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">당신의 MBTI에 딱 맞는 여행지를 찾아드려요 🌍</p>', unsafe_allow_html=True)

mbti_types = list(MBTI_DATA.keys())
selected_mbti = st.selectbox("나의 MBTI를 선택해주세요", mbti_types, index=None, placeholder="MBTI 선택 👇")

if st.button("여행지 추천받기 🎁"):
    if selected_mbti is None:
        st.warning("MBTI를 먼저 선택해주세요! 😅")
    else:
        info = MBTI_DATA[selected_mbti]
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-emoji">{info['emoji']}</div>
                <div class="result-place">{selected_mbti}님께 추천하는 여행지</div>
                <div class="result-place" style="color:#FF6F61;">{info['place']}</div>
                <div class="result-desc">{info['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.balloons()

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Made with ❤️ using Streamlit")
