import streamlit as st
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="데이터세트 검색 서비스",
    page_icon="📊",
    layout="wide"
)

# CSS 스타일 적용 (간소화)
st.markdown("""
<style>
    .dataset-container {
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 15px;
        background-color: white;
    }
    .dataset-header {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .dataset-title {
        font-size: 20px;
        font-weight: bold;
        margin-right: 10px;
    }
    .badge {
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 14px;
        margin-right: a6px;
    }
    .badge-green {
        background-color: #4CAF50;
        color: white;
    }
    .badge-blue {
        background-color: #3182CE;
        color: white;
    }
    .tag {
        background-color: #f1f1f1;
        padding: 2px 8px;
        border-radius: 10px;
        margin-right: 5px;
        font-size: 12px;
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
    
    # 예시 데이터 (이미지에서 보이는 데이터 기반)
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
        }
    ]
    
    # 데이터세트 표시 (Streamlit 기본 요소 사용)
    for dataset in datasets:
        with st.container():
            # 제목 줄 (제목 + 품질점수 + 유사도)
            col1, col2, col3 = st.columns([6, 1, 2])
            with col1:
                st.markdown(f"### {dataset['title']}")
            with col2:
                st.markdown(f"<div style='background-color: #4CAF50; color: white; padding: 4px 8px; border-radius: 4px; text-align: center; font-weight: bold;'>{dataset['quality_score']}</div>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<div style='background-color: #3182CE; color: white; padding: 4px 8px; border-radius: 4px; text-align: center; font-weight: bold;'>유사도: {dataset['relevance_score']}</div>", unsafe_allow_html=True)
            
            # 설명
            st.markdown(f"{dataset['description']}")
            
            # 메타데이터 첫 줄
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f"**제공기관:** {dataset['provider']}")
            with col2:
                st.markdown(f"**담당부서:** {dataset['department']}")
            with col3:
                st.markdown(f"**등록일:** {dataset['reg_date']}")
            with col4:
                st.markdown(f"**수정일:** {dataset['update_date']}")
            
            # 메타데이터 둘째 줄
            col1, col2, col3 = st.columns([1, 2, 3])
            with col1:
                st.markdown(f"**파일형식:** {dataset['file_format']}")
            with col2:
                st.markdown(f"**분류체계:** {dataset['category']}")
            with col3:
                tag_html = " ".join([f'<span style="background-color: #f1f1f1; padding: 2px 8px; border-radius: 10px; margin-right: 5px; font-size: 12px;">{tag}</span>' for tag in dataset['tags']])
                st.markdown(f"**키워드:** {tag_html}", unsafe_allow_html=True)
            
            st.markdown("---")
