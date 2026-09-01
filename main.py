from fastapi import FastAPI

import models
from database import Base, engine, SessionLocal
from models import PolicyFamily
from schemas import PolicyFamilyCreate

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


@app.get("/policy-families")
def get_policy_families():
    db = SessionLocal()
    policy_families = db.query(PolicyFamily).all()
    db.close()

    return policy_families
