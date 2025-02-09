import requests
import datetime
import threading
import time
import html
p = ""

def c(d):
    global p
    for i in range(3):
        try:
            c = requests.get("https://openosv.net/osv/poll").text
            time.sleep(d)
            if c != "" and not c in "!Archive-Denial":
                if c != p:
                    
                    if len(c) > 500:
                        c = c[:500]+"(長いので省略)"
                    
                    c = html.unescape(c).replace("\n"," \\n ")
                    
                    
                    open(datetime.datetime.now().strftime("%Y-%m-%d.txt"),"a").write(
                        c[1:]+"\n"
                    )
                    p = c        
        except:
            pass
        
c(0.1)