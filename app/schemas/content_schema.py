from pydantic import BaseModel


class CampaignContent(BaseModel):

    linkedin_post: str

    marketing_email: str

    google_ad_copy: str