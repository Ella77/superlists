
from selenium import webdriver
browser = webdriver.Firefox(executable_path='/Users/soojin/Downloads/geckodriver')
browser.get('http://localhost:8000')
assert 'To-Do' in browser.title

