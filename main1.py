from fastapi import FastAPI

app = FastAPI()

pacientes = []

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao Sistema Vida+ Saúde"}

@app.post("/pacientes")
def criar_paciente(nome: str, cpf: str):
    pacientes.append({"nome": nome, "cpf": cpf})
    return {"paciente": nome, "cpf": cpf, "status": "Cadastrado"}

@app.get("/pacientes")
def listar_pacientes():
    return pacientes
