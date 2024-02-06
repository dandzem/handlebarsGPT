from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate


def process_request(request, payload, api_key, model_name='gpt-3.5-turbo-0125'):
    """
    add to the template values and generate with model string of Json
    :param api_key: api key for openai model
    :param payload: json payload
    :param request: requested html structure
    :return:
    """
    template = """
    You are professional handlebar template builder. Based on payload and request create proper html template.
    You should output only pure html without any additional comments.
    Payload: \n
    {payload}
    \n
    Create html for following request:
    {request}
    \n
    Output html: 
    """
    llm = ChatOpenAI(openai_api_key=api_key, model_name=model_name)
    prompt = ChatPromptTemplate.from_template(template=template)
    chain = (
            prompt
            | llm
            | StrOutputParser()
    )
    resp = chain.invoke({"payload": payload, "request": request})
    return resp

