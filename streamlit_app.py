import streamlit as st
import pandas as pd

# 간단한 데이터베이스
school_data = {
    "서울고등학교": [
        {"이름": "김민준", "학년": 1, "반": 3, "성적": 89},
        {"이름": "이서연", "학년": 2, "반": 1, "성적": 95}
    ],
    "부산여자고등학교": [
        {"이름": "박지훈", "학년": 3, "반": 2, "성적": 78},
        {"이름": "최윤아", "학년": 1, "반": 1, "성적": 88}
    ],
    "대구과학고등학교": [
        {"이름": "정수민", "학년": 2, "반": 2, "성적": 92}
    ]
}

# 챗봇 UI
st.title("🤖 학교 정보 챗봇")

st.markdown("학교나 학생에 대한 질문을 해보세요. 예: `서울고등학교 학생 알려줘`, `부산여자고등학교 평균 성적`")

# 사용자 입력 받기
user_input = st.text_input("💬 사용자 입력", "")

# 챗봇 응답 처리
if user_input:
    found = False
    for school, students in school_data.items():
        if school in user_input:
            df = pd.DataFrame(students)
            found = True
            if "학생" in user_input:
                st.markdown(f"**📋 {school} 학생 명단:**")
                st.dataframe(df)
            elif "평균" in user_input or "성적" in user_input:
                avg_score = df["성적"].mean()
                st.markdown(f"**📊 {school} 평균 성적: {avg_score:.2f}점**")
            else:
                st.markdown("🔍 학생 정보나 평균 성적 중 어떤 정보를 원하시는지 알려주세요.")
            break
    if not found:
        st.markdown("❓ 해당 학교 정보를 찾을 수 없습니다. 학교명을 정확히 입력해주세요.")
