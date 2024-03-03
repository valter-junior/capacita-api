from infrastructure.data.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, Query
from infrastructure.repositores.knowledge_repository import KnowledgeRepository


class KnowledgeService:
    def __init__(self, db: Session):
        self.repository = KnowledgeRepository(db)

    def get(self, knowledge_id):
        knowledge = self.repository.get(knowledge_id)
        if knowledge is None:
            return {"message": "Knowledge not found"}
        return knowledge

    def create(self, knowledge):
        return self.repository.create(knowledge)

 