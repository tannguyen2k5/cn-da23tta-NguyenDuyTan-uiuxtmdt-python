"""
data_preprocessing.py
----------------------
Tiền xử lý dữ liệu khảo sát/log trải nghiệm người dùng (UI/UX) trên hệ thống TMĐT.

Các bước chính:
1. Đọc dữ liệu thô (CSV) từ setup/data/
2. Kiểm tra giá trị thiếu, trùng lặp
3. Chuẩn hóa/mã hóa các biến (ví dụ: platform: app/web -> 0/1)
4. Xuất dữ liệu đã làm sạch để dùng cho các bước phân tích tiếp theo
"""

import pandas as pd
import numpy as np

RAW_DATA_PATH = "../setup/data/raw_survey_data.csv"
CLEAN_DATA_PATH = "../setup/data/clean_survey_data.csv"


def load_data(path: str = RAW_DATA_PATH) -> pd.DataFrame:
    """Đọc dữ liệu khảo sát thô."""
    df = pd.read_csv(path)
    print(f"Đã đọc {df.shape[0]} dòng, {df.shape[1]} cột.")
    return df


def check_missing_and_duplicates(df: pd.DataFrame) -> None:
    """In ra thông tin giá trị thiếu và dòng trùng lặp."""
    print("Giá trị thiếu theo cột:\n", df.isnull().sum())
    print(f"Số dòng trùng lặp: {df.duplicated().sum()}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Làm sạch dữ liệu:
    - Loại bỏ dòng trùng lặp
    - Xử lý giá trị thiếu (ví dụ: điền bằng median cho cột số)
    - Mã hóa biến phân loại (platform)
    """
    df = df.drop_duplicates()

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    if "platform" in df.columns:
        df["platform_encoded"] = df["platform"].map({"web": 0, "app": 1})

    return df


def main():
    df = load_data()
    check_missing_and_duplicates(df)
    df_clean = clean_data(df)
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)
    print(f"Đã lưu dữ liệu sạch tại: {CLEAN_DATA_PATH}")


if __name__ == "__main__":
    main()
