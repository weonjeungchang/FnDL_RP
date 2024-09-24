import streamlit as st
from openai import OpenAI  
  
client = OpenAI()

# Streamlit 애플리케이션 설정
st.set_page_config(page_title="FnDL GPT-4o Chatbot", page_icon="💯")

# 애플리케이션 헤더
# st.title("GPT-4o 기반 챗봇")
st.header("[FnDataLab] 궁금한 점 물어보세요.", divider='rainbow')
st.subheader("GPT-4o 기반 챗봇")

st.write("질문 예시 :")
st.info("2023년10월29일(부터 11월7일까지의) 대한민국 주식시장과 원달러 환율에 대해 알려주세요")
st.caption("금지어 : 킥보드, 갤럭시탭, 음주운전")

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:", "")

# 버튼을 누를 때만 응답을 처리하도록 설정
if st.button("답변 받기"):
    if user_input:
        with st.spinner("GPT-4o가 생각 중입니다..."):
            # OpenAI API를 사용하여 GPT-4 모델과 상호작용
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input},
                    ]
                )
                # 응답 출력
                # answer = response['choices'][0]['message']['content']
                answer = response.choices[0].message.content
                st.markdown(answer)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 입력해 주세요!")
