
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import logging

# Configurar o logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Middleware para logging de requisições
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Recebendo requisição: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Resposta enviada: {response.status_code}")
    return response

# Middleware para autenticação básica (exemplo)
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if "Authorization" not in request.headers:
        logger.warning("Requisição não autorizada")
        raise HTTPException(status_code=401, detail="Autorização necessária")
    return await call_next(request)

@app.get("/")
def read_root():
    logger.info("Endpoint raiz acessado")
    return {"mensagem": "Bem-vindo ao Guia do Sobrevivente Solitário"}
