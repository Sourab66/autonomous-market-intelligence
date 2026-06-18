import streamlit as st

from app.graph.builder import graph
from app.content_only import content_graph
from app.report_pdf_generator import create_pdf
from app.campaign_pdf_generator import create_campaign_pdf

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

    config = {
        "configurable": {
            "thread_id": "user_1"
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

    st.subheader("Market Report")
    st.json(result["market_report"])

    st.subheader("Trend Report")
    st.write(result["trend_report"])

    st.subheader("Competitor Report")
    st.json(result["competitor_report"])

    st.subheader("Strategy")
    st.json(result["strategy"])

    approval = st.radio(
        "Approve Strategy?",
        ["No", "Yes"]
    )

    if approval == "Yes":

        st.success("Strategy Approved")

        if not st.session_state.get(
            "content_generated",
            False
        ):

            content_result = content_graph.invoke(
                {
                    "strategy": result["strategy"]
                }
            )

            st.session_state[
                "campaign_content"
            ] = content_result[
                "campaign_content"
            ]

            st.session_state[
                "content_generated"
            ] = True

        campaign = st.session_state[
            "campaign_content"
        ]

        st.subheader("LinkedIn Post")
        st.write(
            campaign["linkedin_post"]
        )

        st.subheader("Marketing Email")
        st.write(
            campaign["marketing_email"]
        )

        st.subheader("Google Ad Copy")
        st.write(
            campaign["google_ad_copy"]
        )

    else:

        st.warning(
            "Strategy Rejected"
        )

    pdf_file = create_pdf(result)

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="Download PDF Report",
            data=file,
            file_name="market_report.pdf",
            mime="application/pdf"
        )

if "campaign_content" in st.session_state:

    campaign_result = {
        "campaign_content":
        st.session_state["campaign_content"]
    }

    campaign_pdf = create_campaign_pdf(
        campaign_result
    )

    with open(
        campaign_pdf,
        "rb"
    ) as file:

        st.download_button(
            label="Download Campaign PDF",
            data=file,
            file_name="campaign_content.pdf",
            mime="application/pdf"
        )