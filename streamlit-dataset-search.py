import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="데이터세트 검색 서비스",
    page_icon="📊",
    layout="wide"
)

# CSS 스타일 적용
st.markdown("""
<style>
    .main-header {
        font-size: 26px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 20px;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: white;
        margin-bottom: 20px;
    }
    .metadata-group {
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }
    .metadata-label {
        font-weight: bold;
        color: #555;
        min-width: 120px;
        display: inline-block;
    }
    .metadata-value {
        color: #000;
    }
    .tag {
        background-color: #E5E7EB;
        padding: 5px 10px;
        border-radius: 15px;
        margin-right: 5px;
        font-size: 0.8em;
    }
    .highlight {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 2px 6px;
        border-radius: 4px;
    }
    .button-container {
        display: flex;
        gap: 10px;
        margin-top: 15px;
    }
    .last-update {
        color: #888;
        font-size: 0.8em;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# 검색 기능
st.markdown('<div class="main-header">데이터세트 검색 서비스</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    search_query = st.text_input("검색어를 입력하세요", value="문화재")
with col2:
    st.write("")
    st.write("")
    search_button = st.button("검색", use_container_width=True)

# 필터 섹션
st.markdown("### 검색 필터")
col1, col2, col3 = st.columns(3)
with col1:
    category = st.selectbox("카테고리", ["전체", "문화재", "관광", "경제", "교통", "환경", "기타"])
with col2:
    date_range = st.date_input("기간 선택", [datetime(2014, 1, 1), datetime(2023, 12, 31)])
with col3:
    sort_by = st.selectbox("정렬 기준", ["등록일 (최신순)", "등록일 (오래된 순)", "조회수", "다운로드 수"])

# 검색 결과 - 예시 데이터
if search_button or search_query:
    st.markdown("### 검색 결과")
    
    # 예시 데이터 (이미지에서 보이는 데이터 기반)
    dataset = {
        "title": "강원도 문화재통계",
        "id": "generated:3a474f61-aa0a-479b-8271-d0b5fc107042",
        "description": "도내 문화재(국가지정,지방지정 등) 통계",
        "doc_id": "3082811",
        "doc_type": "FILE",
        "reg_date": "2014-10-22",
        "update_date": "2020-07-30",
        "provider": "강원특별자치도",
        "department": "정보화정책과",
        "file_format": "csv",
        "category": "문화재목관 - 문화재",
        "tags": ["문화재", "국보", "보물"],
        "views": 1248,
        "downloads": 347,
        "quality_score": "100%",
        "relevance_score": "74.5%"
    }
    
    # 데이터세트 카드 형태로 표시
    with st.container():
        st.markdown(f"""
        <div class="card">
            <h2>{dataset["title"]} 
                <span class="highlight">{dataset["quality_score"]}</span>
                <span class="highlight" style="background-color: #2563EB;">유사도: {dataset["relevance_score"]}</span>
            </h2>
            <p>{dataset["description"]}</p>
            
            <div class="metadata-group">
                <span class="metadata-label">제공기관:</span>
                <span class="metadata-value">{dataset["provider"]}</span> |
                <span class="metadata-label">담당부서:</span>
                <span class="metadata-value">{dataset["department"]}</span>
            </div>
            
            <div class="metadata-group">
                <span class="metadata-label">등록일:</span>
                <span class="metadata-value">{dataset["reg_date"]}</span> |
                <span class="metadata-label">수정일:</span>
                <span class="metadata-value">{dataset["update_date"]}</span> |
                <span class="metadata-label">파일형식:</span>
                <span class="metadata-value">{dataset["file_format"].upper()}</span>
            </div>
            
            <div class="metadata-group">
                <span class="metadata-label">데이터 ID:</span>
                <span class="metadata-value">{dataset["id"]}</span>
            </div>
            
            <div class="metadata-group">
                <span class="metadata-label">분류체계:</span>
                <span class="metadata-value">{dataset["category"]}</span>
            </div>
            
            <div>
                {' '.join([f'<span class="tag">{tag}</span>' for tag in dataset["tags"]])}
            </div>
            
            <div class="button-container">
                <button style="background-color: #2563EB; color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer;">데이터 미리보기</button>
                <button style="background-color: #059669; color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer;">다운로드</button>
                <button style="background-color: #6B7280; color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer;">메타데이터 보기</button>
            </div>
            
            <p class="last-update">마지막 업데이트: 3년 전</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 사용 통계 시각화
    st.markdown("### 데이터세트 사용 통계")
    col1, col2 = st.columns(2)
    
    with col1:
        # 월별 다운로드 추이 (예시 데이터)
        months = ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', 
                 '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12']
        downloads = [23, 18, 35, 42, 28, 30, 47, 50, 38, 41, 53, 60]
        
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=months, y=downloads, mode='lines+markers', 
                                name='다운로드 수', line=dict(color='#2563EB', width=3)))
        fig1.update_layout(
            title='월별 다운로드 추이',
            xaxis_title='월',
            yaxis_title='다운로드 수',
            height=300
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # 연관 데이터세트 (예시)
        st.markdown("### 연관 데이터세트")
        
        related_datasets = [
            {"title": "강원도 국가지정문화재 현황", "similarity": "92%"},
            {"title": "강원도 관광지 문화재 방문객 통계", "similarity": "85%"},
            {"title": "강원도 무형문화재 보유자 현황", "similarity": "78%"}
        ]
        
        for ds in related_datasets:
            st.markdown(f"""
            <div style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between;">
                    <span>{ds["title"]}</span>
                    <span class="highlight" style="background-color: #2563EB;">유사도: {ds["similarity"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # 데이터 미리보기 (예시)
    with st.expander("데이터 미리보기"):
        # 예시 데이터
        df = pd.DataFrame({
            '지역': ['춘천시', '원주시', '강릉시', '속초시', '삼척시'],
            '국보': [3, 1, 2, 0, 0],
            '보물': [12, 8, 15, 5, 3],
            '사적': [4, 3, 6, 2, 1],
            '명승': [2, 1, 3, 2, 1],
            '천연기념물': [3, 2, 4, 1, 2]
        })
        st.dataframe(df, use_container_width=True)
