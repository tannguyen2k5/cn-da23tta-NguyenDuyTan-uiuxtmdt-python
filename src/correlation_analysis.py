"""
correlation_analysis.py
-------------------------
Lập ma trận tương quan giữa các thuộc tính UI/UX với độ hài lòng
(điểm hài lòng, thời gian duyệt trang, tần suất mua lại).

Phương pháp: Pearson (biến định lượng, quan hệ tuyến tính)
             Spearman (biến thứ bậc/không giả định tuyến tính)
"""

import pandas as pd
from scipy.stats import pearsonr, spearmanr

CLEAN_DATA_PATH = "../setup/data/clean_survey_data.csv"

UIUX_FEATURES = [
    "loading_speed_score",
    "visual_clarity_score",
    "color_scheme_score",
    "checkout_process_score",
]

TARGET_VARIABLES = [
    "satisfaction_score",
    "browsing_time_sec",
    "repurchase_frequency",
]


def compute_correlation_matrix(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """Tính ma trận tương quan giữa các biến UI/UX và biến mục tiêu."""
    cols = UIUX_FEATURES + TARGET_VARIABLES
    return df[cols].corr(method=method)


def compute_pairwise_correlation(df: pd.DataFrame):
    """
    In chi tiết hệ số tương quan + p-value cho từng cặp
    (thuộc tính UI/UX) x (biến mục tiêu), theo cả Pearson và Spearman.
    """
    results = []
    for feature in UIUX_FEATURES:
        for target in TARGET_VARIABLES:
            r_pearson, p_pearson = pearsonr(df[feature], df[target])
            r_spearman, p_spearman = spearmanr(df[feature], df[target])
            results.append({
                "feature": feature,
                "target": target,
                "pearson_r": round(r_pearson, 3),
                "pearson_p": round(p_pearson, 4),
                "spearman_r": round(r_spearman, 3),
                "spearman_p": round(p_spearman, 4),
            })
    return pd.DataFrame(results)


def main():
    df = pd.read_csv(CLEAN_DATA_PATH)

    print("=== Ma trận tương quan Pearson ===")
    print(compute_correlation_matrix(df, method="pearson"))

    print("\n=== Ma trận tương quan Spearman ===")
    print(compute_correlation_matrix(df, method="spearman"))

    print("\n=== Chi tiết từng cặp biến ===")
    result_df = compute_pairwise_correlation(df)
    print(result_df)
    result_df.to_csv("correlation_results.csv", index=False)


if __name__ == "__main__":
    main()
