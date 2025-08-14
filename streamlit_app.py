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
    
    /* 선택 버튼 스타일링 */
    div[data-testid="stVerticalBlock"] .stButton > button {
        background: #E8F4FD !important;
        color: #1E40AF !important;
        border: 2px solid #60A5FA !important;
        border-radius: 15px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 20px !important;
        margin: 10px 0 !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-testid="stVerticalBlock"] .stButton > button:hover {
        background: #DBEAFE !important;
        border-color: #3B82F6 !important;
        transform: translateY(-2px) !important;
    }
    
    /* 텍스트 입력 스타일링 */
    .stTextInput > div > div > input {
        border-radius: 15px !important;
        border: 2px solid #E5E7EB !important;
        padding: 15px 20px !important;
        font-size: 16px !important;
        text-align: center !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
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

# 현재 연금 미수령 중 페이지 - 단계별 질문 (자동 진행)
elif st.session_state.page == 'not_receiving':
    # 질문 데이터
    questions = {
        1: {
            "title": "연금 계산기 2",
            "question": "1. 월급 월소득을\n입력해주세요.",
            "type": "input",
            "placeholder": "월 소득을 입력하세요 (만원)"
        },
        2: {
            "title": "연금 계산기 3", 
            "question": "2. 국민연금\n가입기간을\n입력해주세요.",
            "type": "input",
            "placeholder": "국민연금 가입기간을 입력하세요 (년)"
        },
        3: {
            "title": "연금 계산기 29",
            "question": "1. 나이를\n입력해주세요.",
            "type": "input",
            "placeholder": "나이를 입력하세요"
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
            "type": "input",
            "placeholder": "가구원 수를 입력하세요"
        },
        6: {
            "title": "연금 계산기 23",
            "question": "5. 피부양자가\n있나요?",
            "type": "choice",
            "options": ["예", "아니오"]
        },
        7: {
            "title": "연금 계산기 24",
            "question": "6. 현재 보유한\n금융자산을\n입력해주세요.",
            "type": "input",
            "placeholder": "현재 보유 금융자산을 입력하세요 (만원)"
        },
        8: {
            "title": "연금 계산기 25",
            "question": "7. 월 수입하는\n연금 급여를\n입력해주세요.",
            "type": "input",
            "placeholder": "월 수입하는 연금 급여를 입력하세요 (만원)"
        },
        9: {
            "title": "연금 계산기 26",
            "question": "8. 월 평균\n지출비를\n입력해주세요.",
            "type": "input",
            "placeholder": "월 평균 지출비를 입력하세요 (만원)"
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
    <div style="text-align: center; font-size: 20px; font-weight: bold; margin: 50px 0; line-height: 1.5; color: #333;">
        {current_q['question']}
    </div>
    """, unsafe_allow_html=True)
    
    # 답변 입력/선택
    if current_q['type'] == 'input':
        # 입력 필드와 자동 진행
        answer = st.text_input("", placeholder=current_q['placeholder'], key=f"q{st.session_state.question_step}")
        
        # 입력값이 있으면 자동으로 다음 단계로
        if answer and answer.strip():
            # 1초 후 자동 진행을 위한 JavaScript
            st.markdown("""
            <script>
            setTimeout(function() {
                window.parent.document.querySelector('[data-testid="stApp"]').dispatchEvent(new Event('input'));
            }, 1000);
            </script>
            """, unsafe_allow_html=True)
            
            # 답변 저장하고 다음 단계로
            with st.spinner('다음 단계로 이동 중...'):
                import time
                time.sleep(1)  # 1초 대기
                
            st.session_state.answers[st.session_state.question_step] = answer
            if st.session_state.question_step < 10:
                st.session_state.question_step += 1
                st.rerun()
            else:
                st.session_state.page = 'result'
                st.rerun()
    
    elif current_q['type'] == 'choice':
        st.markdown('<div style="margin: 30px 0;"></div>', unsafe_allow_html=True)
        
        # 선택 버튼들
        for option in current_q['options']:
            if st.button(option, key=f"choice_{option}", use_container_width=True):
                # 선택하면 바로 다음 단계로
                st.session_state.answers[st.session_state.question_step] = option
                with st.spinner('다음 단계로 이동 중...'):
                    import time
                    time.sleep(0.5)  # 0.5초 대기
                    
                if st.session_state.question_step < 10:
                    st.session_state.question_step += 1
                    st.rerun()
                else:
                    st.session_state.page = 'result'
                    st.rerun()
    
    # 진행 상황 표시
    progress = st.session_state.question_step / 10
    st.progress(progress)
    st.markdown(f"""
    <div style='text-align: center; margin-top: 15px; font-size: 16px; color: #666;'>
        {st.session_state.question_step}/10 단계
    </div>
    """, unsafe_allow_html=True)
    
    # 상단에 작은 메인으로 돌아가기 버튼만
    st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)
    if st.button("← 메인으로", key="back_to_main"):
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

# 현재 연금 수령 중 페이지 - 단계별 질문 (자동 진행)
elif st.session_state.page == 'receiving':
    # 연금 수령 중 질문 데이터
    receiving_questions = {
        1: {
            "title": "연금 계산기 20",
            "question": "1. 나이를\n입력해주세요.",
            "type": "input",
            "placeholder": "나이를 입력하세요"
        },
        2: {
            "title": "연금 계산기 13", 
            "question": "2. 성별을\n선택해주세요.",
            "type": "choice",
            "options": ["남성", "여성"]
        },
        3: {
            "title": "연금 계산기 19",
            "question": "3. 가구원 수를\n입력해주세요.",
            "type": "input",
            "placeholder": "가구원 수를 입력하세요"
        },
        4: {
            "title": "연금 계산기 14",
            "question": "5. 피부양자가\n있나요?",
            "type": "choice",
            "options": ["예", "아니오"]
        },
        5: {
            "title": "연금 계산기 15",
            "question": "6. 현재 보유한\n금융자산을\n입력해주세요.",
            "type": "input",
            "placeholder": "현재 보유 금융자산을 입력하세요 (만원)"
        },
        6: {
            "title": "연금 계산기 16",
            "question": "7. 월 수령하는\n연금 급여를\n입력해주세요.",
            "type": "input",
            "placeholder": "월 수령하는 연금 급여를 입력하세요 (만원)"
        },
        7: {
            "title": "연금 계산기 17",
            "question": "8. 월 평균\n지출비를\n입력해주세요.",
            "type": "input",
            "placeholder": "월 평균 지출비를 입력하세요 (만원)"
        },
        8: {
            "title": "연금 계산기 11",
            "question": "9. 평균 월소득을\n입력해주세요.",
            "type": "input",
            "placeholder": "평균 월소득을 입력하세요 (만원)"
        },
        9: {
            "title": "연금 계산기 18",
            "question": "10. 투자 성향을\n선택해주세요.",
            "type": "choice",
            "options": ["안정형", "안정추구형", "위험중립형", "적극투자형"]
        }
    }
    
    current_q = receiving_questions[st.session_state.question_step]
    
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
    <div style="text-align: center; font-size: 20px; font-weight: bold; margin: 50px 0; line-height: 1.5; color: #333;">
        {current_q['question']}
    </div>
    """, unsafe_allow_html=True)
    
    # 답변 입력/선택
    if current_q['type'] == 'input':
        # 입력 필드와 자동 진행
        answer = st.text_input("", placeholder=current_q['placeholder'], key=f"receiving_q{st.session_state.question_step}")
        
        # 입력값이 있으면 자동으로 다음 단계로
        if answer and answer.strip():
            # 답변 저장하고 다음 단계로
            with st.spinner('다음 단계로 이동 중...'):
                import time
                time.sleep(1)  # 1초 대기
                
            st.session_state.answers[st.session_state.question_step] = answer
            if st.session_state.question_step < 9:
                st.session_state.question_step += 1
                st.rerun()
            else:
                st.session_state.page = 'receiving_result'
                st.rerun()
    
    elif current_q['type'] == 'choice':
        st.markdown('<div style="margin: 30px 0;"></div>', unsafe_allow_html=True)
        
        # 선택 버튼들
        for option in current_q['options']:
            if st.button(option, key=f"receiving_choice_{option}", use_container_width=True):
                # 선택하면 바로 다음 단계로
                st.session_state.answers[st.session_state.question_step] = option
                with st.spinner('다음 단계로 이동 중...'):
                    import time
                    time.sleep(0.5)  # 0.5초 대기
                    
                if st.session_state.question_step < 9:
                    st.session_state.question_step += 1
                    st.rerun()
                else:
                    st.session_state.page = 'receiving_result'
                    st.rerun()
    
    # 진행 상황 표시
    progress = st.session_state.question_step / 9
    st.progress(progress)
    st.markdown(f"""
    <div style='text-align: center; margin-top: 15px; font-size: 16px; color: #666;'>
        {st.session_state.question_step}/9 단계
    </div>
    """, unsafe_allow_html=True)
    
    # 상단에 작은 메인으로 돌아가기 버튼만
    st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)
    if st.button("← 메인으로", key="receiving_back_to_main"):
        st.session_state.page = 'main'
        st.session_state.question_step = 1
        st.session_state.answers = {}
        st.rerun()

# 연금 수령 중 결과 페이지
elif st.session_state.page == 'receiving_result':
    st.markdown("""
    <div class="main-header">
        <div class="kb-logo">
            <span class="kb-star">★</span><span class="kb-text">b KB</span>
        </div>
        <div class="title">연금 수령 현황 분석</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 현재 연금 수령 현황")
    
    # 입력된 답변 기반 분석
    if 6 in st.session_state.answers and 7 in st.session_state.answers:
        try:
            current_pension = float(st.session_state.answers[6])  # 월 수령 연금
            monthly_expense = float(st.session_state.answers[7])  # 월 지출
            surplus = current_pension - monthly_expense
            
            st.metric("현재 월 수령 연금", f"{current_pension:,.0f}만원")
            st.metric("월 평균 지출", f"{monthly_expense:,.0f}만원")
            
            if surplus > 0:
                st.success(f"🎯 월 잉여금: {surplus:,.0f}만원")
                st.info("💡 현재 연금으로 안정적인 생활이 가능합니다.")
            else:
                st.warning(f"⚠️ 월 부족금: {abs(surplus):,.0f}만원")
                st.info("💡 추가 수입원이나 지출 조정이 필요할 수 있습니다.")
            
            # 연간 분석
            annual_pension = current_pension * 12
            annual_expense = monthly_expense * 12
            st.markdown(f"""
            ### 📈 연간 분석
            - **연간 수령액**: {annual_pension:,.0f}만원
            - **연간 지출액**: {annual_expense:,.0f}만원
            - **연간 수지**: {(annual_pension - annual_expense):,.0f}만원
            """)
            
        except ValueError:
            st.error("입력값에 오류가 있습니다.")
    
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = 'main'
        st.session_state.question_step = 1
        st.session_state.answers = {}
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
