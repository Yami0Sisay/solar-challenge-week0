import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_csv, summarize_metrics


st.title("Cross-Country Solar Comparison")
st.caption("Benin • Sierra Leone • Togo")

st.markdown(
    """
**What this app does**
- Lets you upload cleaned CSVs and compare **GHI/DNI/DHI** across countries.
- Shows distributions, summary stats, and a simple ranking.
- Optionally runs **ANOVA** and **Kruskal–Wallis** on GHI to check if differences are significant.

**How to use**
1) In the left sidebar, upload one or more country CSVs.
2) Pick a metric to compare.
3) Scroll for summary table, tests, and notes.
4) Expand the “Show combined data” section to preview raw data.
"""
)

# sidebar
st.sidebar.header("Upload Cleaned CSVs")
st.sidebar.markdown(
    "*CSV must include columns:* `Country` (or will be added), `GHI` (plus optional `DNI`, `DHI`)."
)


with st.sidebar:
    f_benin = st.file_uploader("Benin", type="csv", key="benin")
    f_sl    = st.file_uploader("Sierraleone", type="csv", key="sierraleone")
    f_togo  = st.file_uploader("Togo", type="csv", key="togo")



dfs = []
if f_benin is not None:
    dfs.append(load_csv(f_benin, "Benin"))
if f_sl is not None:
    dfs.append(load_csv(f_sl, "Sierra Leone"))
if f_togo is not None:
    dfs.append(load_csv(f_togo, "Togo"))

if len(dfs) == 0:
    st.info("Upload at least one CSV to begin.")
    st.stop()

df = pd.concat(dfs, ignore_index=True)

# Basic checks
metric_options = [c for c in ["GHI", "DNI", "DHI"] if c in df.columns]
if not metric_options:
    st.error("Your files must include at least one of: GHI, DNI, DHI.")
    st.stop()

st.subheader("Key Metrics Overview")
st.markdown("Average GHI (Global Horizontal Irradiance) gives an overall sense of each country’s solar energy potential.")

kpi_cols = st.columns(len(dfs))
for i, country in enumerate(df["Country"].unique()):
    sub = df[df["Country"] == country]
    mean_ghi = sub["GHI"].mean() if "GHI" in sub.columns else float("nan")
    with kpi_cols[i]:
        st.metric(label=f"{country} • Mean GHI", value=f"{mean_ghi:,.2f}")

# Boxplot
st.subheader("Distribution Comparison")
st.markdown(
    """
Each boxplot shows how solar values (GHI/DNI/DHI) vary within each country.  
- A higher median and upper whisker indicate stronger sunlight intensity.  
- Outliers reflect extreme radiation peaks during very sunny periods.
"""
)

metric = st.selectbox("Select metric", metric_options, index=0)
fig_box = px.box(df, x="Country", y=metric, color="Country", title=f"{metric} by Country (boxplot)")
st.plotly_chart(fig_box, use_container_width=True)

# Summary Table
st.subheader("Summary Table (mean / median / std)")
st.markdown(
    """
This table summarizes each country’s central tendency and variability.  
Higher **mean** and **median** values indicate better solar conditions,  
while **std (standard deviation)** shows consistency or fluctuation.
"""
)

summary_cols = [c for c in ["GHI", "DNI", "DHI"] if c in df.columns]
summary = summarize_metrics(df, summary_cols)
st.dataframe(summary)

# Ranking bar of average GHI

if "GHI" in df.columns:
    st.subheader("Average GHI by Country")
    st.markdown(
        """
     This bar chart ranks countries by their average **GHI**,  
     helping identify which regions receive the most consistent sunlight.
     """
     )

    rank = df.groupby("Country")["GHI"].mean().reset_index().sort_values("GHI", ascending=False)
    fig_rank = px.bar(rank, x="Country", y="GHI", title="Ranking by Average GHI")
    st.plotly_chart(fig_rank, use_container_width=True)

with st.expander("Show combined data(First 100 rows)"):
    st.markdown("Preview of the merged dataset used for analysis.")
    st.dataframe(df.head(100))