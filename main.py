from utils import browser_handler, url, data
from openpyxl import Workbook
import time

# 主函数
if __name__ == '__main__':
    # 需要提前配置好selenium对应的浏览器驱动
    driver_path = r'E:\driver\chromedriver.exe'
    base_url = 'https://www.linkedin.com'
    browser_handle = browser_handler.BrowserHandler(driver_path=driver_path, base_url=base_url)

# 创建work_type的dictionary来进行遍历
    job_type_dict = {'f_JT=F&': 'full_time',
                     'f_JT=P&': 'part_time',
                     'f_JT=C&': 'contract',
                     'f_JT=T&': 'temporary',
                     'f_JT=I&': 'internship',
                     'f_JT=O&': 'other'}

    # 新建一个Excel文档来存储数据
    w = Workbook()
    for jobType in job_type_dict.keys():
        # 根据不同的work_type来创建不同的ExcelSheet
        ws = w.create_sheet(job_type_dict[jobType])
        # 由于每个type的数量不同，需要提前获取最大页数
        num = browser_handle.get_last_button(jobType)
        for start in range(0, num + 1, 25):
            # 拼凑出新的URL来访问
            newUrl = url.get_url(jobType, start)
            browser_handle.get_url(newUrl)
            # 防止元素没加载出来，将滑条拉倒最下 确保元素都加载出来了
            browser_handle.mouse_slide_move()
            titles = browser_handle.find_elements(
                '//div[@class=\'full-width artdeco-entity-lockup__title ''ember-view\']')
            Row_Index = 1
            for title in titles:
                title.click()
                time.sleep(0.1)
                data.get_details(browser_handle, job_type_dict[jobType], start + Row_Index, ws, w)
                Row_Index = Row_Index + 1
    w.save('test.xlsx')
    browser_handle.quit()
