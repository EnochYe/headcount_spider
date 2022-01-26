from attr import attributes
import zipcodes


def get_details(browser_handle, job_type, row_index, ws, w):
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
        company_details = browser_handle.find_element(
            '//li[@class=\'jobs-unified-top-card__job-insight\'][2]').text.split('·')
        company_size = company_details[0]
        company_industry = company_details[1]
    except Exception:
        company_size = 'null'
        company_industry = 'null'

    if (len(browser_handle.find_elements(
            '//span[@class="jobs-unified-top-card__subtitle-primary-grouping mr2 t-black"]/span')) < 3):
        workplace_type = 'null'
    else:
        workplace_type = browser_handle.find_element('//span[@class="jobs-unified-top-card__workplace-type"]').text
    # try:
    #     workplace_type = browser_handle.find_element('//span[@class="jobs-unified-top-card__workplace-type"]').text
    # except Exception:
    #     workplace_type = 'null'

    # 使用外来的包获取地址对应的邮编
    try:
        city = location.split(', ')[0]
        state = location.split(', ')[1]
        zipcode = zipcodes.filter_by(city=city, state=state)[0]['zip_code']
    except IndexError as rss:
        zipcode = 'null'

    attributes = (
        job_title, company_name, location, job_link, company_link, job_type, workplace_type, zipcode, company_industry,
        company_size)
    for index, attr in enumerate(attributes):
        ws.cell(row_index, index + 1, attr)
    w.save("test.xlsx")
