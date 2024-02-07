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
    Always replace requested field with variable name from the payload.
    As handlebars expression always use given payload variable name.
    Always ignore variable values and use handlebars expression for requested fields.
    Use path in payload to substitute requested fields to path in cursive braces.
    If path is not in payload then dont need to substitute.
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

