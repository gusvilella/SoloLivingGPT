
# SoloLivingGPT

## Estrutura do Projeto

```plaintext
SoloLivingGPT/
│
├── APIs/                             # Diretório principal para APIs
│   ├── planejamento_financeiro_api/  # API de Planejamento Financeiro
│   │   ├── _hidden/                  # Arquivos ocultos (ex.: .env)
│   │   ├── app/                      # Código principal da aplicação
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # Ponto de entrada da API
│   │   │   ├── models.py             # Definição de modelos e entidades
│   │   │   ├── routes.py             # Configuração de rotas da API
│   │   │   ├── services.py           # Lógica de negócios
│   │   │   ├── test_api.py           # Testes automatizados
│   │   │   └── database.py           # Configuração do banco de dados
│   │   ├── config/
│   │   │   ├── settings.py           # Configurações da aplicação
│   │   │   └── .gitignore            # Ignorar arquivos sensíveis
│   │   ├── banco.db                  # Banco de dados SQLite (se utilizado)
│   │   ├── requirements.txt          # Dependências do projeto Python
│   │   └── README.md                 # Documentação da API
│
├── docs/                             # Documentação geral do projeto
│   ├── Guia_Planejamento_Financeiro.md
│   └── Guia_Instalacao_Projeto.md
│
├── tests/                            # Testes gerais (separados por API ou funcionalidade)
│   ├── test_integracao.py
│   ├── test_unidade.py
│   └── fixtures.py                   # Dados de teste reutilizáveis
│
├── README.md                         # Documentação principal do projeto
├── .gitignore                        # Arquivos/pastas a serem ignorados pelo Git
└── LICENSE                           # Licença do projeto
```

---

## Atualizações Realizadas

1. **Renomeação do projeto**:
   - Nome alterado para **SoloLivingGPT** em toda a estrutura.

2. **Organização de APIs**:
   - Pasta `APIs` centraliza todas as APIs desenvolvidas, começando pela API de Planejamento Financeiro.

3. **Separação de Documentação**:
   - Diretório `docs` criado para armazenar guias e explicações do projeto.

4. **Inclusão de Testes**:
   - Diretório `tests` para centralizar testes de unidade e integração.

5. **Git Configurado**:
   - Adicionado `.gitignore` para ignorar arquivos sensíveis (como `.env` e `*.pyc`).
