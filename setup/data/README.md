# Thư mục dữ liệu

Đặt file dữ liệu khảo sát/log trải nghiệm người dùng tại đây, ví dụ: `raw_survey_data.csv`.

## Cấu trúc cột dữ liệu đề xuất (survey)

| Cột                  | Mô tả                                                  | Kiểu dữ liệu           |
|----------------------|---------------------------------------------------------|------------------------|
| respondent_id        | Mã định danh người trả lời                              | int/string             |
| loading_speed_score  | Đánh giá tốc độ tải trang (thang Likert 1-5)            | int                    |
| visual_clarity_score | Đánh giá độ trực quan giao diện (thang Likert 1-5)      | int                    |
| color_scheme_score   | Đánh giá màu sắc giao diện (thang Likert 1-5)            | int                    |
| checkout_process_score | Đánh giá quy trình thanh toán (thang Likert 1-5)      | int                    |
| satisfaction_score   | Điểm hài lòng chung (thang Likert 1-5 hoặc NPS)          | int                    |
| browsing_time_sec    | Thời gian duyệt trang (giây) — nếu có log hệ thống       | float                  |
| repurchase_frequency | Tần suất mua lại (số lần/tháng hoặc phân loại có/không)  | int/bool               |
| platform             | Nền tảng sử dụng: "app" hoặc "web"                       | string (categorical)   |

> Bảng trên chỉ là gợi ý ban đầu — điều chỉnh lại theo bảng câu hỏi khảo sát thực tế của bạn.

## Nguồn dữ liệu có thể tham khảo (nếu không tự khảo sát kịp)

- Bộ dữ liệu mở về UX/e-commerce trên Kaggle (tìm từ khóa "e-commerce user experience", "website UX survey")
- Log truy cập website (Google Analytics export) nếu có quyền truy cập một trang TMĐT thực tế
