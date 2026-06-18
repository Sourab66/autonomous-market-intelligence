from pydantic import BaseModel
from typing import List


class MarketReport(BaseModel):

    trends: List[str]

    opportunities: List[str]

    risks: List[str]