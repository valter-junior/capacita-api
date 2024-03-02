from sqlalchemy.orm import Session
import uuid
from infrastructure.data import model, schemas


class KnowledgeRepository:
    def get_knowledgements(self, db: Session):
        return db.query(model.Knowledgement).all()

    def get_knowledgement(self, db: Session, knowledgement_id: uuid.UUID):
        return (
            db.query(model.Knowledgement)
            .filter(model.Knowledgement.id == knowledgement_id)
            .first()
        )

    def create_knowledgement(
        self, db: Session, knowledgement: schemas.KnowledgementBase
    ):

        db_knowledgement = model.Knowledgement(
            id=uuid.uuid4().hex,
            title=knowledgement.title,
            description=knowledgement.description,
            knowledgement_type=knowledgement.knowledgement_type,
            knowledgement_text=knowledgement.knowledgement_text,
            url=knowledgement.url,
            is_active=knowledgement.is_active,
        )
        db.add(db_knowledgement)
        db.commit()
        db.refresh(db_knowledgement)
