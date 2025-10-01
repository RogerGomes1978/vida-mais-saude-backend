Vida+ Saúde - Backend (Protótipo)

Este é um protótipo simples desenvolvido em Python com FastAPI, como parte da avaliação do curso de Análise e Desenvolvimento de Sistemas.
O objetivo é demonstrar conhecimentos básicos em Back-end e organização de projeto.

Tecnologias utilizadas

Python 3.x

FastAPI

Como executar o projeto

Clonar este repositório:
git clone https://github.com/RogerGomes1978/vida-mais-saude-backend.git
cd vida-mais-saude-backend

Criar e ativar ambiente virtual (opcional):
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

Instalar as dependências:
pip install fastapi uvicorn

Rodar o servidor:
uvicorn main1:app --reload

Acessar no navegador:
Documentação automática: http://127.0.0.1:8000/docs
Endpoint raiz: http://127.0.0.1:8000/

Endpoints disponíveis
GET / → Retorna mensagem de boas-vindas.
POST /pacientes → Cadastra paciente (nome, cpf).

Exemplo de requisição no Swagger UI:
{
  "nome": "João Silva",
  "cpf": "12345678900"
}

Autor
Rogerio Gomes
GitHub: RogerGomes1978
