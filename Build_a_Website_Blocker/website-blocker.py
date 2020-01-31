import time as t
from datetime import datetime as dt

host_temp = '/Users/vishvajeetsingh/Project/Python/py-code/Build_a_Website_Blocker/hosts'
host_path = '/etc/hosts'
redirect = "127.0.0.1"
website_list = ["facebook.com" , "www.facebook.com"]

while True:
    if dt(dt.now().year , dt.now().month , dt.now().day ,8) < dt.now() <  dt(dt.now().year , dt.now().month , dt.now().day ,16):
       print("Working Time")
       with open(host_temp,'r+') as file:
           content = file.read()
           for website in website_list:
               if website in content:
                   pass
               else :
                   file.write(redirect+" "+website+"\n") 
    else :
       print("Fun Time")
       with open(host_temp ,'r+')
           content = file.readlines()
           file.seek(0)
           for line in content:
               if not any (website in line for website in website_list):
                   file.write(line)
            file.truncate()
        print("Fun hours...")
    t.sleep(5) 
    