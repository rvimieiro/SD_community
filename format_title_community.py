import pandas as pd
with open('./Downloads/TitulosGrupoARXIV_IA_PageRank.csv') as f:                 
        d = list()                                                          
        for line in f:                                                      
            x = line.replace('\n','').strip().split(';')                    
            d.extend([{'title':a,'community':x[0].replace('Grupo ','')} for a in x[1:] if a != '']) 
pd.DataFrame(d,columns=['title','community']).to_csv('SD_community/titulo_doc_comunidade_pagerank.csv',index=False,header=True,sep=';')

with open('./Downloads/TitulosGrupoARXIV_IA_Degree.csv') as f:                 
        d = list()                                                          
        for line in f:                                                      
            x = line.replace('\n','').strip().split(';')                    
            d.extend([{'title':a,'community':x[0].replace('Grupo ','')} for a in x[1:] if a != '']) 
pd.DataFrame(d,columns=['title','community']).to_csv('SD_community/titulo_doc_comunidade_degree.csv',index=False,header=True,sep=';')
