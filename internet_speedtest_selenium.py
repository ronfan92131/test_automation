from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to your ChromeDriver executable 
chrome_driver_path = '/usr/local/bin/chromedriver'

# URL for the speed test website
speed_test_url = 'https://www.speedtest.net/'

# Create a Chrome webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (optional)
driver = webdriver.Chrome()

try:
    # Open the speed test website
    driver.get(speed_test_url)
    
    # Wait for the page to load
    time.sleep(5)  # Adjust the time based on your internet speed or website load time
    
    # Find the button to start the speed test
    start_test_button = driver.find_element(By.CLASS_NAME,'start-text')
    start_test_button.click()
    
    # Wait for the speed test to complete (adjust the time based on your internet speed)
    time.sleep(60)  # Assuming the test takes approximately 60 seconds
    
    # Get and print the results
    result_element = driver.find_element(By.CLASS_NAME,'result-container-speed')
    result = result_element.find_element('text').text
    
    print(f'Download Speed: {download_speed}')
    print(f'Upload Speed: {upload_speed}')
except:
    print("exception observed")    
finally:
    # Close the browser window
    driver.quit()
