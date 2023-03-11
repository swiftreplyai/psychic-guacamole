import streamlit as st
import openai

secrets = st.secrets["openai"]
openai.api_key = secrets["api_key"]

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

st.title("SwiftReply: Automatic Email Response Generation")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''SwiftReply is an AI-powered web application that uses natural language processing to analyze incoming emails and draft personalized and professional response emails. With SwiftReply, you can easily respond to emails that address the sender's concerns or questions, provide additional information or clarification, and maintain a professional tone. All you need to do is enter the body of the email and any additional insights you have, and then click "Generate Response". SwiftReply will analyze the email content and use its advanced algorithms to craft a response email that is personalized to the sender's needs and concerns.
       '''
    )

# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = secrets["openai"]["api_key"]

def generate_response_email(email_body, insight):
    '''Generates a response email based on the input email body and insight'''

    # Generate a default prompt that incorporates the email body and insight
    prompt = f"Your task is to craft a clear and comprehensive email response using only the information provided in the body of the email. This requires a thorough understanding of the email's context and purpose, as well as strong written communication skills to effectively convey your message. In your response, you should address any questions or concerns raised in the original email, while also providing any additional information or clarification that may be necessary. It's important to use a professional and courteous tone throughout your email, and to ensure that your message is both concise and easy to understand. Additionally, you should carefully proofread your email for any spelling or grammatical errors, and ensure that it meets any formatting or stylistic guidelines that may be required. Do not end it with a signoff.:\n\nEmail body: {email_body}\n\nInsight: {insight}\n\n"

    # Use the OpenAI API to generate a response email
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.9,
        top_p=0.9
    )

    response_text = response.choices[0].text.strip()
    return response_text

def main():
    '''Gets the user input and generates and displays the response email'''

    # Get user input for the email body
    email_body = st.text_area("Enter email body:")

    # Get user input for the insight
    insight = st.text_input("Enter insight:")

    # Generate and display the response email
    if st.button("Generate Response"):
        response_email = generate_response_email(email_body, insight)
        st.write(response_email)

# Call the main function
if __name__ == '__main__':
    main()

