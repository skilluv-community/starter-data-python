"""Small helpers imported from the notebooks.

Keep functions here pure and tested — notebooks should only orchestrate them.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a DataFrame. Raises FileNotFoundError if missing."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"dataset not found: {p}")
    return pd.read_csv(p)


def summary_stats(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Aggregate `value_col` by `group_col` and return count/mean/sum/std."""
    grouped = df.groupby(group_col)[value_col].agg(["count", "mean", "sum", "std"])
    return grouped.reset_index()


def top_n(df: pd.DataFrame, column: str, n: int = 10) -> pd.DataFrame:
    """Return the `n` rows with the highest `column` value."""
    if n <= 0:
        raise ValueError("n must be positive")
    return df.sort_values(column, ascending=False).head(n).reset_index(drop=True)
