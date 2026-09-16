import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")


import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 웹소설 추천",
    page_icon="📚",
    layout="centered"
)

# MBTI별 웹소설 데이터베이스
novel_data = {
    "INTJ": [
        {"title": "전지적 독자 시점", "author": "싱숑", "desc": "치밀한 설계와 전략적 사고가 돋보이는 회귀물의 정점"},
        {"title": "나 혼자만 레벨업", "author": "추공", "desc": "체계적으로 성장해나가는 주인공의 이야기"},
    ],
    "INTP": [
        {"title": "화산귀환", "author": "비가", "desc": "논리적이고 계산적인 두뇌 플레이가 일품"},
        {"title": "템빨", "author": "박새날", "desc": "분석적으로 파고드는 아이템 헌팅 액션"},
    ],
    "ENTJ": [
        {"title": "재벌집 막내아들", "author": "산경", "desc": "리더십과 야망으로 세상을 뒤집는 이야기"},
        {"title": "download", "author": "조석", "desc": "목표 지향적인 주인공의 압도적 성장기"},
    ],
    "ENTP": [
        {"title": "김 부장", "author": "박새날", "desc": "기발한 아이디어와 임기응변이 빛나는 코믹 판타지"},
        {"title": "폭군의 셰프", "author": "제나", "desc": "재치와 창의력으로 위기를 돌파하는 이야기"},
    ],
    "INFJ": [
        {"title": "구원자", "author": "라마르", "desc": "깊은 통찰력과 내면의 성장이 중심인 이야기"},
        {"title": "달빛조각사", "author": "남희성", "desc": "이상을 향해 묵묵히 나아가는 서사"},
    ],
    "INFP": [
        {"title": "묵향", "author": "전동조", "desc": "감성적이고 낭만적인 무협 판타지의 고전"},
        {"title": "그 해, 우리는", "author": "웹소설 각색작", "desc": "섬세한 감정선이 돋보이는 힐링 로맨스"},
    ],
    "ENFJ": [
        {"title": "황제의 외동딸", "author": "숙향", "desc": "주변을 이끌고 챙기는 따뜻한 여주의 성장담"},
        {"title": "버림받은 왕비", "author": "제나", "desc": "공감 능력과 리더십이 돋보이는 로판"},
    ],
    "ENFP": [
        {"title": "상수리나무 아래", "author": "차소희", "desc": "발랄하고 자유로운 영혼의 로맨스 판타지"},
        {"title": "빙의로판 다수작", "author": "다양한 작가", "desc": "활기찬 에너지가 넘치는 명랑 로판"},
    ],
    "ISTJ": [
        {"title": "무공만빵빵해도 살아남는다", "author": "요람", "desc": "원칙과 성실함으로 차근차근 성장하는 이야기"},
        {"title": "환생좌", "author": "산경", "desc": "꼼꼼하고 계획적인 인생 설계 판타지"},
    ],
    "ISFJ": [
        {"title": "이상한 변호사 우영우 각색", "author": "웹소설화", "desc": "배려심 깊고 세심한 캐릭터의 성장기"},
        {"title": "간 떨어지는 동거", "author": "홍짬뽕", "desc": "따뜻하고 배려 가득한 로맨스 판타지"},
    ],
    "ESTJ": [
        {"title": "전무후무", "author": "매지션", "desc": "체계적 관리와 추진력이 돋보이는 기업물"},
        {"title": "천재소년의 계약결혼", "author": "다양", "desc": "효율적이고 실용적인 문제 해결형 주인공"},
    ],
    "ESFJ": [
        {"title": "공작저의 사냥개", "author": "정연", "desc": "사람들을 챙기고 조율하는 따뜻한 여주"},
        {"title": "결혼반지는 진심이 아니었습니다", "author": "다양", "desc": "관계 중심의 사랑스러운 로판"},
    ],
    "ISTP": [
        {"title": "SSS급 자살헌터", "author": "박서준", "desc": "실전적이고 효율적인 액션 판타지"},
        {"title": "레디 플레이어 원 스타일 게임판타지", "author": "다양", "desc": "실용적 문제 해결이 돋보이는 게임 판타지"},
    ],
    "ISFP": [
        {"title": "달빛유령", "author": "박서리", "desc": "조용하지만 감성적인 매력의 판타지"},
        {"title": "여신강림 각색 로판", "author": "다양", "desc": "예술적 감각과 개성이 돋보이는 이야기"},
    ],
    "ESTP": [
        {"title": "김치찌개용 돼지고기를 사러 왔다가", "author": "산경", "desc": "즉흥적이고 다이나믹한 액션 판타지"},
        {"title": "던전 디펜스", "author": "유진성", "desc": "과감하고 실전적인 전략 액션"},
    ],
    "ESFP": [
        {"title": "황녀, 반역자를 각인시키다", "author": "다양", "desc": "화려하고 에너지 넘치는 로맨스 판타지"},
        {"title": "악녀는 마리오네트", "author": "체리핑", "desc": "밝고 사교적인 매력의 로판"},
    ],
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
    padding: 20px;
    margin-bottom: 15px;
    border: 1px solid #E5E1FF;
}
.novel-title {
    font-size: 1.3em;
    font-weight: 700;
    color: #4B3F72;
}
.novel-author {
    color: #A594F9;
    font-size: 0.9em;
    margin-bottom: 8px;
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

    novels = novel_data.get(mbti, [])
    if novels:
        for novel in novels:
            st.markdown(f"""
            <div class="novel-card">
                <div class="novel-title">📖 {novel['title']}</div>
                <div class="novel-author">✍️ {novel['author']}</div>
                <div class="novel-desc">{novel['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.info("아직 준비된 추천작이 없어요! 곧 업데이트할게요 🙏")

st.write("")
st.markdown("---")
st.caption("Made with 💜 using Streamlit")
