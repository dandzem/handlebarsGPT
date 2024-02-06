import streamlit as st
from utils import process_request

col1, col2 = st.columns([1, 2])

if 'api_key' not in st.session_state:
    st.session_state['api_key'] = ''

if 'model_name' not in st.session_state:
    st.session_state['model_name'] = ''

with st.sidebar:
    api_key = st.text_input("API Key")
    model_name = st.selectbox("Model Name", ['gpt-3.5-turbo-0125', 'gpt-4-0125-preview'])
    if model_name:
        st.session_state['model_name'] = model_name
    if api_key:
        st.session_state['api_key'] = api_key
    else:
        st.write("Please enter your API Key")

if st.session_state['api_key']:
    payload = col1.text_area("Please input your payload here", height=600)
    request = col1.text_area("Please input your request here", height=600)

    if payload and request:
        if st.button("Submit", type='primary'):
            generated_html = process_request(payload,
                                             request,
                                             api_key=st.session_state['api_key'],
                                             model_name=st.session_state['model_name'])
            if generated_html:
                col2.code(generated_html)
            else:
                col2.write('Here will be shown generated html')
else:
    st.info("Please enter your API Key before proceeding")
