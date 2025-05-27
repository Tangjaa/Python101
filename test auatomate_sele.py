'''from selenium import webdriver

#สร้าง Webdriver
options = get_default_edge_options()
driver = webdriver.Edge(options=options)

#เปิดเว็บไซต์
driver.get("https://www.google.com")

def get_default_edge_options():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    return options'''

from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("--start-maximized")  # ใส่ option ที่ต้องการ

driver = webdriver.Edge(options=options)
driver.get("https://www.google.com")
