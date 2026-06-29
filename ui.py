import streamlit as st
import uuid

from app.graph.builder import graph
from app.content_only import content_graph

from app.report_pdf_generator import create_pdf
from app.campaign_pdf_generator import create_campaign_pdf
from app.json_export import create_json

st.set_page_config(
    page_title="Autonomous Market Intelligence",
    layout="wide"
)

st.title("Autonomous Market Intelligence")

industry = st.text_input(
    "Industry",
    "AI SaaS"
)

goal = st.text_input(
    "Goal",
    "Increase Signups"
)

if st.button("Generate Strategy"):

    st.session_state["thread_id"] = str(uuid.uuid4())

    with st.spinner("Running Multi-Agent Workflow..."):

        config = {
            "configurable": {
                "thread_id": st.session_state["thread_id"]
            }
        }

        result = graph.invoke(
            {
                "industry": industry,
                "goal": goal
            },
            config=config
        )

        st.session_state["result"] = result
        st.session_state["content_generated"] = False

if "result" in st.session_state:

    result = st.session_state["result"]
    st.write(result.keys())

    st.success("Research Completed")

    st.caption(
        f"Session ID: {st.session_state['thread_id']}"
    )

    # ===================================================
    # WORKFLOW METRICS
    # ===================================================

    st.header("Workflow Metrics")

    market_time = result.get("market_execution_time", 0)
    trend_time = result.get("trend_execution_time", 0)
    competitor_time = result.get("competitor_execution_time", 0)
    strategy_time = result.get("strategy_execution_time", 0)

    market_tokens = result.get("market_tokens", {})
    trend_tokens = result.get("trend_tokens", {})
    competitor_tokens = result.get("competitor_tokens", {})
    strategy_tokens = result.get("strategy_tokens", {})

    market_cost = result.get("market_cost", 0)
    trend_cost = result.get("trend_cost", 0)
    competitor_cost = result.get("competitor_cost", 0)
    strategy_cost = result.get("strategy_cost", 0)

    total_time = (
        market_time
        + trend_time
        + competitor_time
        + strategy_time
    )

    total_tokens = (
        market_tokens.get("total_tokens", 0)
        + trend_tokens.get("total_tokens", 0)
        + competitor_tokens.get("total_tokens", 0)
        + strategy_tokens.get("total_tokens", 0)
    )

    total_cost = (
        market_cost
        + trend_cost
        + competitor_cost
        + strategy_cost
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Workflow Time",
        f"{total_time:.2f} sec"
    )

    c2.metric(
        "Total Tokens",
        total_tokens
    )

    c3.metric(
        "Estimated Cost",
        f"${total_cost:.6f}"
    )

    with st.expander("Per Agent Metrics"):

        st.json({

            "Market Agent": {

                "Execution Time": market_time,

                "Tokens": market_tokens,

                "Cost": market_cost

            },

            "Trend Agent": {

                "Execution Time": trend_time,

                "Tokens": trend_tokens,

                "Cost": trend_cost

            },

            "Competitor Agent": {

                "Execution Time": competitor_time,

                "Tokens": competitor_tokens,

                "Cost": competitor_cost

            },

            "Strategy Agent": {

                "Execution Time": strategy_time,

                "Tokens": strategy_tokens,

                "Cost": strategy_cost

            }

        })

    # ===================================================
    # MARKET REPORT
    # ===================================================

    st.header("Market Report")

    st.json(result["market_report"])

    st.caption(
        f"Research collected: {result.get('market_timestamp','N/A')}"
    )

    with st.expander("Market Sources"):

        for source in result.get("market_sources", []):

            st.markdown(
                f"**{source['title']}**"
            )

            st.write(source["url"])

    # ===================================================
    # TREND REPORT
    # ===================================================

    st.header("Trend Report")

    st.write(result["trend_report"])

    st.caption(
        f"Research collected: {result.get('trend_timestamp','N/A')}"
    )

    with st.expander("Trend Sources"):

        for source in result.get("trend_sources", []):

            st.markdown(
                f"**{source['title']}**"
            )

            st.write(source["url"])

                # ===================================================
    # COMPETITOR REPORT
    # ===================================================

    st.header("Competitor Report")

    competitors = result["competitor_report"]["competitors"]

    for company in competitors:

        st.subheader(company["name"])

        st.write(
            f"**Website:** {company['website']}"
        )

        st.write(
            f"**Description:** {company['description']}"
        )

        st.write(
            f"**Strength:** {company['strength']}"
        )

        st.write(
            f"**Weakness:** {company['weakness']}"
        )

        st.write(
            f"**Pricing:** {company['pricing']}"
        )

        st.divider()

    st.subheader("Overall Strengths")

    st.write(
        result["competitor_report"]["strengths"]
    )

    st.subheader("Overall Weaknesses")

    st.write(
        result["competitor_report"]["weaknesses"]
    )

    st.subheader("Pricing Insights")

    st.write(
        result["competitor_report"]["pricing_insights"]
    )

    st.caption(
        f"Research collected: {result.get('competitor_timestamp','N/A')}"
    )

    with st.expander("Competitor Sources"):

        for source in result.get("competitor_sources", []):

            st.markdown(
                f"**{source['title']}**"
            )

            st.write(source["url"])

    # ===================================================
    # STRATEGY
    # ===================================================

    st.header("Strategy")

    st.json(result["strategy"])

    approval = st.radio(

        "Approve Strategy?",

        [
            "No",
            "Yes"
        ]

    )

    if approval == "Yes":

        st.success("Strategy Approved")

        if not st.session_state.get(
            "content_generated",
            False
        ):

            with st.spinner("Generating Campaign Content..."):

                content_result = content_graph.invoke(

                    {
                        "strategy": result["strategy"]
                    }

                )

                st.session_state["campaign_content"] = content_result["campaign_content"]

                st.session_state["content_execution_time"] = content_result["content_execution_time"]

                st.session_state["content_tokens"] = content_result["content_tokens"]

                st.session_state["content_cost"] = content_result["content_cost"]

                st.session_state["content_generated"] = True

        campaign = st.session_state["campaign_content"]

        st.header("Campaign Metrics")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Execution Time",
            f"{st.session_state['content_execution_time']:.2f} sec"
        )

        c2.metric(
            "Total Tokens",
            st.session_state["content_tokens"].get(
                "total_tokens",
                0
            )
        )

        c3.metric(
            "Estimated Cost",
            f"${st.session_state['content_cost']:.6f}"
        )

        with st.expander("Content Agent Details"):

            st.json({

                "Execution Time":
                st.session_state["content_execution_time"],

                "Tokens":
                st.session_state["content_tokens"],

                "Estimated Cost":
                st.session_state["content_cost"]

            })

        st.header("LinkedIn Post")

        st.write(
            campaign["linkedin_post"]
        )

        st.header("Marketing Email")

        st.write(
            campaign["marketing_email"]
        )

        st.header("Google Ad Copy")

        st.write(
            campaign["google_ad_copy"]
        )

    else:

        st.warning(
            "Strategy Rejected"
        )

    json_file = create_json(result)

    pdf_file = create_pdf(result)

    # ===================================================
    # DOWNLOAD MARKET REPORT
    # ===================================================

    with open(
        pdf_file,
        "rb"
    ) as file:

        st.download_button(

            label="📄 Download Market Report (PDF)",

            data=file,

            file_name="market_report.pdf",

            mime="application/pdf"

        )

    with open(
        json_file,
        "rb"
    ) as file:

        st.download_button(

            label="📦 Download JSON Report",

            data=file,

            file_name="market_report.json",

            mime="application/json"

        )

# ===================================================
# CAMPAIGN PDF
# ===================================================

if "campaign_content" in st.session_state:

    campaign_result = {

        "industry": industry,

        "goal": goal,

        "campaign_content": st.session_state[
            "campaign_content"
        ]

    }

    campaign_pdf = create_campaign_pdf(
        campaign_result
    )

    with open(
        campaign_pdf,
        "rb"
    ) as file:

        st.download_button(

            label="📄 Download Campaign Report",

            data=file,

            file_name="campaign_content.pdf",

            mime="application/pdf"

        )