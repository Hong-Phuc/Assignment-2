# Selenium Testing with Pytest

## Mô tả
Dự án này sử dụng Selenium và Pytest để tự động hóa các bài kiểm tra cho trang web demo Opencart. Các bài kiểm tra bao gồm đăng nhập, đăng xuất, gửi biểu mẫu, điều hướng, thêm vào giỏ hàng và thanh toán, kiểm tra tính năng tìm kiếm, kiểm tra dữ liệu sản phẩm và khả năng đáp ứng của trang web.

## Yêu cầu
- Python 3.x
- Pytest
- Selenium
- Trình duyệt Microsoft Edge

## Cài đặt
1. **Cài đặt Python**: Đảm bảo rằng Python đã được cài đặt trên máy tính của bạn.
2. **Cài đặt các thư viện cần thiết**:
   ```
   pip install pytest selenium
   
3. **Cài đặt WebDriver cho Microsoft Edge**: Tải và cài đặt Microsoft Edge WebDriver từ trang tải xuống WebDriver.

## Cách sử dụng
1. Tải mã nguồn của dự án này về máy của bạn.
2. Mở terminal và điều hướng đến thư mục chứa mã nguồn.
3. Chạy các bài kiểm tra bằng lệnh:
    ```
    pytest

## Các bài kiểm tra
1. Đăng nhập không hợp lệ
Kiểm tra tình huống đăng nhập với thông tin không chính xác.

2. Đăng nhập hợp lệ
Kiểm tra tình huống đăng nhập với thông tin chính xác.

3. Đăng xuất
Kiểm tra quá trình đăng xuất sau khi đăng nhập.

4. Gửi biểu mẫu
Kiểm tra gửi biểu mẫu với thông tin không chính xác.

5. Điều hướng
Kiểm tra khả năng điều hướng giữa các trang trên trang web.

6. Xác thực dữ liệu
Kiểm tra tên, giá và mô tả của sản phẩm.

7. Thêm vào giỏ hàng và thanh toán
Kiểm tra chức năng thêm sản phẩm vào giỏ hàng và tiến hành thanh toán.

8. Tìm kiếm
Kiểm tra chức năng tìm kiếm sản phẩm trên trang web.

9. Thiết kế đáp ứng
Kiểm tra khả năng đáp ứng của trang web với các kích thước cửa sổ khác nhau.

## Ghi chú
- Đảm bảo rằng bạn đã cho phép các trình duyệt mở trong môi trường của mình và đã cài đặt WebDriver đúng cách.
- Các bài kiểm tra có sử dụng time.sleep() để chờ các yếu tố tải, có thể thay thế bằng các phương thức chờ tốt hơn như WebDriverWait.

## Hỗ trợ
Nếu bạn gặp vấn đề nào trong quá trình sử dụng hoặc có câu hỏi, vui lòng tạo một issue trên GitHub hoặc liên hệ trực tiếp với tôi.