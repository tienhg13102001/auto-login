from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import json


file_path = os.path.join(os.path.dirname(__file__), 'input.json')

try:
  with open(file_path, encoding="utf8") as f:
      data = json.load(f)
  print(data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print(f"File {file_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")

driver = webdriver.Chrome()
sleep(1)
driver.get("https://www.netflix.com/login")

sleep(2)
def login_to_website(email, password):
    # Mở trang web
    driver.get('https://www.netflix.com/login')

    # Tìm và nhập email
    email_input = driver.find_element(By.NAME, 'userLoginId')
    email_input.send_keys(email)

    # Tìm và nhập mật khẩu
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    # Gửi biểu mẫu đăng nhập
    password_input.send_keys(Keys.RETURN)

    # Đợi một chút để trang tải
    time.sleep(5)

    # Kiểm tra xem đăng nhập có thành công hay không
    try:
        # Giả sử có phần tử với id 'profile-menu' khi đăng nhập thành công
        driver.find_element(By.CLASS_NAME, 'default-ltr-cache-1x17g94')
        print(f"Đăng nhập thất bại với {email}")
        return False
    except:
        print(f"Đăng nhập thành công với {email}")
        return True

for account in data['accounts']:
    if login_to_website(account['email'], account['password']):
        break  # Dừng lại khi đăng nhập thành công