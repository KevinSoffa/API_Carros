from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CriarDTO
from .router import router
from uuid import uuid4
from fastapi import (
    status,
    Depends
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CriarDTO)
async def criar(carro_DTO: CriarDTO, db: AsyncSession = Depends(get_session)):
    novo_carro = CriarDTO(
        id=str(uuid4()),
        nome=carro_DTO.nome, 
        modelo=carro_DTO.modelo, 
        marca=carro_DTO.marca,
        ano_modelo=carro_DTO.ano_modelo,
        preco=carro_DTO.preco
    )
    db.add(novo_carro)
    await db.commit()

    return novo_carro
