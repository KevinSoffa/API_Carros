from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CriarDTO
from sqlmodel import select
from fastapi import Depends
from .router import router
from typing import List


@router.get('/', response_model=List[CriarDTO])
async def listagem(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CriarDTO)
        result = await session.execute(query)
        cursos: List[CriarDTO] = result.scalars().all()

        return cursos
