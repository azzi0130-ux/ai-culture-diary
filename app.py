import streamlit as st
import openai

# --- 1. AI 호출을 위한 핵심 함수 ---
def generate_diary_and_image(country, environment, api_key):
    openai.api_key = api_key
    
    # 1-1. GPT-4로 일기 생성
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

    # 1-2. DALL-E 3로 그림 생성
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

# --- 2. 웹페이지 화면 구성 ---

st.title('AI 세계 문화 탐험 일기')

# 여기에 본인의 실제 API 키를 큰따옴표 안에 넣으세요!!!
# 이 방법은 보안에 완벽하지는 않지만, 지금은 '작동'이 가장 중요합니다.
my_api_key = "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"

country = st.selproj-JraLxmTiLZs8eQLlEaja9BMJXWwwj6I6tkuILgCZi0XBlZykKaMtFB3r1lgVGA9tEyk2ITNpGwT3BlbkFJgKfQXc3rBCXFT2LJb9YFhV01yKfX5qcAS9Hd0I4jwoDsnKBNx94oDQQ4Fs2PTEdkFRAxY4LiIAectbox('나라를 선택하세요', ['이집트', '페루', '브라질', '몽골'])
environment = st.selectbox('자연환경을 선택하세요', ['사막', '고산지대', '열대 우림', '초원'])

if st.button('일기 생성하기'):
    with st.spinner('AI가 열심히 일기를 쓰고 그림을 그리는 중입니다... 잠시만 기다려주세요!'):
        diary, image = generate_diary_and_image(country, environment, my_api_key)
        
        st.subheader('AI가 만든 그림일기')
        st.image(image)
        st.write(diary)