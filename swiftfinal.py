import streamlit as st
import openai

secrets = st.secrets["openai"]
openai.api_key = secrets["api_key"]

st.title("SwiftReply: Automatic Email Response Generation")
st.markdown("Enter the email body and any additional insights you have, then click 'Generate Response'.")

model_engine = "text-davinci-003"
openai.api_key = secrets["api_key"]

def generate_response_email(email_body, insight, tone):
    if tone == "formal":
        prompt = f"Your task is to compose a clear and professional email response. Carefully consider the information within the email body and integrate any relevant user insights. The response should address the sender's concerns or inquiries, provide any necessary explanations, and suggest appropriate next steps or actions. Additionally, you should carefully proofread your email for any spelling or grammatical errors, and ensure that it meets any formatting or stylistic guidelines that may be required. Do not end it with a signoff.:\n\nEmail body: {email_body}\n\nInsight: {insight}\n\n"
    elif tone == "casual":
        prompt = f"Your task is to compose a friendly and informal email response. Carefully consider the information within the email body and integrate any relevant user insights. The response should address the sender's concerns or inquiries, provide any necessary explanations, and suggest appropriate next steps or actions. Additionally, you should carefully proofread your email for any spelling or grammatical errors, and ensure that it meets any formatting or stylistic guidelines that may be required. Do not end it with a signoff.:\n\nEmail body: {email_body}\n\nInsight: {insight}\n\n"
    elif tone == "friendly":
        prompt = f"Your task is to compose a warm and engaging email response. Carefully consider the information within the email body and integrate any relevant user insights. The response should address the sender's concerns or inquiries, provide any necessary explanations, and suggest appropriate next steps or actions. Additionally, you should carefully proofread your email for any spelling or grammatical errors, and ensure that it meets any formatting or stylistic guidelines that may be required. Do not end it with a signoff.:\n\nEmail body: {email_body}\n\nInsight: {insight}\n\n"
    elif tone == "professional":
        prompt = f"Your task is to compose a clear and comprehensive email response that is warm and relatable, avoiding AI jargon. Carefully consider the information within the email body and integrate any relevant user insights. The response should address the sender's concerns or inquiries, provide any necessary explanations, and suggest appropriate next steps or actions. Aim to create a response that feels personal and engaging, ensuring its effectiveness in communication. Additionally, you should carefully proofread your email for any spelling or grammatical errors, and ensure that it meets any formatting or stylistic guidelines that may be required. Do not end it with a signoff.:\n\nEmail body: {email_body}\n\nInsight: {insight}\n\n"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.9,
        top_p=0.9
    )

    return response.choices[0].text.strip()

def main():
    email_body = st.text_area("Enter email body:", height=200)
    insight = st.text_input("Enter insight:")
    tone = st.selectbox("Select tone of voice:", ["formal", "casual", "friendly", "professional"])

if st.button("Generate Response"):
        response_email = generate_response_email(email_body, insight, tone)
        st.write(response_email)

if __name__ == '__main__':
    st.sidebar.header("Instructions")
    st.sidebar.info(
        '''SwiftReply is an AI-powered web application that uses natural language processing to analyze incoming emails and draft personalized and professional response emails. With SwiftReply, you can easily respond to emails that address the sender's concerns or questions, provide additional information or clarification, and maintain a professional tone. All you need to do is enter the body of the email and any additional insights you have, and then click "Generate Response". SwiftReply will analyze the email content and use its advanced algorithms to craft a response email that is personalized to the sender's needs and concerns.
           '''
    )
    main()
