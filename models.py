from sqlalchemy import Column, Integer, String

from database import Base


class PolicyFamily(Base):
    __tablename__ = "policy_families"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    issuing_authority = Column(String, nullable=False)
    audience = Column(String, nullable=False)
