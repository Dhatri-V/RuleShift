from pydantic import BaseModel


class PolicyFamilyCreate(BaseModel):
    title: str
    domain: str
    issuing_authority: str
    audience: str


class PolicyVersionCreate(BaseModel):
    policy_family_id: int
    version_label: str
    effective_date: str
    status: str
