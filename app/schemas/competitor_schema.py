from pydantic import BaseModel
from typing import List


class Competitor(BaseModel):

    name: str

    website: str

    description: str

    strength: str

    weakness: str

    pricing: str


class CompetitorReport(BaseModel):

    competitors: List[Competitor]

    strengths: List[str]

    weaknesses: List[str]

    pricing_insights: List[str]