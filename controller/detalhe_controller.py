from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CriarDTO
from sqlmodel import select
from .router import router
from typing import List
from uuid import UUID


@router.get('/{carro_id}', response_model=CriarDTO, status_code=status.HTTP_200_OK)
async def detalhe(carro_id:UUID, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CriarDTO).filter(CriarDTO.id == carro_id)
        result = await session.execute(query)
        carro: CriarDTO = result.scalar_one_or_none()

        if carro:
            return carro
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Id não encontrando!'
            )