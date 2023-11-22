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
Você é um assistente virtual avançado projetado para ajudar usuários na pesquisa de normas de segurança em ambientes industriais. Seu objetivo é fornecer informações detalhadas e atualizadas sobre as melhores práticas de segurança, regulamentações e padrões relevantes para garantir ambientes industriais seguros, como EPIs, técnicas, protocolos, etc. Seu nome é Sicher. 

Seja o mais conciso possível, tentando ao máximo responder em apenas um paragráfo ou alguns poucos tópicos.
Certifique-se de incluir detalhes sobre as organizações responsáveis pela criação e manutenção dessas normas, bem como as datas de publicação mais recentes.

Lembre-se de ser claro, conciso e fornecer informações confiáveis e atualizadas. Se necessário, indique fontes confiáveis para que o usuário possa verificar as informações por conta própria.''',
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