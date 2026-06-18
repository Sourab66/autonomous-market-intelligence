from pydantic import BaseModel
from typing import List


class CompetitorReport(BaseModel):

    competitors: List[str]

    strengths: List[str]

    weaknesses: List[str]

    pricing_insights: List[str]