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
    
    /* 버튼 스타일 숨기기 */
    .stButton > button {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        width: 100% !important;
        height: auto !important;
    }
    
    .stButton > button:hover {
        background: transparent !important;
        border: none !important;
    }
    
    .stButton > button:focus {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* 커스텀 버튼 스타일 */
    .custom-button {
        width: 100%;
        padding: 25px 20px;
        margin: 15px 0;
        border: none;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        line-height: 1.3;
    }
    
    .yellow-button {
        background: #FFE4B5;
        color: #8B4513;
    }
    
    .blue-button {
        background: #B8D4F0;
        color: #2C5282;
    }
    
    .green-button {
        background: #C6F6D5;
        color: #22543D;
        width: 48%;
        display: inline-block;
        margin: 10px 1%;
        font-size: 16px;
        padding: 20px 10px;
    }
    
    .pink-button {
        background: #FED7E2;
        color: #97266D;
        width: 48%;
        display: inline-block;
        margin: 10px 1%;
        font-size: 16px;
        padding: 20px 10px;
    }
    
    .custom-button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .button-row {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin-top: 20px;
    }
    
    .button-row .custom-button {
        flex: 1;
        margin: 0;
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

# 메인 페이지 - HTML 버튼으로 원본과 동일한 디자인
if st.session_state.page == 'main':
    # 현재 연금 미수령 중 버튼
    st.markdown("""
    <div class="custom-button yellow-button" onclick="document.querySelector('[data-testid=\'stButton\']:nth-of-type(1) button').click()">
        현재 연금<br>미수령 중
    </div>
    """, unsafe_allow_html=True)
    if st.button("", key="pension_not_receiving"):
        st.session_state.page = 'not_receiving'
        st.rerun()
    
    # 현재 연금 수령 중 버튼
    st.markdown("""
    <div class="custom-button blue-button" onclick="document.querySelector('[data-testid=\'stButton\']:nth-of-type(2) button').click()">
        현재 연금<br>수령 중
    </div>
    """, unsafe_allow_html=True)
    if st.button("", key="pension_receiving"):
        st.session_state.page = 'receiving'
        st.rerun()
    
    # 하단 버튼들
    st.markdown("""
    <div class="button-row">
        <div class="custom-button green-button" onclick="document.querySelector('[data-testid=\'stButton\']:nth-of-type(3) button').click()">
            상품<br>정보
        </div>
        <div class="custom-button pink-button" onclick="document.querySelector('[data-testid=\'stButton\']:nth-of-type(4) button').click()">
            전화<br>상담
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("", key="product_info"):
            st.session_state.page = 'product_info'
            st.rerun()
    
    with col2:
        if st.button("", key="phone_consultation"):
            st.session_state.page = 'phone_consultation'
            st.rerun()

# 현재 연금 미수령 중 페이지
elif st.session_state.page == 'not_receiving':
    st.markdown("### 📊 현재 연금 미수령 중")
    st.write("연금 수령 예상 계산을 도와드립니다.")
    
    # 기본 정보 입력
    age = st.number_input("현재 나이", min_value=20, max_value=100, value=45)
    monthly_income = st.number_input("월 소득 (만원)", min_value=0, value=300)
    career_years = st.number_input("가입 예상 기간 (년)", min_value=1, max_value=50, value=20)
    
    if st.button("계산하기"):
        # 간단한 연금 계산 (실제 계산식과는 다를 수 있음)
        estimated_pension = (monthly_income * 10000 * 0.015 * career_years) / 12
        st.success(f"예상 월 연금액: {estimated_pension:,.0f}원")
    
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = 'main'
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
