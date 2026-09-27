"""
model_training.py
-------------------
Xây dựng mô hình phân loại dự báo khả năng khách hàng hài lòng
dựa trên các thuộc tính UI/UX.

Mô hình: Logistic Regression, Decision Tree
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

CLEAN_DATA_PATH = "../setup/data/clean_survey_data.csv"

FEATURES = [
    "loading_speed_score",
    "visual_clarity_score",
    "color_scheme_score",
    "checkout_process_score",
]

# Biến mục tiêu dạng nhị phân: hài lòng (1) / không hài lòng (0)
# Ví dụ quy ước: satisfaction_score >= 4 -> hài lòng
TARGET = "is_satisfied"


def prepare_target(df: pd.DataFrame, threshold: int = 4) -> pd.DataFrame:
    df[TARGET] = (df["satisfaction_score"] >= threshold).astype(int)
    return df


def train_and_evaluate(df: pd.DataFrame):
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print(f"\n=== {name} ===")
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification report:\n", classification_report(y_test, y_pred))


def main():
    df = pd.read_csv(CLEAN_DATA_PATH)
    df = prepare_target(df)
    train_and_evaluate(df)


if __name__ == "__main__":
    main()
