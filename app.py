import streamlit as st
import openai

# --- 1. AI 함수 (비밀 금고에서 읽어옵니다) ---
def generate_diary_and_image(country, environment):
    # 이 마법의 한 줄은 Streamlit에게 방금 만든 '비밀 금고'에서 키를 가져오라고 지시합니다.
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    
    # ... (함수의 나머지 부분은 이전과 정확히 동일합니다) ...
    diary_prompt = (
        f"너는 {country}의 {environment}에 사는 창의적인 어린이야. "
        f"이 조건에 맞는 일기를 한국어로 10문장 이내로 써줘. "
        f"어린이의 시선과 감정이 잘 드러나게 해줘."
    )    
    diary_response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "너는 창의적인 어린이 일기 작가야."},
            {"role": "user", "content": diary_prompt}
        ],
        max_tokens=500,
        temperature=0.8
    )
    diary_text = diary_response.choices[0].message.content.strip()

    image_prompt = (
        f"{country}의 {environment}에서 사는 어린이의 일기 내용을 바탕으로 한, 따뜻하고 감성적인 그림을 그려줘. "
        f"일러스트레이션 스타일로."
    )    
    image_response = openai.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = image_response.data[0].url

    return diary_text, image_url

# --- 2. 웹페이지 레이아웃 ---

st.title('AI 세계 문화 탐험 일기')

country = st.selectbox('나라를 선택하세요', ['이집트', '페루', '브라질', '몽골'])
environment = st.selectbox('자연환경을 선택하세요', ['사막', '고산지대', '열대 우림', '초원'])

if st.button('일기 생성하기'):
    with st.spinner('AI가 열심히 일기를 쓰고 그림을 그리는 중입니다... 잠시만 기다려주세요!'):
        
        diary, image = generate_diary_and_image(country, environment)
        
        st.subheader('AI가 만든 그림일기')
        st.image(image)
        st.write(diary)