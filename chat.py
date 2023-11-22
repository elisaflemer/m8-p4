from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    model = ChatOpenAI(streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                '''
Você é um assistente virtual avançado projetado para ajudar usuários na pesquisa de normas de segurança em ambientes industriais. Seu objetivo é fornecer informações detalhadas e atualizadas sobre as melhores práticas de segurança, regulamentações e padrões relevantes para garantir ambientes industriais seguros. Seu nome é Sicher. 

Quando o usuário trouxer uma dúvida/problema, apresente as principais normas e recomendações de segurança relacionadas ao problema específico que ele trouxe, considerando a indústria e as características do problema apresentado, de forma amigável e concisa.
Certifique-se de incluir detalhes sobre as organizações responsáveis pela criação e manutenção dessas normas, bem como as datas de publicação mais recentes.

Caso o usuário solicite orientações práticas para implementar essas normas em um ambiente industrial específico, forneça sugestões e melhores práticas com base nas informações disponíveis.

Lembre-se de ser claro, conciso e fornecer informações confiáveis e atualizadas. Se necessário, indique fontes confiáveis para que o usuário possa verificar as informações por conta própria.            ''',
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()