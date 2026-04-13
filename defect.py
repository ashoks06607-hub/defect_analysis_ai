import streamlit as st
from dotenv import load_dotenv
load_dotenv()


import google.generativeai as genai
from PIL import Image



st.set_page_config('DEFECT AI', page_icon='🤖',layout = 'wide')
st.title('AI POWERED DEFECT ANALYZER🤖🧠🇦🇮👾')
st.header(":blue[Prototype of automated structural defect analyzer using AI]🎯")
st.subheader(f":red[AI powered structural defect analysis using streamlit that allows users to upload the image of any structural defects and to get suggestions and recommandations for repair and rebuilt]🚀")

with st.expander('About the app:'):
    st.markdown(f''' This app helps to detect the defects like cracks, misallignments etc and provide
                - **Defect Detection**
                - **Recommendation**
                - **Suggestions fo improvements** ''')


import os

key = os.getenv('Google_api_key')

genai.configure(api_key=key)

input_image = st.file_uploader('Upload your file here ➤', type = ['png', 'jpeg', 'jpg'])

img =''

if input_image:
    img =Image.open(input_image).convert('RGB')
    st.image(img, caption='uploaded successfully ✅️')

prompt = f'''You are an quality engineer and civil engineer. you need to analyze the input and provide necessary details for the below given quets
in bullet points(max 3 points for each questions)

1. identify the type of defect in the image like cracks, misallingents that etc
2. what is the probility of damages caused by the defect detected in the image
3. what is the severity of the defect detected in the image
4. what are the possible causes of the defect detected in the image
5. what are the recommendations for repairing the defect detected in the image
6. what are the suggestions for improvement to prevent such defects in the future
7. what are the possible consequences if the defect is not repaired
8. what are the possible consequences if the defect is repaired
9. what are the possible consequences if the defect is repaired by a non-professional
10. what are the possible consequences if the defect is repaired by a professional'''

model = genai.GenerativeModel('models/gemini-2.5-flash-lite')

def generate_result(prompt, img):
    
    result = model.generate_content(f'''Using the given{prompt}
                           and given image{img}
                           analyze the image and give the
                           results as per the given prompt ''')
    return result.text

submit = st.button('Analyze the image 🎯')

if submit:
    with st.spinner('Results loading...👩🏻‍💻'):
        response = generate_result(prompt, img)
        
        st.markdown('## :green[result]')
        st.write(response)




