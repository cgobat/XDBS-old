import numpy as np
import pandas as pd

def hms_to_dec(hms):
    h,m,s = pd.to_numeric(hms.split()) # hms will always be between 0 and +24 hours
    deg = ((s/60 + m)/60 + h)*15 # 360 degrees/24 hours = 15 deg/hr
    return float(deg)
    
def dms_to_dec(dms):
    if dms[0] == "-": # since negative degrees are possible
        sign = -1
    else:
        sign = 1
    d,m,s = pd.to_numeric(dms.split())    
    deg = sign*((s/60 + m)/60 + np.abs(d)) # use magnitudes only and reapply sign after
    return float(deg)