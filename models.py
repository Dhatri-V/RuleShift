from sqlalchemy import Column, ForeignKey, Integer, String

from database import Base


class PolicyFamily(Base):
    __tablename__ = "policy_families"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    issuing_authority = Column(String, nullable=False)
    audience = Column(String, nullable=False)


class PolicyVersion(Base):
    __tablename__ = "policy_versions"

    id = Column(Integer, primary_key=True)
    policy_family_id = Column(Integer, ForeignKey("policy_families.id"))
    version_label = Column(String, nullable=False)
    effective_date = Column(String, nullable=False)
    status = Column(String, nullable=False)
