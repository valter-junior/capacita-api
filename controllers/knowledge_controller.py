from fastapi import APIRouter;
from infrastructure.data import schemas
import uuid
from infrastructure.data.database import get_db
from fastapi import Depends


from services.knowledge_service import KnowledgeService

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

@router.post("/")
async def create_knowledge(knowledge: schemas.KnowledgeBase, db: get_db = Depends()):
    return KnowledgeService(db).create(knowledge)

@router.get("/{knowledge_id}")
async def get_knowledge(knowledge_id: uuid.UUID, db: get_db = Depends()):
    return KnowledgeService(db).get(knowledge_id)
