from sqlalchemy.orm import Session
import uuid
from infrastructure.data import model, schemas


class KnowledgeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(model.Knowledge).all()

    def get(self, knowledgement_id: uuid.UUID):
        return (
            self.db.query(model.Knowledge)
            .filter(model.Knowledge.id == knowledgement_id)
            .first()
        )

    def create(
        self, knowledgement: schemas.KnowledgeBase
    ):

        db_knowledgement = model.Knowledge(
            id=uuid.uuid4().hex,
            title=knowledgement.title,
            description=knowledgement.description,
            knowledgement_type=knowledgement.knowledgement_type,
            knowledgement_text=knowledgement.knowledgement_text,
            url=knowledgement.url,
            is_active=knowledgement.is_active,
        )
        self.db.add(db_knowledgement)
        self.db.commit()
        self.db.refresh(db_knowledgement)
