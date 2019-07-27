##It may fail sometimes. Feel free to adapt to your own need
## @author {DARWISH Marwan, https://github.com/DMarwan, https://www.linkedin.com/in/dmarwan/}



def scraper(mail, password, job, location):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    browser = webdriver.Chrome('/usr/bin/chromedriver')
    browser.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
    login = browser.find_element_by_xpath('//*[@id="username"]').send_keys(mail)
    pwd = browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    validation_1 = browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').send_keys(Keys.ENTER)
    time.sleep(1.5)
    jobs = browser.find_element_by_xpath('//*[@id="jobs-nav-item"]/a').click()
    time.sleep(1.5)
    position = browser.find_element_by_xpath("//*[@placeholder='Search jobs']").send_keys(job)
    location = browser.find_element_by_xpath("//*[@placeholder='Search location']").send_keys(location)
    validation_2 = browser.find_element_by_xpath("//*[@placeholder='Search location']").send_keys(Keys.ENTER)
    time.sleep(2)
    distance_options = browser.find_element_by_xpath('//*[@aria-controls="distance-facet-values"]').click()
    set_distance_to_10_miles = browser.find_element_by_xpath("//*[@for='distance-10']").click()
    apply_distance = browser.find_element_by_xpath("//*[@data-control-name='filter_pill_apply']").click()
    time.sleep(1.5)
    linkedin_features = browser.find_element_by_xpath("//*[@aria-label='LinkedIn Features filter. Clicking this button displays all LinkedIn Features filter options.']").click()
    easy_apply_only = browser.find_element_by_xpath("//*[@for='f_LF-f_AL']").click()
    validation_3 = browser.find_element_by_xpath("//*[@class='search-s-facet__values search-s-facet__values--is-floating search-s-facet__values--f_LF container-with-shadow']//*[@class='display-flex justify-flex-end mt4']/button[@data-control-name='filter_pill_apply']").click()
    time.sleep(1.5)
    pages = [browser.find_element_by_xpath(f'//*[@aria-label="Page {i}"]') for i in range (2,6)]

    ################### Here we go ! ##############################
    i = -1
    while i < 5:
        i += 1 
        offers = browser.find_elements_by_xpath('//*[@class="occludable-update artdeco-list__item--offset-4 artdeco-list__item p0 ember-view"]')
        for offer in offers:
            offer.click()
            time.sleep(1)
            easy_apply = browser.find_element_by_xpath("//*[@class='jobs-apply-button--top-card artdeco-button--3 artdeco-button--primary jobs-apply-button artdeco-button ember-view']").click()
            try:
                submit = browser.find_element_by_xpath('//button[@type="submit"]').click()
                time.sleep(1)
                close = browser.find_element_by_xpath('//*[@class="artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view"]').click()
                time.sleep(1)
            except: 
                continue
        pages[i].click()
        time.sleep(2)
