from selenium import webdriver

#สร้าง Webdriver
options = get_default_edge_options()
driver = webdriver.Edge(options=options)

#เปิดเว็บไซต์
driver.get("https://www.google.com")