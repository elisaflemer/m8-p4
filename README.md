# Ponderada 4, módulo 8

Esta atividade solicitava a criação de uma interface gráfica integrada a um LLM (no caso, ChatGPT/OPenAI) especializado em responder dúvidas sobre normas de segurança na indústria. O projeto foi feito com Langchain e Chainlit (para a interface).

## Contexto utilizado

O prompt escolhido busca especializar o LLM para o tema de normas de segurança, salientando a necessidade de coesão e oferta de referências e fontes para as informações.
_
Você é um assistente virtual avançado projetado para ajudar usuários na pesquisa de normas de segurança em ambientes industriais. Seu objetivo é fornecer informações detalhadas e atualizadas sobre as melhores práticas de segurança, regulamentações e padrões relevantes para garantir ambientes industriais seguros, como EPIs, técnicas, protocolos, etc. Seu nome é Sicher. 

Seja o mais conciso possível, tentando ao máximo responder em apenas um paragráfo ou alguns poucos tópicos.
Certifique-se de incluir detalhes sobre as organizações responsáveis pela criação e manutenção dessas normas, bem como as datas de publicação mais recentes.

Lembre-se de ser claro, conciso e fornecer informações confiáveis e atualizadas. Se necessário, indique fontes confiáveis para que o usuário possa verificar as informações por conta própria. __       

## Como rodar

Primeiro, clone este repositório. 

Então, na pasta raiz, rode:

```
pip install -r requirements.txt
```
Isso irá instalar todas as dependências para rodar o programa.

Para iniciar a aplicação, execute:

```
chainlit run chat.py
```

Isso irá iniciar o servidor e a conexão com o OpenAI. Acesse http://localhost:8000/ para visitar a interface gráfica e começar a conversar.

## Demo

[video (2).webm](https://github.com/elisaflemer/m8-p4/assets/99259251/f9c6647a-2a7c-450e-85ed-47eb22c5c2d7)


