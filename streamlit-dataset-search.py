import streamlit as st
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="데이터세트 검색 서비스",
    page_icon="📊",
    layout="wide"
)

# CSS 스타일 적용
st.markdown("""
<style>
    .dataset-header {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .dataset-title {
        font-size: 22px;
        font-weight: bold;
        color: #2C3E50;
        margin-right: 10px;
    }
    .quality-badge {
        background-color: #4CAF50;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 14px;
        margin-right: 6px;
    }
    .relevance-badge {
        background-color: #3182CE;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 14px;
    }
    .dataset-description {
        font-size: 16px;
        color: #333;
        margin-bottom: 15px;
    }
    .metadata-row {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 6px;
    }
    .metadata-item {
        display: flex;
    }
    .metadata-label {
        font-weight: 500;
        color: #555;
        margin-right: 4px;
    }
    .metadata-value {
        color: #1A202C;
    }
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 8px;
    }
    .tag {
        background-color: #EDF2F7;
        color: #4A5568;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 13px;
    }
    .divider {
        height: 1px;
        background-color: #E2E8F0;
        margin: 12px 0;
    }
</style>
""", unsafe_allow_html=True)

# 검색 기능
st.title("데이터세트 검색 서비스")

search_query = st.text_input("검색어를 입력하세요", value="문화재")
search_button = st.button("검색", use_container_width=False)

# 필터 섹션
col1, col2, col3, col4 = st.columns(4)
with col1:
    category = st.selectbox("카테고리", ["전체", "문화재", "관광", "경제", "교통", "환경", "기타"])
with col2:
    provider = st.selectbox("제공기관", ["전체", "강원특별자치도", "서울특별시", "경기도", "기타"])
with col3:
    file_format = st.selectbox("파일형식", ["전체", "CSV", "JSON", "XML", "PDF", "기타"])
with col4:
    sort_by = st.selectbox("정렬 기준", ["관련도 순", "최신 등록일 순", "다운로드 많은 순"])

# 검색 결과 - 예시 데이터
if search_button or search_query:
    st.markdown("---")
    st.markdown("### 검색 결과")
    
    # 예시 데이터들 (여러 데이터세트 표시)
    datasets = [
        {
            "title": "강원도 문화재통계",
            "description": "강원도 문화재와 관련된 통계 데이터입니다.",
            "provider": "강원특별자치도",
            "department": "정보화정책과",
            "reg_date": "2024-10-25",
            "update_date": "2025-10-01",
            "file_format": "CSV",
            "category": "문화예술 - 문화재",
            "tags": ["문화재", "통계", "강원도"],
            "quality_score": "100%",
            "relevance_score": "74.5%"
        },
        {
            "title": "강원도 국가지정문화재 현황",
            "description": "강원도 내 위치한 국가지정문화재 현황 및 상세 정보입니다.",
            "provider": "강원특별자치도",
            "department": "문화유산과",
            "reg_date": "2024-08-15",
            "update_date": "2025-09-20",
            "file_format": "CSV",
            "category": "문화예술 - 문화재",
            "tags": ["문화재", "국보", "보물", "강원도"],
            "quality_score": "95%",
            "relevance_score": "92.3%"
        },
        {
            "title": "강원도 무형문화재 보유자 현황",
            "description": "강원도 무형문화재 보유자 및 전수 현황에 대한 정보입니다.",
            "provider": "강원특별자치도",
            "department": "문화유산과",
            "reg_date": "2024-09-05",
            "update_date": "2025-09-05",
            "file_format": "CSV",
            "category": "문화예술 - 문화재",
            "tags": ["무형문화재", "전통", "강원도"],
            "quality_score": "90%",
            "relevance_score": "82.1%"
        }
    ]
    
    # 데이터세트 카드 형태로 표시
    for dataset in datasets:
        st.markdown(f"""
        <div>
            <div class="dataset-header">
                <div class="dataset-title">{dataset["title"]}</div>
                <div class="quality-badge">{dataset["quality_score"]}</div>
                <div class="relevance-badge">유사도: {dataset["relevance_score"]}</div>
            </div>
            
            <div class="dataset-description">{dataset["description"]}</div>
            
            <div class="metadata-row">
                <div class="metadata-item">
                    <div class="metadata-label">제공기관:</div>
                    <div class="metadata-value">{dataset["provider"]}</div>
                </div>
                <div class="metadata-item">
                    <div class="metadata-label">담당부서:</div>
                    <div class="metadata-value">{dataset["department"]}</div>
                </div>
                <div class="metadata-item">
                    <div class="metadata-label">등록일:</div>
                    <div class="metadata-value">{dataset["reg_date"]}</div>
                </div>
                <div class="metadata-item">
                    <div class="metadata-label">수정일:</div>
                    <div class="metadata-value">{dataset["update_date"]}</div>
                </div>
            </div>
            
            <div class="metadata-row">
                <div class="metadata-item">
                    <div class="metadata-label">파일형식:</div>
                    <div class="metadata-value">{dataset["file_format"]}</div>
                </div>
                <div class="metadata-item">
                    <div class="metadata-label">분류체계:</div>
                    <div class="metadata-value">{dataset["category"]}</div>
                </div>
                <div class="metadata-item">
                    <div class="metadata-label">키워드:</div>
                    <div class="tag-container">
                        {' '.join([f'<span class="tag">{tag}</span>' for tag in dataset["tags"]])}
                    </div>
                </div>
            </div>
            <div class="divider"></div>
        </div>
        """, unsafe_allow_html=True)
