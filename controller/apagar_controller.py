from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CriarDTO
from sqlmodel import select
from .router import router
from uuid import UUID
from fastapi import (
    Depends, 
    status, 
    HTTPException, 
    Response
)




@router.delete('/{carro_id}', status_code=status.HTTP_204_NO_CONTENT)
async def apagar(carro_id: UUID, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CriarDTO).filter(CriarDTO.id == carro_id)
        result = await session.execute(query)
        carro_del: CriarDTO = result.scalar_one_or_none()

        if carro_del:
            await session.delete(carro_del)
            await session.commit()

            return Response(
                status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Id não encontrando!'
            )