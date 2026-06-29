
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(result, filename="market_report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    content = []

    # ==================================================
    # COVER PAGE
    # ==================================================
    content.append(
        Paragraph(
            "Autonomous Market Intelligence Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 30))

    content.append(
        Paragraph(
            f"<b>Industry:</b> {result['industry']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Goal:</b> {result['goal']}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Generated using LangGraph Multi-Agent Workflow",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            f"<b>Market Research Time:</b> {result.get('market_timestamp','N/A')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Trend Research Time:</b> {result.get('trend_timestamp','N/A')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Competitor Research Time:</b> {result.get('competitor_timestamp','N/A')}",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================
    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"""
            This report analyzes the
            <b>{result['industry']}</b>
            market and provides strategic recommendations
            for achieving the business goal:

            <b>{result['goal']}</b>
            """,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Top Market Trends",
            styles["Heading2"]
        )
    )

    for item in result["market_report"]["trends"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    # ==================================================
    # MARKET ANALYSIS
    # ==================================================
    content.append(
        Paragraph(
            "Market Analysis",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            "Market Trends",
            styles["Heading2"]
        )
    )

    for item in result["market_report"]["trends"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Opportunities",
            styles["Heading2"]
        )
    )

    for item in result["market_report"]["opportunities"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Risks",
            styles["Heading2"]
        )
    )

    for item in result["market_report"]["risks"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Research Sources",
            styles["Heading2"]
        )
    )

    for source in result.get("market_sources", []):
        content.append(
            Paragraph(
                f"• <b>{source['title']}</b><br/>{source['url']}",
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    # ==================================================
    # TREND ANALYSIS
    # ==================================================
    content.append(
        Paragraph(
            "Industry Trend Analysis",
            styles["Heading1"]
        )
    )

    trend_text = result["trend_report"]
    trend_text = trend_text.replace("**", "")

    for i in range(1, 6):
        trend_text = trend_text.replace(
            f"{i}.",
            f"<br/><br/><b>Trend {i}</b><br/>"
        )

    content.append(
        Paragraph(
            trend_text,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Research Sources",
            styles["Heading2"]
        )
    )

    for source in result.get("trend_sources", []):
        content.append(
            Paragraph(
                f"• <b>{source['title']}</b><br/>{source['url']}",
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    # ==================================================
    # COMPETITOR ANALYSIS
    # ==================================================
    content.append(
        Paragraph(
            "Competitor Analysis",
            styles["Heading1"]
        )
    )

    competitors = result["competitor_report"]["competitors"]

    for company in competitors:
        content.append(
            Paragraph(
                f"<b>{company['name']}</b>",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Website:</b> {company['website']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Description:</b> {company['description']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Main Strength:</b> {company['strength']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Main Weakness:</b> {company['weakness']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Pricing:</b> {company['pricing']}",
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "Overall Market Strengths",
            styles["Heading2"]
        )
    )

    for item in result["competitor_report"]["strengths"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Overall Market Weaknesses",
            styles["Heading2"]
        )
    )

    for item in result["competitor_report"]["weaknesses"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Pricing Insights",
            styles["Heading2"]
        )
    )

    for item in result["competitor_report"]["pricing_insights"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Research Sources",
            styles["Heading2"]
        )
    )

    for source in result.get("competitor_sources", []):
        content.append(
            Paragraph(
                f"• <b>{source['title']}</b><br/>{source['url']}",
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    # ==================================================
    # STRATEGY
    # ==================================================
    content.append(
        Paragraph(
            "Strategic Recommendations",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            "Target Audience",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["strategy"]["target_audience"],
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Positioning",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["strategy"]["positioning"],
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Marketing Channels",
            styles["Heading2"]
        )
    )

    for item in result["strategy"]["marketing_channels"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    for item in result["strategy"]["recommendations"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    # ==================================================
    # WORKFLOW SUMMARY
    # ==================================================
    content.append(
        Paragraph(
            "Workflow Summary",
            styles["Heading1"]
        )
    )

    workflow = """
    User Input
    <br/><br/>
    ↓
    <br/><br/>
    Streamlit UI
    <br/><br/>
    ↓
    <br/><br/>
    LangGraph Workflow
    <br/><br/>
    ↓
    <br/><br/>
    Market Agent
    <br/><br/>
    ↓
    <br/><br/>
    Competitor Agent + Trend Agent (Parallel)
    <br/><br/>
    ↓
    <br/><br/>
    Strategy Agent
    <br/><br/>
    ↓
    <br/><br/>
    Human Approval
    <br/><br/>
    ↓
    <br/><br/>
    Content Agent
    <br/><br/>
    ↓
    <br/><br/>
    PDF Generation
    """

    content.append(
        Paragraph(
            workflow,
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ==================================================
    # WORKFLOW METRICS
    # ==================================================
    content.append(
        Paragraph(
            "Workflow Metrics",
            styles["Heading1"]
        )
    )

    agents = [
        (
            "Market Agent",
            result.get("market_execution_time", 0),
            result.get("market_tokens", {}),
            result.get("market_cost", 0)
        ),
        (
            "Trend Agent",
            result.get("trend_execution_time", 0),
            result.get("trend_tokens", {}),
            result.get("trend_cost", 0)
        ),
        (
            "Competitor Agent",
            result.get("competitor_execution_time", 0),
            result.get("competitor_tokens", {}),
            result.get("competitor_cost", 0)
        ),
        (
            "Strategy Agent",
            result.get("strategy_execution_time", 0),
            result.get("strategy_tokens", {}),
            result.get("strategy_cost", 0)
        )
    ]

    total_execution = 0
    total_tokens = 0
    total_cost = 0

    for name, exec_time, tokens, cost in agents:
        total_execution += exec_time
        total_cost += cost
        total_tokens += tokens.get("total_tokens", 0)

        content.append(
            Paragraph(
                f"<b>{name}</b>",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Execution Time : {exec_time} sec",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Input Tokens : {tokens.get('input_tokens',0)}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Output Tokens : {tokens.get('output_tokens',0)}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Total Tokens : {tokens.get('total_tokens',0)}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Estimated Cost : ${cost}",
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 12))

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "<b>Total Workflow Summary</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Total Execution Time : {round(total_execution,2)} sec",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Total Tokens : {total_tokens}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Estimated Total Cost : ${round(total_cost,6)}",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ==================================================
    # SYSTEM INFORMATION
    # ==================================================
    content.append(
        Paragraph(
            "System Information",
            styles["Heading1"]
        )
    )

    system_points = [
        "Framework : LangGraph",
        "LLM : Gemini 2.5 Flash",
        "External Search : Tavily Search API",
        "Memory : MemorySaver",
        "Human Approval : Enabled",
        "Parallel Execution : Enabled",
        "Structured Outputs : Pydantic Schemas",
        "Frontend : Streamlit",
        "PDF Engine : ReportLab",
        "",
        f"Market Research Timestamp : {result.get('market_timestamp','N/A')}",
        f"Trend Research Timestamp : {result.get('trend_timestamp','N/A')}",
        f"Competitor Research Timestamp : {result.get('competitor_timestamp','N/A')}"
    ]

    for point in system_points:
        content.append(
            Paragraph(
                f"• {point}",
                styles["BodyText"]
            )
        )

    doc.build(content)
    return filename

