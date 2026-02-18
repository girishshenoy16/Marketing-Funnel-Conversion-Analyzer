import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.stats.proportion import proportions_ztest

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Ecommerce Growth Analytics",
    layout="wide",
    page_icon="📊"
)

plotly_template = "plotly_dark"

# -------------------------------------------------
# LOAD PRECOMPUTED DATA (FAST)
# -------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data():
    session_summary = pd.read_csv("data/processed/session_summary.csv")
    category_summary = pd.read_csv("data/processed/category_summary.csv")
    cohort_table = pd.read_csv("data/processed/cohort_table.csv", index_col=0)
    monthly_metrics = pd.read_csv("data/processed/monthly_metrics.csv")

    return session_summary, category_summary, cohort_table, monthly_metrics

session_summary, category_summary, cohort_table, monthly_metrics = load_data()

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("📊 Ecommerce Growth & Funnel Analytics Platform")
st.markdown("---")

# -------------------------------------------------
# TABS
# -------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Executive",
    "🔍 Funnel",
    "🛍 Category",
    "🔁 Retention",
    "🧪 Experiment"
])

# =================================================
# EXECUTIVE TAB
# =================================================
with tab1:

    total_sessions = session_summary.shape[0]
    total_purchases = session_summary["has_purchase"].sum()

    conversion_rate = round((total_purchases / total_sessions) * 100, 2)

    total_revenue = round(monthly_metrics["total_revenue"].sum(), 2)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sessions", f"{total_sessions:,}")
    col2.metric("Total Revenue", f"${total_revenue:,.2f}")
    col3.metric("Conversion Rate", f"{conversion_rate:.2f}%")

    st.markdown("### Monthly Revenue Trend")

    fig_rev = px.line(
        monthly_metrics,
        x="event_month",
        y="total_revenue",
        template=plotly_template,
        markers=True
    )

    fig_rev.update_layout(height=450)
    st.plotly_chart(fig_rev, use_container_width=True)

# =================================================
# FUNNEL TAB
# =================================================
with tab2:

    view_sessions = session_summary["has_view"].sum()
    cart_sessions = session_summary["has_cart"].sum()
    purchase_sessions = session_summary["has_purchase"].sum()

    fig_funnel = go.Figure(go.Funnel(
        y=["View", "Cart", "Purchase"],
        x=[view_sessions, cart_sessions, purchase_sessions],
        textinfo="value+percent initial"
    ))

    fig_funnel.update_layout(template=plotly_template, height=500)
    st.plotly_chart(fig_funnel, use_container_width=True)

    sequential_sessions = session_summary[
        session_summary["has_view"] &
        session_summary["has_cart"] &
        session_summary["has_purchase"]
    ].shape[0]

    true_seq_rate = round((sequential_sessions / total_sessions) * 100, 2)

    st.metric("True Sequential Conversion", f"{true_seq_rate:.2f}%")

# =================================================
# CATEGORY TAB
# =================================================
with tab3:

    category_summary["conversion_rate"] = (
        category_summary["conversion_rate"].round(2)
    )

    top_categories = (
        category_summary
        .sort_values("conversion_rate", ascending=False)
        .head(10)
        .reset_index()
    )

    fig_cat = px.bar(
        top_categories,
        x="conversion_rate",
        y="category_code",
        orientation="h",
        template=plotly_template,
        text=top_categories["conversion_rate"].apply(lambda x: f"{x:.2f}%"),
        labels={"conversion_rate": "Conversion Rate (%)"}
    )

    fig_cat.update_traces(textposition="outside")
    fig_cat.update_layout(height=600)

    st.plotly_chart(fig_cat, use_container_width=True)

# =================================================
# RETENTION TAB
# =================================================
with tab4:

    purchase_sessions = session_summary[
        session_summary["has_purchase"] == True
    ]

    user_counts = purchase_sessions.groupby("user_id").size()

    repeat_users = (user_counts > 1).sum()
    total_buyers = user_counts.count()

    repeat_rate = round(
        (repeat_users / total_buyers) * 100 if total_buyers > 0 else 0,
        2
    )

    st.metric("Repeat Purchase Rate", f"{repeat_rate:.2f}%")

    cohort_display = cohort_table.round(2)

    fig_cohort = px.imshow(
        cohort_display,
        text_auto=".2f",
        aspect="auto",
        template=plotly_template,
        color_continuous_scale="Blues",
        height=500
    )

    st.plotly_chart(fig_cohort, use_container_width=True)

# =================================================
# EXPERIMENT TAB
# =================================================
with tab5:

    st.subheader("A/B Test Simulation")

    session_ab = session_summary.copy()
    session_ab["experiment_group"] = np.random.choice(
        ["A", "B"], len(session_ab)
    )

    conversions = session_ab.groupby("experiment_group")["has_purchase"].sum()
    sessions = session_ab.groupby("experiment_group")["user_session"].count()

    conv_a = conversions.get("A", 0)
    conv_b = conversions.get("B", 0)

    total_a = sessions.get("A", 1)
    total_b = sessions.get("B", 1)

    rate_a = round((conv_a / total_a) * 100, 2)
    rate_b = round((conv_b / total_b) * 100, 2)

    count = np.array([conv_a, conv_b])
    nobs = np.array([total_a, total_b])

    stat, pval = proportions_ztest(count, nobs)
    pval = round(pval, 2)

    fig_ab = px.bar(
        x=["Group A", "Group B"],
        y=[rate_a, rate_b],
        template=plotly_template,
        text=[f"{rate_a:.2f}%", f"{rate_b:.2f}%"],
        labels={"x": "Group", "y": "Conversion Rate (%)"}
    )

    fig_ab.update_traces(textposition="outside")
    fig_ab.update_layout(height=500)

    st.plotly_chart(fig_ab, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Group A Conversion", f"{rate_a:.2f}%")
    col2.metric("Group B Conversion", f"{rate_b:.2f}%")
    col3.metric("p-value", f"{pval:.2f}")

    if pval < 0.05:
        st.success("Statistically Significant Difference Detected")
    else:
        st.info("No Statistically Significant Difference")