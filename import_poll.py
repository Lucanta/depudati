# main libraries
import os
import re
import time
from selenium.webdriver.common.keys import Keys
from scrap_polls import scrap_poll_vi
#from assign_id import write_poll_to_csv
from write_to_file import write_poll_to_csv, write_poll_to_SQL, write_metadata_to_SQL, write_question_to_SQL

def import_polls(no_polls_avail,list_polls_avail,browser,main_window,vi_string,vi_filename_csv):
    
    # Loop over polls and open a new browser tab for each one
    for i in range(no_polls_avail):
        list_polls_avail[i].send_keys(Keys.CONTROL+Keys.RETURN)
        time.sleep(2)
    
        # Switch to new tab and store information about the poll
        browser.switch_to.window(browser.window_handles[-1])
        pollster_name = browser.find_element_by_id("ctl00_Contenuto_ucGestioneSondaggio_ucDatiSondaggioReadOnly_Realizzatore").text
        start_date_fw = browser.find_element_by_id("ctl00_Contenuto_ucGestioneSondaggio_ucDatiSondaggioReadOnly_DataRealizzazioneDa").text
        end_date_fw = browser.find_element_by_id("ctl00_Contenuto_ucGestioneSondaggio_ucDatiSondaggioReadOnly_DataRealizzazioneA").text
        sample_size = browser.find_element_by_id("ctl00_Contenuto_ucGestioneSondaggio_ucDatiSondaggioReadOnly_Campione_Intervistati").text
        method = browser.find_element_by_id("ctl00_Contenuto_ucGestioneSondaggio_ucDatiSondaggioReadOnly_Metodo_Raccolta_Informazioni").text
        
        # Check poll number through pdf file name
        SCARICA_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div/div/div[2]/div/a')
        SCARICA_button.click()
        time.sleep(2)
        # open a new tab
        browser.execute_script("window.open()")
        time.sleep(2)
        # switch to new tab
        browser.switch_to.window(browser.window_handles[2])
        # navigate to chrome downloads
        browser.get('chrome://downloads')
        # get file name
        poll_name = browser.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
        print(poll_name)
        poll_id = int(poll_name.replace("Sondaggio","").replace(".pdf",""))
        print(poll_id)
        # close the download tab and go back to previous tab
        browser.close()
        browser.switch_to.window(browser.window_handles[1])
    
        # remove downloaded polls (pdf files)
        os.remove('/localhome/mmlca/Downloads/'+poll_name)
        
        # Add metadata about poll to SQL database
        db_path = 'sql_db/ItalianPolls.db'
        table_metadata = "polls_metadata"
        table_questions = 'polls_questions'
        table_data = 'polls_data'
        write_metadata_to_SQL(db_path,table_metadata,poll_id,pollster_name,start_date_fw.replace("/","-"),end_date_fw.replace("/","-"),sample_size,method)
        
        # Go to the 'Domande' section
        DOMANDE_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[1]/div[2]/div[2]/input[2]')
        DOMANDE_button.click()
        
        # Check how many questions there are
        no_questions_text = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/table/tfoot/tr/td/span[1]').text
        no_questions = max(list(map(int,re.findall("\d+",no_questions_text))))
    #    no_questions = int(no_questions_text[15])
        print(no_questions)
        
        # Check if it is a poll about voting intention
        for j in range(no_questions):
            if(j+1>5 and j+1<11 and ((j+1)%5)==1): browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/table/tfoot/tr/td/span[2]/input[3]').click()
            if(j+1>10 and j+1<16 and ((j+1)%5)==1): browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/table/tfoot/tr/td/span[2]/input[4]').click()
            if(j+1>15 and ((j+1)%5)==1): browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/table/tfoot/tr/td/span[2]/input[5]').click()
            question_id = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucListaDomande_dgDomande_Row"+str(j%5+1)+"_Domanda")
            question_text = question_id.get_attribute("value")
            print(question_text)
            # Open question about voting intention if present
            if any(x in question_text for x in vi_string):
                write_question_to_SQL(db_path,table_questions,poll_id,j+1,question_text)
                question_id.click()
                poll_results = scrap_poll_vi(browser,pollster_name)
                print(poll_results)
                # Write results on a csv file
                write_poll_to_csv(poll_id,j+1,poll_results,vi_filename_csv,23)
                write_poll_to_SQL(db_path,table_data,poll_id,j+1,23,poll_results)
                
        time.sleep(2)
        # close tab and return to main window
        browser.close()
        browser.switch_to.window(main_window)

