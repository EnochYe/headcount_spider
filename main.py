from utils import browser_handler, url, data
from openpyxl import Workbook
import time

if __name__ == '__main__':
    driver_path = r'E:\driver\chromedriver.exe'
    base_url = 'https://www.linkedin.com'
    browser_handle = browser_handler.BrowserHandler(driver_path=driver_path, base_url=base_url)

    job_type_dict = {   'f_JT=F&': 'full_time', 
                        'f_JT=P&': 'part_time', 
                        'f_JT=C&': 'contract', 
                        'f_JT=T&': 'temporary',
                        'f_JT=I&': 'internship', 
                        'f_JT=O&': 'other'}

    w = Workbook()
    for jobType in job_type_dict.keys():
        ws = w.create_sheet(job_type_dict[jobType])
        for start in range(0,1000,25):
            newUrl = url.get_url(jobType, start)
            browser_handle.get_url(newUrl)
            browser_handle.mouse_slide_move()
            titles = browser_handle.find_elements('//div[@class=\'full-width artdeco-entity-lockup__title ''ember-view\']')
            for title in titles:
                title.click()
                time.sleep(1)
                data.get_details(browser_handle, job_type_dict[jobType], start + 1, ws)
    w.save('test.xlsx')
    browser_handle.quit()
