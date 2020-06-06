import pandas as pd
import numpy as np
from os import path

def assign_party_id(party_str):
    
    # list each party string in alphabetical order
    az_str = ['Azione','azione','AZIONE','Azione di Calenda','Azione-C. Calenda']
    az_id = 1
    altr_str = ['Altro partito','Altri partiti','Altri','ALTRA LISTA','Altro','altri']
    altr_id = 2
    ev_str = ['Europa Verde','verdi','Verdi','VERDI','I Verdi','Federazione dei Verdi-Europa verde']
    ev_id = 3
    fdi_str = ['Fratelli d\'Italia','Fratelli dâ€™Italia','FdI','FRATELLI D\'ITALIA','Fratelli d’Italia-Meloni','fdi','Fratelli d’Italia']
    fdi_id = 4
    fi_str = ['Forza Italia','Forza italia','fi','FI','FORZA ITALIA','Forza Italia-Berlusconi']
    fi_id = 5    
    indnv_str = ['Indecisi+non voto','astensione/incerti','NON SI ESPRIME','Indecisi/astenuti','INDECISI - ASTENSIONE']
    indnv_id = 6
    iv_str = ['Italia Viva','Italia viva','IV','ITALIA VIVA','Italia Viva-M.Renzi','iv','Iv']
    iv_id = 7
    las_str = ['La Sinistra','Sinistra','SINISTRA IT./MDP ART.1','La sinistra','Sinistra/MDP/Articolo 1','la sinistra','Sin-LeU']
    las_id = 8
    lega_str = ['Lega','LEGA','Lega – Salvini','Lega-Salvini Premier','lega']
    lega_id = 9
    m5s_str = ['Movimento 5 stelle','MOVIMENTO 5 STELLE','Movimento 5 Stelle','M5S','m5s']
    m5s_id = 10
    pd_str = ['Partito Democratico','Partito democratico','PARTITO DEMOCRATICO','pd','PD','Partito Democratico-PSE']
    pd_id = 11 
    piue_str = ['Più Europa','PiÃ¹ Europa','+ Europa','+EUROPA','+Europa','+europa','più Europa']
    piue_id = 12
    pap_str = ['Potere al Popolo','Partito Comunista/pap']
    pap_id = 13
    camb_str = ['CAMBIAMO!','Cambiamo','Cambiamo!']
    camb_id = 14
    pc_str = ['Partito Comunista di Rizzo','Partito Comunista/pap']
    pc_id = 15
    mdp_str = ['SINISTRA IT./MDP ART.1','Sinistra/MDP/Articolo 1','MDP-Articolo 1']
    mdp_id = 16
    leu_str = ['Liberi e Uguali']
    leu_id = 17
    pdf_str = ['Il Popolo della Famiglia']
    pdf_id = 18
    svp_str = ['SVP - UV']
    svp_id = 19
    altsx_str = ['Altri di Sinistra']
    altsx_id = 20
    ind_str = ['Indecisi']
    ind_id = 21
    aff_str = ['Affluenza']
    aff_id = 22
    lcon_str = ['La lista di Giuseppe Conte']
    lcon_id = 23


    # the order here is important because of the substring possibly present in multiple party names (e.g. 'azione' in 'Federazione', etc)
    if any( x in party_str for x in ev_str): party_id = ev_id    
    elif any(x in party_str for x in az_str): party_id = az_id
    elif any( x in party_str for x in altr_str): party_id = altr_id
    elif any( x in party_str for x in fdi_str): party_id = fdi_id
    elif any( x in party_str for x in fi_str): party_id = fi_id
    elif any( x in party_str for x in indnv_str): party_id = indnv_id
    elif any( x in party_str for x in iv_str): party_id = iv_id 
    elif any( x in party_str for x in las_str): party_id = las_id
    elif any( x in party_str for x in lega_str): party_id = lega_id  
    elif any( x in party_str for x in m5s_str): party_id = m5s_id
    elif any( x in party_str for x in piue_str): party_id = piue_id    
    elif any( x in party_str for x in pd_str): party_id = pd_id
    elif any( x in party_str for x in pap_str): party_id = pap_id
    elif any( x in party_str for x in camb_str): party_id = camb_id
    elif any( x in party_str for x in pc_str): party_id = pc_id
    elif any( x in party_str for x in leu_str): party_id = leu_id
    elif any( x in party_str for x in pdf_str): party_id = pdf_id
    elif any( x in party_str for x in svp_str): party_id = svp_id
    elif any( x in party_str for x in altsx_str): party_id = altsx_id
    elif any( x in party_str for x in ind_str): party_id = ind_id
    elif any( x in party_str for x in aff_str): party_id = aff_id
    elif any( x in party_str for x in lcon_str): party_id = lcon_id
    else: party_id = 0
        
    return party_id

def write_poll_to_csv(poll_id,poll_results,filename,no_of_parties):
    
    if(path.exists(filename)):
        # Check if poll_id is already present in csv file
        dataframe = pd.read_csv(filename,header=None,delimiter=';',usecols=list(range(no_of_parties+1)),error_bad_lines=False)
        is_poll_in_file = poll_id in dataframe[0].unique()
    
        if not is_poll_in_file:
            row_to_add = pd.Series(np.append(poll_id,poll_results))
            print(row_to_add)
            dataframe = dataframe.append(row_to_add,ignore_index=True)
            dataframe.to_csv(filename,header=None,index=False,index_label=False,sep=';',line_terminator='\n')
            
    else:
        print(poll_results)
        row_to_add = pd.DataFrame([np.append(poll_id,poll_results)],index=None,columns=range(no_of_parties+1))
        print(row_to_add)
        row_to_add.to_csv(filename,header=None,index=False,index_label=False,columns=range(no_of_parties+1),sep=';',line_terminator='\n')