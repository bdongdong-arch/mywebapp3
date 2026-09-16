import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")


import streamlit as st
import random
from urllib.parse import quote

# 페이지 설정
st.set_page_config(
    page_title="MBTI 웹소설 추천",
    page_icon="📚",
    layout="centered"
)


# 장르별 색상 (플레이스홀더 이미지 배경색)
GENRE_COLOR = {
    "현대판타지": "6C63FF",
    "게임판타지": "4CAF50",
    "로맨스판타지": "FF6FA0",
    "무협": "8B5E3C",
    "공포/미스터리": "2C2C54",
    "SF/재난": "1E90FF",
    "책빙의": "FFA500",
}

def cover_url(title, genre):
    color = GENRE_COLOR.get(genre, "6C63FF")
    text = quote(title)
    return f"https://placehold.co/500x300/{color}/FFFFFF?text={text}&font=noto-sans-kr"

# 웹소설 데이터베이스 (title, author, genre, desc)
N = {
    "전독시": ("전지적 독자 시점", "싱숑", "현대판타지", "치밀한 설계와 전략적 사고가 돋보이는 회귀물의 정점"),
    "나혼렙": ("나 혼자만 레벨업", "추공", "현대판타지", "체계적으로 성장해나가는 주인공의 압도적 성장기"),
    "템빨": ("템빨", "박새날", "게임판타지", "분석적으로 파고드는 아이템 헌팅 액션"),
    "재벌집": ("재벌집 막내아들", "산경", "현대판타지", "치밀한 전략과 야망으로 세상을 뒤집는 회귀 서사"),
    "달빛조각사": ("달빛조각사", "남희성", "게임판타지", "이상을 향해 묵묵히 나아가는 국민 게임판타지"),
    "묵향": ("묵향", "전동조", "무협", "감성적이고 낭만적인 무협 판타지의 고전"),
    "황제외동딸": ("황제의 외동딸", "윤슬", "로맨스판타지", "주변을 이끌고 챙기는 따뜻한 여주의 성장담"),
    "상수리나무": ("상수리나무 아래", "차소희", "로맨스판타지", "발랄하고 자유로운 영혼의 로맨스 판타지"),
    "데못죽": ("데뷔 못 하면 죽는 병 걸림", "백덕수", "현대판타지", "데뷔 못 하면 죽는다는 상태창의 협박 속 아이돌 서바이벌 성장기"),
    "괴담출근": ("괴담에 떨어져도 출근을 해야 하는구나", "백덕수", "공포/미스터리", "괴담 속 규칙을 분석해 위기를 하나씩 돌파해가는 격리 픽션"),
    "어바등": ("어두운 바다의 등불이 되어", "연산호", "SF/재난", "깊은 바닷속 재난 속에서 등불처럼 빛나는 한 사람의 이야기"),
    "백망나": ("백작가의 망나니가 되었다", "유려한", "책빙의", "망나니 도련님 몸에 빙의해 재치 있게 위기를 헤쳐가는 이야기"),
    "어공주": ("어느 날 공주가 되어버렸다", "플루토스", "로맨스판타지", "냉혹한 황제 아빠의 마음을 얻어가는 따뜻한 가족 성장담"),
    "던디": ("던전 디펜스", "유진성", "게임판타지", "과감하고 실전적인 전략 액션 판타지"),
    "나노마신": ("나노마신", "한중월야", "게임판타지", "목표를 향해 냉철하게 파고드는 게임 판타지"),
    "버림황비": ("버림 받은 황비", "정유나", "로맨스판타지", "회귀 후 진짜 행복을 찾아가는 로판계의 교과서적 명작"),
    "이생가": ("이번 생은 가주가 되겠습니다", "김로아", "로맨스판타지", "환생 후 목표를 향해 똑부러지게 나아가는 성장 로판"),
}

# MBTI별 추천 (각 2편)
novel_data = {
    "INTJ": ["전독시", "나혼렙"],
    "INTP": ["괴담출근", "템빨"],
    "ENTJ": ["재벌집", "던디"],
    "ENTP": ["백망나", "나노마신"],
    "INFJ": ["어바등", "달빛조각사"],
    "INFP": ["묵향", "황제외동딸"],
    "ENFJ": ["어공주", "이생가"],
    "ENFP": ["데못죽", "상수리나무"],
    "ISTJ": ["나혼렙", "재벌집"],
    "ISFJ": ["버림황비", "어공주"],
    "ESTJ": ["재벌집", "던디"],
    "ESFJ": ["이생가", "황제외동딸"],
    "ISTP": ["괴담출근", "나노마신"],
    "ISFP": ["어바등", "상수리나무"],
    "ESTP": ["던디", "백망나"],
    "ESFP": ["데못죽", "어공주"],
}

# ---- 스타일 ----
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 2.2em;
    font-weight: 800;
    color: #6C63FF;
    margin-bottom: 0px;
}
.sub-title {
    text-align: center;
    color: #888;
    margin-bottom: 30px;
}
.novel-card {
    background-color: #F8F7FF;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 15px;
    border: 1px solid #E5E1FF;
}
.novel-title {
    font-size: 1.25em;
    font-weight: 700;
    color: #4B3F72;
    margin-top: 8px;
}
.novel-author {
    color: #A594F9;
    font-size: 0.9em;
    margin-bottom: 6px;
}
.novel-genre {
    display: inline-block;
    background-color: #E5E1FF;
    color: #6C63FF;
    font-size: 0.75em;
    padding: 2px 10px;
    border-radius: 12px;
    margin-bottom: 6px;
}
.novel-desc {
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# ---- 헤더 ----
st.markdown('<div class="main-title">📚 MBTI 웹소설 추천기</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 MBTI에 딱 맞는 웹소설을 찾아드려요 ✨</div>', unsafe_allow_html=True)

st.write("")

# ---- MBTI 선택 ----
col1, col2 = st.columns(2)
with col1:
    e_i = st.radio("에너지 방향", ["E (외향)", "I (내향)"], horizontal=True)
    s_n = st.radio("인식 기능", ["S (감각)", "N (직관)"], horizontal=True)
with col2:
    t_f = st.radio("판단 기능", ["T (사고)", "F (감정)"], horizontal=True)
    j_p = st.radio("생활 양식", ["J (판단)", "P (인식)"], horizontal=True)

mbti = e_i[0] + s_n[0] + t_f[0] + j_p[0]

st.write("")

# ---- 추천 버튼 ----
if st.button("🔮 내 MBTI 웹소설 추천받기", use_container_width=True):
    st.markdown(f"### 당신의 MBTI: **{mbti}**")
    st.write("")

    keys = novel_data.get(mbti, [])
    if keys:
        for key in keys:
            title, author, genre, desc = N[key]
            img_url = cover_url(title, genre)
            st.image(img_url, use_container_width=True)
            st.markdown(f"""
            <div class="novel-card">
                <span class="novel-genre">{genre}</span>
                <div class="novel-title">📖 {title}</div>
                <div class="novel-author">✍️ {author}</div>
                <div class="novel-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.info("아직 준비된 추천작이 없어요! 곧 업데이트할게요 🙏")

st.write("")
st.markdown("---")
st.caption("Made with 💜 using Streamlit")
