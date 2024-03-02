from fastapi import APIRouter;
from infrastructure.data import schemas

from services import KnowledgeService

router = APIRouter()


router = APIRouter(
    prefix="/knowledge",
    tags=["knowledge"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_knowledge(knowledge: schemas.KnowledgementBase):
    return KnowledgeService.create_knowledge(knowledge)




