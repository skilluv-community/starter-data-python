from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from src.utils import load_csv, summary_stats, top_n


def test_load_csv_reads_file(tmp_path: Path) -> None:
    p = tmp_path / "sample.csv"
    p.write_text("country,pop\nBenin,13\nSenegal,17\n")
    df = load_csv(p)
    assert list(df.columns) == ["country", "pop"]
    assert len(df) == 2


def test_load_csv_missing_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_csv(tmp_path / "missing.csv")


def test_summary_stats() -> None:
    df = pd.DataFrame({"region": ["W", "W", "E"], "pop": [10, 20, 30]})
    s = summary_stats(df, "region", "pop")
    assert s.loc[s.region == "W", "sum"].iloc[0] == 30
    assert s.loc[s.region == "E", "count"].iloc[0] == 1


def test_top_n() -> None:
    df = pd.DataFrame({"country": ["A", "B", "C"], "pop": [1, 3, 2]})
    top = top_n(df, "pop", n=2)
    assert list(top.country) == ["B", "C"]


def test_top_n_invalid_n() -> None:
    df = pd.DataFrame({"a": [1]})
    with pytest.raises(ValueError):
        top_n(df, "a", n=0)
