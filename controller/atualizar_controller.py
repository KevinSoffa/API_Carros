from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CriarDTO
from sqlmodel import select
from .router import router
from uuid import UUID



@router.put('/{carro_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CriarDTO)
async def atualizar(carro_id:UUID, carro_dto: CriarDTO, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CriarDTO).filter(CriarDTO.id == carro_id)
        result = await session.execute(query)
        carro_up: CriarDTO = result.scalar_one_or_none()

        if carro_up:
            carro_up.nome = carro_dto.nome
            carro_up.modelo = carro_dto.modelo
            carro_up.marca = carro_dto.marca
            carro_up.ano_modelo = carro_dto.ano_modelo
            carro_up.preco = carro_dto.preco

            await session.commit()

            return carro_up

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Id não encontrando!'
            )
