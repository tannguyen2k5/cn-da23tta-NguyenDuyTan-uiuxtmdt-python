# Phân tích mối tương quan về mức độ hài lòng về trải nghiệm người dùng (UI/UX) trên hệ thống thương mại điện tử

**Sinh viên thực hiện:** Nguyễn Duy Tân
**Lớp:** DA23TTA
**Khoa:** Công nghệ Thông tin — Trường Kỹ thuật và Công nghệ, Trà Vinh University (TVU)
**Giảng viên hướng dẫn:** *(đang cập nhật)*

---

## 1. Giới thiệu đề tài

Nghiên cứu các thành phần giao diện (tốc độ tải, độ trực quan, màu sắc, quy trình thanh toán) tác động đến điểm hài lòng và hành vi quay lại của khách hàng trên sàn giao dịch thương mại điện tử (TMĐT).

## 2. Mục tiêu

Nhận diện các thuộc tính UI/UX cốt lõi giúp tối ưu trải nghiệm người dùng trên hệ thống TMĐT.

## 3. Đối tượng và phạm vi nghiên cứu

- **Đối tượng:** Điểm đánh giá UI/UX, thời gian duyệt trang, tần suất mua lại.
- **Phạm vi:** Người tiêu dùng sử dụng ứng dụng di động hoặc website TMĐT.

## 4. Nội dung thực hiện

- Tiền xử lý dữ liệu khảo sát/log trải nghiệm người dùng.
- Lập ma trận tương quan giữa các thuộc tính UI/UX với độ hài lòng.
- Xây dựng mô hình phân loại dự báo khả năng khách hàng hài lòng.

## 5. Phương pháp nghiên cứu

- Phân tích tương quan Pearson/Spearman.
- Hồi quy Logistic (Logistic Regression).
- Cây quyết định (Decision Tree).

## 6. Công nghệ sử dụng

- **Ngôn ngữ:** Python
- **Thư viện (dự kiến):** pandas, numpy, scipy, scikit-learn, matplotlib/seaborn

## 7. Cấu trúc thư mục

```
.
├── setup/            # Hướng dẫn/tập tin cài đặt môi trường, dữ liệu thử nghiệm
├── src/              # Mã nguồn chính (tiền xử lý, phân tích tương quan, mô hình)
├── progress-report/  # [bắt buộc] Báo cáo tiến độ hàng tuần
├── thesis/           # [bắt buộc] Tài liệu văn bản của đồ án
│   ├── doc/          # Tài liệu dạng .DOC
│   ├── pdf/          # Tài liệu dạng .PDF
│   ├── html/         # Tài liệu dạng web
│   ├── abs/           # Báo cáo dạng .PPT, .AVI, ...
│   └── refs/         # Tài liệu tham khảo
├── soft/             # Phần mềm liên quan (nếu có)
└── README.md
```

## 8. Hướng dẫn cài đặt & chạy thử

```bash
# 1. Clone repository
git clone https://github.com/tannguyen2k5/cn-da23tta-NguyenDuyTan-uiuxtmdt-python.git
cd cn-da23tta-NguyenDuyTan-uiuxtmdt-python

# 2. Tạo môi trường ảo (khuyến khích)
python -m venv venv
venv\Scripts\activate      # Windows

# 3. Cài đặt thư viện
pip install -r setup/requirements.txt

# 4. Chạy chương trình phân tích
python src/main.py
```

*(Nội dung mục này sẽ được cập nhật chi tiết hơn khi có mã nguồn thực tế.)*

## 9. Tiến độ

Xem chi tiết báo cáo tiến độ hàng tuần tại thư mục [`progress-report/`](./progress-report).

## 10. Liên hệ

- **Họ tên:** Nguyễn Duy Tân
- **Email:** *(điền email của bạn)*
- **Điện thoại:** *(điền số điện thoại của bạn)*
