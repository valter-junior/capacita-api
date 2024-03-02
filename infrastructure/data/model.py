from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

import datetime 

from infrastructure.data.database import Base

class Knowledge(Base):
    __tablename__ = 'knowledge'
    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    knowledgement_type = Column(String, nullable=False)
    knowledgement_text = Column(String, nullable=True)
    url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
