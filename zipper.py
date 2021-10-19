'''
Created on 17 Mar 2021

@author: thomasgumbricht
'''

import os
import zipfile
import gzip
import shutil
from fnmatch import fnmatch


def UnZip(zipFPN, dstFP, dstFN, pattern):    
    ''' Unzip 
    '''   
             
    zipF = zipfile.ZipFile(zipFPN, "r")
    
    fL =  zipF.namelist()
    
    dstFPN = False
    
    #compstr is the string to look for in the zipfile
    for item in fL:
        
        if pattern in item:
                        
            #fN = os.path.split(item)[1]
            
            source = zipF.open(item)
            
            dstFPN = os.path.join(dstFP, dstFN)
            
            if not os.path.isfile(dstFPN):
                
                print ('unzipping to',dstFPN)
                
                with open(dstFPN, 'wb') as dest:

                    shutil.copyfileobj(source, dest)

            break

    return dstFPN