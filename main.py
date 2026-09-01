from fastapi import FastAPI, HTTPException

import models
from database import Base, engine, SessionLocal
from models import PolicyFamily, PolicyVersion
from schemas import PolicyFamilyCreate, PolicyVersionCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "RuleShift API is running"}


@app.post("/policy-families")
def create_policy_family(policy_family: PolicyFamilyCreate):
    db = SessionLocal()

    new_policy_family = PolicyFamily(
        title=policy_family.title,
        domain=policy_family.domain,
        issuing_authority=policy_family.issuing_authority,
        audience=policy_family.audience,
    )

    db.add(new_policy_family)
    db.commit()
    db.refresh(new_policy_family)
    db.close()

    return new_policy_family


@app.post("/policy-versions")
def create_policy_version(policy_version: PolicyVersionCreate):
    db = SessionLocal()

    new_policy_version = PolicyVersion(
        policy_family_id=policy_version.policy_family_id,
        version_label=policy_version.version_label,
        effective_date=policy_version.effective_date,
        status=policy_version.status,
    )

    db.add(new_policy_version)
    db.commit()
    db.refresh(new_policy_version)
    db.close()

    return new_policy_version


@app.get("/policy-versions")
def get_policy_versions():
    db = SessionLocal()
    policy_versions = db.query(PolicyVersion).all()
    db.close()

    return policy_versions


@app.get("/policy-families")
def get_policy_families():
    db = SessionLocal()
    policy_families = db.query(PolicyFamily).all()
    db.close()

    return policy_families


@app.get("/policy-families/{policy_id}")
def get_policy_family(policy_id: int):
    db = SessionLocal()
    policy_family = db.query(PolicyFamily).filter(PolicyFamily.id == policy_id).first()
    db.close()

    if policy_family is None:
        raise HTTPException(status_code=404, detail="Policy family not found")

    return policy_family
