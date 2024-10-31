import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

# Login invalid
def test_login_invalid(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(5)
    driver.get("https://demo.opencart.com/") # Chờ xác thực là con người
    time.sleep(12) 
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click() # Mở menu tài khoản
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click() # Chọn đăng nhập
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("abc") # Nhập tài khoản đã đăng kí
    driver.find_element(By.NAME, "password").send_keys("xyz") # Nhập mật khẩu đúng
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click() # Ấn đăng nhập
    time.sleep(2)  # Chờ tải trang và thông báo lỗi

# Login valid
def test_login_valid(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(1)
    driver.get("https://demo.opencart.com/") # Chờ xác thực là con người
    time.sleep(12) 
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click() # Mở menu tài khoản
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click() # Chọn đăng nhập
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("hongphuc71233@gmail.com") # Nhập tài khoản đã đăng kí
    driver.find_element(By.NAME, "password").send_keys("nguyenhongphucnguyenhongphuc") # Nhập mật khẩu đúng
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click() # Ấn đăng nhập
    time.sleep(2)  # Chờ tải trang account

# Logout
def test_logout(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(1)
    driver.get("https://demo.opencart.com/") # Chờ xác thực là con người
    time.sleep(12) 
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click() # Mở menu tài khoản
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click() # Chọn đăng nhập
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("hongphuc71233@gmail.com") # Nhập tài khoản đã đăng kí
    driver.find_element(By.NAME, "password").send_keys("nguyenhongphucnguyenhongphuc") # Nhập mật khẩu đúng
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click() # Ấn đăng nhập
    time.sleep(2)  # Chờ tải trang account
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click() # mở menu ngừi dùng
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/logout']").click() # Chọn đăng xuất
    
# Form Submission
def test_form_submission(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("hongphuc71233@gmail.com") # Nhập tài khoản
    driver.find_element(By.NAME, "password").send_keys("xyz") # Nhập mật khẩu
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(3)
    # Kiểm tra thông báo sau khi gửi biểu mẫu
    message = driver.find_element(By.ID, "alert").text
    assert "Warning: No match for E-Mail Address and/or Password." in message

# Navigation
def test_navigation(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)  # Chờ trang tải
    driver.get("https://demo.opencart.com/") # Chờ xác thực là con người
    time.sleep(12)
    assert "Your Store" in driver.title  # Kiểm tra tiêu đề trang chính

    # Điều hướng đến trang đăng nhập
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(2)  # Chờ trang tải
    assert "Account Login" in driver.title  # Kiểm tra tiêu đề trang đăng nhập

    # Điều hướng đến trang đăng ký
    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(2)  # Chờ trang tải
    assert "Register Account" in driver.title  # Kiểm tra tiêu đề trang đăng ký

    # Quay lại trang chính
    driver.get("https://demo.opencart.com/en-gb?route=common/home")
    time.sleep(2)  # Chờ trang tải
    assert "Your Store" in driver.title  # Kiểm tra lại tiêu đề trang chính

# Data Validation
def test_data_validation(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # Xác thực tên sản phẩm
    product_name = driver.find_element(By.XPATH, "//a[text()='iPhone']").text
    assert product_name == "iPhone", f"Lỗi: Tên sản phẩm mong đợi 'iPhone', nhưng nhận được '{product_name}'"

    # Xác thực giá sản phẩm
    price_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[2]/div/div/span[1]")
    price_text = price_element.text.split("\n")[0]
    expected_price = "$123.20"
    assert price_text == expected_price, f"Lỗi: Giá sản phẩm mong đợi '{expected_price}', nhưng nhận được '{price_text}'"

    # Xác thực mô tả sản phẩm
    description = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[2]/div/p").text
    assert "iPhone is a revolutionary new mobile phone" in description, "Lỗi: Mô tả sản phẩm không chứa thông tin mong đợi."

    print("Dữ liệu sản phẩm đã được kiểm tra thành công!")

# Add to cart, check out
def test_add_to_cart_and_checkout(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(2)

    driver.get("https://demo.opencart.com/") # Chờ xác thực là con người
    time.sleep(12) # Xác thực xong hãy kéo xuống danh mục sản phẩm
    
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[2]/form/div/button[1]").click() # Chọn thêm sản phẩm vào giỏ hàng
    time.sleep(2)

    driver.get("https://demo.opencart.com/") # Về đầu trang để ấn vào giỏ hàng
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle").click() # Chọn xem giỏ hàng để hiện nút checkout
    time.sleep(3)

    driver.find_element(By.XPATH, "//*[@id='header-cart']/div/ul/li/div/p/a[2]").click() # chọn checkout
    time.sleep(3)

    assert "Checkout" in driver.title

# Search Functionality:
def test_search_functionality(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)

    driver.find_element(By.NAME, "search").send_keys("Macbook") #Nhập từ khóa
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    time.sleep(3)
    
    assert "Search - Macbook" in driver.title # Kiểm tra kết quả tìm kiếm

# Responsive Design
@pytest.mark.parametrize("size", [(800, 600), (1024, 768), (1920, 1080)])  # Thiết lập kích thước cửa sổ trình duyệt
def test_responsive_design(driver, size):
    driver.set_window_size(*size)
    driver.get("https://demo.opencart.com/")
    
    time.sleep(5)

    element = driver.find_element(By.ID, "logo") # Kiểm tra tính hiển thị của logo
    assert element.is_displayed()