import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="KB 시니어 연금 계산기",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS 스타일링 - 원본 디자인에 더 가깝게 수정
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 20px 0;
        margin-bottom: 30px;
        background-color: #f8f9fa;
    }
    
    .kb-logo {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    
    .kb-star {
        color: #FFB800;
        margin-right: 8px;
    }
    
    .kb-text {
        color: #666;
        margin-right: 15px;
    }
    
    .elderly-emoji {
        font-size: 48px;
        margin-left: 10px;
    }
    
    .title {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        margin-top: 15px;
    }
    
    .stApp {
        max-width: 350px;
        margin: 0 auto;
        background-color: #f8f9fa;
        padding: 20px;
    }
    
    /* Streamlit 버튼 스타일링 */
    .stButton > button {
        width: 100% !important;
        height: 80px !important;
        border-radius: 20px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease !important;
        white-space: pre-line !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
    }
    
    /* 첫 번째 버튼 (미수령) - 노란색 */
    div[data-testid="stVerticalBlock"] > div:nth-child(1) .stButton > button {
        background: #FFE4B5 !important;
        color: #8B4513 !important;
    }
    
    /* 두 번째 버튼 (수령중) - 파란색 */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) .stButton > button {
        background: #B8D4F0 !important;
        color: #2C5282 !important;
    }
    
    /* 세 번째 버튼 (상품정보) - 초록색 */
    div[data-testid="stVerticalBlock"] > div:nth-child(5) div:nth-child(1) .stButton > button {
        background: #C6F6D5 !important;
        color: #22543D !important;
        height: 60px !important;
        font-size: 16px !important;
    }
    
    /* 네 번째 버튼 (전화상담) - 분홍색 */
    div[data-testid="stVerticalBlock"] > div:nth-child(5) div:nth-child(2) .stButton > button {
        background: #FED7E2 !important;
        color: #97266D !important;
        height: 60px !important;
        font-size: 16px !important;
    }
    
    /* 모바일 최적화 */
    @media (max-width: 400px) {
        .custom-button {
            font-size: 18px;
            padding: 20px 15px;
        }
        
        .green-button, .pink-button {
            font-size: 14px;
            padding: 18px 8px;
        }
        
        .kb-logo {
            font-size: 32px;
        }
        
        .title {
            font-size: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# 헤더 - 원본 디자인과 더 유사하게
st.markdown("""
<div class="main-header">
    <div class="kb-logo">
        <span class="kb-star">★</span><span class="kb-text">b KB</span>
        <span class="elderly-emoji">👴👵</span>
    </div>
    <div class="title">시니어 연금 계산기</div>
</div>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'question_step' not in st.session_state:
    st.session_state.question_step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# 메인 페이지
if st.session_state.page == 'main':
    # 현재 연금 미수령 중 버튼
    if st.button("현재 연금\n미수령 중", key="pension_not_receiving", use_container_width=True):
        st.session_state.page = 'not_receiving'
        st.rerun()
    
    st.markdown('<div style="margin: 15px 0;"></div>', unsafe_allow_html=True)
    
    # 현재 연금 수령 중 버튼  
    if st.button("현재 연금\n수령 중", key="pension_receiving", use_container_width=True):
        st.session_state.page = 'receiving'
        st.rerun()
    
    st.markdown('<div style="margin: 20px 0;"></div>', unsafe_allow_html=True)
    
    # 하단 버튼들
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("상품\n정보", key="product_info", use_container_width=True):
            st.session_state.page = 'product_info'
            st.rerun()
    
    with col2:
        if st.button("전화\n상담", key="phone_consultation", use_container_width=True):
            st.session_state.page = 'phone_consultation'
            st.rerun()

# 현재 연금 미수령 중 페이지 - 단계별 질문
elif st.session_state.page == 'not_receiving':
    # 질문 데이터
    questions = {
        1: {
            "title": "연금 계산기 2",
            "question": "1. 월급 월소득을\n입력해주세요.",
            "type": "input"
        },
        2: {
            "title": "연금 계산기 3", 
            "question": "2. 국민연금\n가입기간을\n입력해주세요.",
            "type": "input"
        },
        3: {
            "title": "연금 계산기 29",
            "question": "1. 나이를\n입력해주세요.",
            "type": "input"
        },
        4: {
            "title": "연금 계산기 22",
            "question": "2. 성별을\n선택해주세요.",
            "type": "choice",
            "options": ["남성", "여성"]
        },
        5: {
            "title": "연금 계산기 28",
            "question": "3. 가구원 수를\n입력해주세요.",
            "type": "input"
        },
        6: {
            "title": "연금 계산기 23",
            "question": "5. 파부양자가\n있나요?",
            "type": "choice",
            "options": ["예", "아니오"]
        },
        7: {
            "title": "연금 계산기 24",
            "question": "6. 현재 보유한\n금융자산을\n입력해주세요.",
            "type": "input"
        },
        8: {
            "title": "연금 계산기 25",
            "question": "7. 월 수입하는\n연금 급여를\n입력해주세요.",
            "type": "input"
        },
        9: {
            "title": "연금 계산기 26",
            "question": "8. 월 평균\n지출비를\n입력해주세요.",
            "type": "input"
        },
        10: {
            "title": "연금 계산기 27",
            "question": "9. 투자 성향을\n선택해주세요.",
            "type": "choice",
            "options": ["안정형", "안정추구형", "위험중립형", "적극투자형"]
        }
    }
    
    current_q = questions[st.session_state.question_step]
    
    # 헤더
    st.markdown(f"""
    <div class="main-header">
        <div class="kb-logo">
            <span class="kb-star">★</span><span class="kb-text">b KB</span>
        </div>
        <div class="title">{current_q['title']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 질문 표시
    st.markdown(f"""
    <div style="text-align: center; font-size: 18px; font-weight: bold; margin: 40px 0; line-height: 1.5;">
        {current_q['question']}
    </div>
    """, unsafe_allow_html=True)
    
    # 답변 입력/선택
    if current_q['type'] == 'input':
        if st.session_state.question_step == 1:  # 월급
            answer = st.text_input("월 소득을 입력하세요 (만원)", key=f"q{st.session_state.question_step}")
        elif st.session_state.question_step == 2:  # 가입기간
            answer = st.text_input("국민연금 가입기간을 입력하세요 (년)", key=f"q{st.session_state.question_step}")
        elif st.session_state.question_step == 3:  # 나이
            answer = st.text_input("나이를 입력하세요", key=f"q{st.session_state.question_step}")
        elif st.session_state.question_step == 5:  # 가구원수
            answer = st.text_input("가구원 수를 입력하세요", key=f"q{st.session_state.question_step}")
        elif st.session_state.question_step == 7:  # 금융자산
            answer = st.text_input("현재 보유 금융자산을 입력하세요 (만원)", key=f"q{st.session_state.question_step}")
        elif st.session_state.question_step == 8:  # 월 연금급여
            answer = st.text_input("월 수입하는 연금 급여를 입력하세요 (만원)", key=f"q{st.session_state.question_step}")
        elif st.session_state.question_step == 9:  # 월 지출
            answer = st.text_input("월 평균 지출비를 입력하세요 (만원)", key=f"q{st.session_state.question_step}")
        
        if st.button("다음", key="next_btn") and answer:
            st.session_state.answers[st.session_state.question_step] = answer
            if st.session_state.question_step < 10:
                st.session_state.question_step += 1
                st.rerun()
            else:
                st.session_state.page = 'result'
                st.rerun()
    
    elif current_q['type'] == 'choice':
        st.markdown('<div style="margin: 20px 0;"></div>', unsafe_allow_html=True)
        
        for option in current_q['options']:
            if st.button(option, key=f"choice_{option}"):
                st.session_state.answers[st.session_state.question_step] = option
                if st.session_state.question_step < 10:
                    st.session_state.question_step += 1
                    st.rerun()
                else:
                    st.session_state.page = 'result'
                    st.rerun()
    
    # 진행 상황 표시
    progress = st.session_state.question_step / 10
    st.progress(progress)
    st.markdown(f"<div style='text-align: center; margin-top: 10px;'>{st.session_state.question_step}/10</div>", unsafe_allow_html=True)
    
    # 이전/메인으로 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← 이전"):
            if st.session_state.question_step > 1:
                st.session_state.question_step -= 1
                st.rerun()
    
    with col2:
        if st.button("메인으로"):
            st.session_state.page = 'main'
            st.session_state.question_step = 1
            st.session_state.answers = {}
            st.rerun()

# 결과 페이지
elif st.session_state.page == 'result':
    st.markdown("""
    <div class="main-header">
        <div class="kb-logo">
            <span class="kb-star">★</span><span class="kb-text">b KB</span>
        </div>
        <div class="title">연금 계산 결과</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 계산 결과")
    
    # 간단한 연금 계산 (입력된 답변 기반)
    if 1 in st.session_state.answers and 2 in st.session_state.answers:
        try:
            monthly_income = float(st.session_state.answers[1])
            pension_years = float(st.session_state.answers[2])
            estimated_pension = (monthly_income * 0.015 * pension_years)
            
            st.success(f"🎯 예상 월 연금액: {estimated_pension:,.0f}만원")
            
            # 입력한 정보 요약
            st.markdown("### 📋 입력 정보 요약")
            for step, answer in st.session_state.answers.items():
                question_title = questions[step]['question'].replace('\n', ' ')
                st.write(f"**{question_title}**: {answer}")
                
        except ValueError:
            st.error("입력값에 오류가 있습니다.")
    
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = 'main'
        st.session_state.question_step = 1
        st.session_state.answers = {}
        st.rerun()

# 현재 연금 수령 중 페이지
elif st.session_state.page == 'receiving':
    st.markdown("### 💰 현재 연금 수령 중")
    st.write("연금 수령 현황을 확인해보세요.")
    
    current_pension = st.number_input("현재 월 수령액 (만원)", min_value=0, value=100)
    start_year = st.number_input("수령 시작 연도", min_value=1980, max_value=2024, value=2020)
    
    if st.button("수령 현황 보기"):
        years_receiving = 2024 - start_year
        total_received = current_pension * 12 * years_receiving * 10000
        st.info(f"수령 기간: {years_receiving}년")
        st.info(f"총 수령액: {total_received:,.0f}원")
    
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = 'main'
        st.rerun()

# 상품 정보 페이지
elif st.session_state.page == 'product_info':
    st.markdown("### 📋 상품 정보")
    st.write("KB 시니어 연금 상품에 대한 자세한 정보입니다.")
    
    st.markdown("""
    **주요 특징:**
    - 안정적인 노후 소득 보장
    - 세제 혜택 제공
    - 다양한 수령 방식 선택 가능
    - 전문가 상담 서비스
    
    **가입 조건:**
    - 만 18세 이상 65세 이하
    - 국민연금 가입자
    - 소득 증빙 가능자
    """)
    
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = 'main'
        st.rerun()

# 전화 상담 페이지
elif st.session_state.page == 'phone_consultation':
    st.markdown("### 📞 전화 상담")
    st.write("전문 상담사와 1:1 상담을 받아보세요.")
    
    st.markdown("""
    **KB 시니어 연금 상담센터**
    
    📞 **상담 전화번호:** 1588-9999
    
    **상담 시간:**
    - 평일: 오전 9시 ~ 오후 6시
    - 토요일: 오전 9시 ~ 오후 1시
    - 일요일 및 공휴일 휴무
    
    **상담 가능 내용:**
    - 연금 상품 안내
    - 가입 절차 문의
    - 수령 방법 상담
    - 세제 혜택 안내
    """)
    
    name = st.text_input("성함")
    phone = st.text_input("연락처")
    
    if st.button("상담 신청하기"):
        if name and phone:
            st.success("상담 신청이 완료되었습니다. 곧 연락드리겠습니다.")
        else:
            st.error("성함과 연락처를 모두 입력해주세요.")
    
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = 'main'
        st.rerun()
