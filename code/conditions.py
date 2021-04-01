#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:38:56 2021

@author: timur
"""

import gc
import time

gc.collect()


start_time = time.time()


x=0

k=1
z=1
y=1
w=1
for i in range(10000000):
    
    if(k == True and z == True):
        x+=(int(k == True)*int(w == True))
        
        if(y == True and w == True):
            x+=(int(y == True)*int(z == True))
            
            if(k == True and z == True):
                x+=(int(k == True)*int(w == True))
                
                
                
                if(k == True and z == True):
                    x+=(int(k == True)*int(w == True))
                    
                    if(y == True and w == True):
                        x+=(int(y == True)*int(z == True))
                        
                        if(k == True and z == True):
                            x+=(int(k == True)*int(w == True))
                            
                            
                            
                        else:
                            x+=(int(k == True)*int(w == True))
                            
                    else:
                        x+=(int(y == True)*int(z == True))
                    
                else:
                    x+=(int(k == True)*int(w == True))
                
                
                
                
            else:
                x+=(int(k == True)*int(w == True))
                
        else:
            x+=(int(y == True)*int(z == True))
        
    else:
        x+=(int(k == True)*int(w == True))
print(x)

end_time = time.time()
print(f"time in seconds: {end_time - start_time}")