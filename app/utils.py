import pandas as pd

def load_csv(file, country_name):
    """Loads a CSV and adds a country identifier column."""
    df = pd.read_csv(file)
    df["Country"] = country_name
    return df

def summarize_metrics(df, metrics):
    """Returns summary stats (mean, median, std) for given metrics per country."""
    summary = (
        df.groupby("Country")[metrics]
        .agg(["mean", "median", "std"])
        .round(2)
    )
    return summary
