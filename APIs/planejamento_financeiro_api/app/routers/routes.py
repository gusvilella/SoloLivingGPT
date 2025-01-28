
from fastapi import APIRouter, Query
from typing import Optional, List

router = APIRouter()

@router.get("/orcamento/")
def get_orcamento(
    salario: float,
    categorias: Optional[List[str]] = Query(None, description="Filtrar por categorias específicas")
):
    """
    Calcula e retorna o orçamento com base no salário.
    Permite filtrar por categorias específicas, como 'moradia' ou 'lazer'.
    """
    orcamento = {
        "moradia": salario * 0.4,
        "alimentacao": salario * 0.3,
        "lazer": salario * 0.2,
        "outros": salario * 0.1
    }
    if categorias:
        return {categoria: orcamento[categoria] for categoria in categorias if categoria in orcamento}
    return orcamento
