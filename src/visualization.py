"""
visualization.py
------------------
Trực quan hóa dữ liệu và kết quả phân tích:
- Heatmap ma trận tương quan
- Phân phối các biến UI/UX và độ hài lòng
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


def plot_correlation_heatmap(df: pd.DataFrame, method: str = "pearson"):
    cols = UIUX_FEATURES + TARGET_VARIABLES
    corr = df[cols].corr(method=method)

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Ma trận tương quan ({method})")
    plt.tight_layout()
    plt.savefig(f"correlation_heatmap_{method}.png")
    plt.show()


def plot_feature_distributions(df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    for ax, feature in zip(axes.flatten(), UIUX_FEATURES):
        sns.histplot(df[feature], kde=True, ax=ax)
        ax.set_title(feature)
    plt.tight_layout()
    plt.savefig("feature_distributions.png")
    plt.show()


def main():
    df = pd.read_csv(CLEAN_DATA_PATH)
    plot_correlation_heatmap(df, method="pearson")
    plot_correlation_heatmap(df, method="spearman")
    plot_feature_distributions(df)


if __name__ == "__main__":
    main()
