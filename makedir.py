import datetime
tod = datetime.date.today()
strtod = tod.strftime("%Y%m%d")

import os

todfolder = tod.strftime("%Y%m%d")

import os 
dir  = os.environ['USERPROFILE'] + "\\logfile\\" + todfolder + "\\"
if not os.path.exists(dir):
     os.mkdir(dir)
else:
     print("フォルダ01あり")


