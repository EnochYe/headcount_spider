from attr import attributes
import zipcodes

def get_details(browser_handle, job_type, row_index, ws):
    job = browser_handle.find_element('//div[@class=\'jobs-unified-top-card__content--two-pane\']/a')
    job_title = job.text
    job_link = job.get_attribute('href')

    # 因为有的工作没有标明相关信息，所以不一定能获取到
    try:
        company = browser_handle.find_element('//a[@class=\'ember-view t-black t-normal\']')
        company_name = company.text
        company_link = company.get_attribute('href')
    except Exception:
        company_name = browser_handle.find_element('//div[@class=\'mt2\']/span[1]/span[1]').text
        company_link = 'null'
    location = browser_handle.find_elements('//span[@class=\'jobs-unified-top-card__bullet\']')[0].text

    try:
        company_details = browser_handle.find_element('//li[@class=\'jobs-unified-top-card__job-insight\'][2]').text.split('·')
        company_size = company_details[0]
        company_industry = company_details[1]
    except Exception:
        company_size = 'null'
        company_industry = 'null'

    try:
        workplace_type = browser_handle.find_element('//span[@class="jobs-unified-top-card__workplace-type"]').text
    except Exception:
        workplace_type = 'null'

    # 使用外来的包获取地址对应的邮编
    try:
        city = location.split(', ')[0]
        state = location.split(', ')[1]
        zipcode = zipcodes.filter_by(city=city, state=state)[0]['zip_code']
    except IndexError as rss:
        zipcode = 'null'

    
    """
    for line_index in range(1, 11):
        if line_index == 1:
            ws.cell(row_index, line_index, job_title)
        elif line_index == 2:
            ws.cell(row_index, line_index, company_name)
        elif line_index == 3:
            ws.cell(row_index, line_index, location)
        elif line_index == 4:
            ws.cell(row_index, line_index, job_link)
        elif line_index == 5:
            ws.cell(row_index, line_index, company_link)
        elif line_index == 6:
            ws.cell(row_index, line_index, job_type)
        elif line_index == 7:
            ws.cell(row_index, line_index, workplace_type)
        elif line_index == 8:
            ws.cell(row_index, line_index, zipcode)
        elif line_index == 9:
            ws.cell(row_index, line_index, company_industry)
        elif line_index == 10:
            ws.cell(row_index, line_index, company_size)
    """
    # 以上写的太笨拙了，给你改成如下

    attributes = (job_title, company_name, location, job_link, company_link, job_type, workplace_type, zipcode, company_industry, company_size)
    for index, attr in enumerate(attributes):
        ws.cell(row_index, index+1, attr)
