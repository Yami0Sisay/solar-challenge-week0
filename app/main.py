import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_csv, summarize_metrics


st.title("Cross-Country Solar Comparison")
st.write("Upload cleaned CSVs for **Benin**, **Sierra Leone**, and **Togo** to compare GHI/DNI/DHI.")

# slider
st.sidebar.header("Upload Cleaned CSVs")
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

st.subheader("Key Metrics")
kpi_cols = st.columns(len(dfs))
for i, country in enumerate(df["Country"].unique()):
    sub = df[df["Country"] == country]
    mean_ghi = sub["GHI"].mean() if "GHI" in sub.columns else float("nan")
    with kpi_cols[i]:
        st.metric(label=f"{country} • Mean GHI", value=f"{mean_ghi:,.2f}")

# Boxplot
st.subheader("Distribution Comparison")
metric = st.selectbox("Select metric", metric_options, index=0)
fig_box = px.box(df, x="Country", y=metric, color="Country",
                 title=f"{metric} by Country (boxplot)")
st.plotly_chart(fig_box, use_container_width=True)

# Summary Table
st.subheader("Summary Table (mean / median / std)")
summary_cols = [c for c in ["GHI", "DNI", "DHI"] if c in df.columns]
summary = summarize_metrics(df, summary_cols)
st.dataframe(summary)

# Ranking bar of average GHI

if "GHI" in df.columns:
    st.subheader("Average GHI by Country")
    rank = df.groupby("Country")["GHI"].mean().reset_index().sort_values("GHI", ascending=False)
    fig_rank = px.bar(rank, x="Country", y="GHI", title="Ranking by Average GHI")
    st.plotly_chart(fig_rank, use_container_width=True)

with st.expander("Show combined data"):
    st.dataframe(df.head(100))