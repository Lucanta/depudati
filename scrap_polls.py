import re
from bs4 import BeautifulSoup
import numpy as np
from assign_id import assign_party_id

# define function to scrap poll results about voting intention
def scrap_poll_vi(browser,pollster):
    
    num_of_parties = 22
    poll_results = np.zeros(num_of_parties)
    
    if(pollster=='Emg Acqua'):
        
        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split(' /|/|/ |:|\n|\* |%',answer_text)

        for i in range(len(poll_results_list)):
            j = assign_party_id(poll_results_list[i])
            
            if(j!=0):     
                poll_value = float(poll_results_list[i+1].replace(',','.'))
                poll_results[j-1] = poll_value
                
    if(pollster=='tecnè srl' or pollster=='Tecnè Srl'):
 
        try:
            soup = BeautifulSoup(browser.page_source,"html.parser")
            table = soup.find_all('table')[3]
            rows = table.find_all('tr')
            for i in range(len(rows)):
                cols = rows[i].find_all('td')
                for j in range(len(cols)):
                    if(j==0): 
                        k = assign_party_id(cols[j].text)
                        if(k==0): break
                    if(j==1): 
                        cols[j] = cols[j].text.replace('%','')
                        cols[j] = cols[j].replace(',','.')
                        poll_results[k-1] = float(cols[j])

        except:
            answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
            print(answer_text)
        
            poll_results_list = re.split('\n',answer_text)
            print(poll_results_list)

            for i in range(len(poll_results_list)):
                j = assign_party_id(poll_results_list[i])
            
                if(j!=0):
                    try:
                        poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                    except:
                        poll_value = float(np.array(re.findall("\d+",poll_results_list[i])))
                    poll_results[j-1] = poll_value
    
    if(pollster=='SWG spa'): 

        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(str(poll_results_list[i].replace('%','')))
            
            if(j!=0):     
                print(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.')))
                try:
                    poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                except:
                    poll_value = float(np.array(re.findall("\d+",poll_results_list[i])))
                poll_results[j-1] = poll_value
                
    if(pollster=='Istituto Ixè S.r.l.'):
        
        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(str(poll_results_list[i]))
            
            if(j!=0):     
                poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                poll_results[j-1] = poll_value
                
    if(pollster=='Winpoll'):
        
        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(poll_results_list[i])
            
            if(j!=0):     
                poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                poll_results[j-1] = poll_value
                
    if(pollster=='Termometro Politico'):
        
        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(poll_results_list[i])
            
            if(j!=0):     
                poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                poll_results[j-1] = poll_value
                
    if(pollster=='Euromedia Research'):
        
        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(poll_results_list[i])
            
            if(j!=0):
                poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                poll_results[j-1] = poll_value
                
    if(pollster=='IndexResearch'):
        
        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(poll_results_list[i])
            
            if(j!=0):     
                poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                poll_results[j-1] = poll_value
                
    if(pollster=='Sondaggi Bidimedia - Bi3'):
    
        soup = BeautifulSoup(browser.page_source,"html.parser")
        table = soup.find_all('table')[3]
        rows = table.find_all('tr')
        for i in range(len(rows)):
            cols = rows[i].find_all('td')
            for j in range(len(cols)):
                if(j==0): 
                    k = assign_party_id(cols[j].text)
                    if(k==0): break
                if(j==1): 
                    cols[j] = cols[j].text.replace('%','')
                    cols[j] = cols[j].replace(',','.')
                    poll_results[k-1] = float(cols[j])

    if(pollster=='Demopolis - Istituto di Ricerche'):
        
        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(str(poll_results_list[i].replace('%','')))
            
            if(j!=0):     
                print(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.')))
                try:
                    poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                except:
                    values = np.array(re.findall("\d+",poll_results_list[i]))
                    if(len(values)>1): poll_value = float(values[1])
                    else: poll_value = values
                print(poll_value)
                poll_results[j-1] = poll_value
                
    if(pollster=='Quorum'):

        answer_text = browser.find_element_by_id("ctl00_Contenuto_ucGestioneDomande_ucSchedaDomandaReadOnly_Risposta").text
        print(answer_text)
        
        poll_results_list = re.split('\n',answer_text)
        print(poll_results_list)

        for i in range(len(poll_results_list)):
            j = assign_party_id(poll_results_list[i])
            
            if(j!=0):     
                poll_value = float(np.array(re.findall("\d+\.\d+",poll_results_list[i].replace(',','.'))))
                poll_results[j-1] = poll_value
            
    return poll_results

# define function to scrap poll results about government approval
#def scrap_poll_ga(pollster,text):
    
#   return poll_results
        