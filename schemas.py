from pydantic import BaseModel


class PolicyFamilyCreate(BaseModel):
    title: str
    domain: str
    issuing_authority: str
    audience: str
