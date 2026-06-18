from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_campaign_pdf(
    result,
    filename="campaign_content.pdf"
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    campaign = result["campaign_content"]

    content.append(
        Paragraph(
            "Campaign Content Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "LinkedIn Post",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            campaign["linkedin_post"],
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Marketing Email",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            campaign["marketing_email"],
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Google Ad Copy",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            campaign["google_ad_copy"],
            styles["BodyText"]
        )
    )

    doc.build(content)

    return filename 
