
# API de Planejamento Financeiro

Uma API para auxiliar no planejamento financeiro pessoal.

## Endpoints

### 1. Raiz
- **GET** `/` - Mensagem de boas-vindas.

### 2. Planejamento Orçamentário
- **GET** `/orcamento/`
  - Parâmetros:
    - `salario` (float): Salário mensal.
  - Retorno:
    - Distribuição do salário em categorias: moradia, alimentação, lazer e outros.

## Como Rodar Localmente

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Acesse a documentação automática:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Testes
Para rodar os testes, use:
```bash
pytest app/tests
```
