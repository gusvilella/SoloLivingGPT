from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_NAME = os.getenv("DB_NAME")

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "bem-vindo ao guia do sobrevivente solitário"}

@app.get("/orcamento/")
def get_orcamento(salario: float):
    return {
        "moradia": salario * 0.4,
        "alimentacao": salario * 0.3,
        "lazer": salario * 0.2,
        "outros": salario * 0.1
    }
