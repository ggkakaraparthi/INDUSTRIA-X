import streamlit as st

st.set_page_config(
    page_title="INDUSTRIA-X",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 INDUSTRIA-X")
st.subheader("AI-Powered Industrial Production & Bottleneck Analysis")

st.markdown("---")

# --------------------------------------------------
# Production Models
# --------------------------------------------------

st.header("📊 Production Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model 1 Bottleneck",
        "Assembly"
    )
    st.metric(
        "Model 1 Throughput",
        "209.45 parts/hour"
    )

with col2:
    st.metric(
        "Model 2 Bottleneck",
        "Drilling"
    )
    st.metric(
        "Model 2 Entities Out",
        "6,554.37"
    )

with col3:
    st.metric(
        "Model 3 Bottleneck",
        "Forklift"
    )
    st.metric(
        "Model 3 Total Products",
        "54,746.71"
    )

st.markdown("---")

# --------------------------------------------------
# Model 3 Insights
# --------------------------------------------------

st.header("🔎 Model 3 Key Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Highest Utilization",
        "Cell1",
        "86.69%"
    )

with col2:
    st.metric(
        "Highest Queue",
        "Warehouse1",
        "190.77"
    )

with col3:
    st.metric(
        "Highest SKU Waiting",
        "SKU1",
        "0.7245"
    )

st.markdown("---")

# --------------------------------------------------
# Bottleneck Summary
# --------------------------------------------------

st.header("🚨 Bottleneck Summary")

bottleneck_data = {
    "Model 1": "Assembly",
    "Model 2": "Drilling",
    "Model 3": "Forklift"
}

for model, bottleneck in bottleneck_data.items():
    st.write(f"**{model}:** {bottleneck}")

st.markdown("---")

# --------------------------------------------------
# Business Impact
# --------------------------------------------------

st.header("💼 Business Impact")

st.info(
    "The system identifies production bottlenecks, queue buildup, "
    "resource utilization and waiting-time exposure to support "
    "evidence-based industrial decisions."
)

st.warning(
    "Financial profit/loss values require actual cost, price, "
    "revenue or margin data. The current dashboard therefore "
    "reports production-impact indicators rather than invented "
    "monetary values."
)

st.markdown("---")

st.success("INDUSTRIA-X Dashboard is running successfully.")