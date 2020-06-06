# main libraries
from datetime import datetime
from selenium import webdriver
from import_poll import import_polls

# define website url
url = 'http://www.sondaggipoliticoelettorali.it'

# import data_inserimento from command line
data_inserimento = '05/06/2020'

# file string name
vi_filename_csv = 'voting_intention_polls.csv'

# vote intention strings
vi_string = ['elezioni politiche','elezioni nazionali','Elezioni Politiche','elezioni Politiche','Camera dei Deputati','il consenso ai partiti','se si votasse oggi']

#soup = BeautifulSoup(url.content, 'html.parser')

# load crome webdiver 
options = webdriver.ChromeOptions()
browser = webdriver.Chrome('bin/chromedriver')

# open browser
browser.get(url)

main_window = browser.current_window_handle

# click on 'SONDAGGI' button
SONDAGGI_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div/ul/li[3]/a')
SONDAGGI_button.click()

CONTROL = 0
pg = 1

while CONTROL!=1:
    
    # Find polls inserted on data_inserimento
    top_date_str = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/input').get_attribute('title')
    bottom_date_str = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[13]/td[1]/div/input').get_attribute('title')
    top_date = datetime.strptime(top_date_str,'%d/%m/%Y')
    bottom_date = datetime.strptime(bottom_date_str,'%d/%m/%Y')
    insertion_date  = datetime.strptime(data_inserimento, '%d/%m/%Y')

    # Create list of polls inserted on data_inserimento                                     
    list_polls_avail = browser.find_elements_by_xpath('//*[@title="'+data_inserimento+'"]')

    # count number of polls available for a specific data_inserimento
    no_polls_avail = len(list_polls_avail)
    
    if(insertion_date>bottom_date and no_polls_avail == 0):
        print('There are no polls inserted on '+data_inserimento)
        break
    
    if(insertion_date<bottom_date and no_polls_avail == 0):
        # click to go to next page
        if(pg==1): NEXTPAGE_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tfoot/tr/td/span[2]/input[3]')
        if(pg==2): NEXTPAGE_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tfoot/tr/td/span[2]/input[4]')
        if(pg>2): NEXTPAGE_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tfoot/tr/td/span[2]/input[5]')
        NEXTPAGE_button.click()
        pg += 1
        continue
    
    #print('I am importing the polls here, outside any ifs')
    import_polls(no_polls_avail,list_polls_avail,browser,main_window,vi_string,vi_filename_csv)
    
    if(insertion_date == bottom_date):
        # click to go to next page
        if(pg==1): NEXTPAGE_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tfoot/tr/td/span[2]/input[3]')
        if(pg==2): NEXTPAGE_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tfoot/tr/td/span[2]/input[4]')
        if(pg>2): NEXTPAGE_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div/table/tfoot/tr/td/span[2]/input[5]')
        NEXTPAGE_button.click()
        pg += 1
        continue
    else:
        CONTROL = 1
        
# close browser    
browser.quit()