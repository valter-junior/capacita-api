from pydantic import BaseModel

class KnowledgeBase(BaseModel):
    title: str
    description: str
    knowledgement_type: str
    knowledgement_text: str
    url: str
    is_active: bool


    class Config:
        orm_mode = True

