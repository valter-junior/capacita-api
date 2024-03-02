from infrastructure.data.database import get_db
from fastapi import Depends, Query
from infrastructure.repositores.knowledge_repository import KnowledgeRepository


class KnowledgeService:
    def __init__(self, knowledge: KnowledgeRepository):
        self.knowledge = knowledge

    def get_knowledge(self, knowledge_id):
        return self.knowledge.get(knowledge_id)

    def create_knowledge(self, knowledge):
        return self.knowledge.create_knowledgement(knowledge)

 