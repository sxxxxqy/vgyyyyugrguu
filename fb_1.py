#coding by : hudaxcode
import re, os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup as bs
import requests

def cari_gc():
    req = requests.Session()
    basee_url = "https://mbasic.facebook.com" 
    url_gc  = "https://mbasic.facebook.com/search/top/?q=grup+ml&refid=8&_rdr"
    cookie  = {"cookie":"datr=SltcYa6J5SHkCxp5bq9-rvHi;sb=WVtcYbQ8peUE6HVOT_1QeCAj;fr=0HCOjbefbnbVE6RbH.AWXdvtqIl-DEVukhC4Z2hHBpL1A.BhXFtR.c7.AAA.0.0.BhvE6R.AWW4AlOlZRA;c_user=100075772737215;xs=34%3ARPVWSJ8l_q0a7A%3A2%3A1639730841%3A-1%3A-1;m_pixel_ratio=1.59375;wd=452x864;x-referer=eyJyIjoiL3Byb2ZpbGUucGhwIiwiaCI6Ii9wcm9maWxlLnBocCIsInMiOiJtIn0%3D;"}
    data_gc = req.get(url_gc,cookies=cookie).content
    data_bs = bs(data_gc,"html.parser")
    data_id = data_bs('a')
    section = data_bs
    for url in section.find_all("a"):
        for nekx in url:
            try:
                nx = url.get('href')
            except:
                pass
            try:
                if not "/graphsearch/str" in nx:
                    pass
                if not "keywords_groups?" in nx:
                    pass
                else:
                    next = nx
            except:
                pass 
    for link in data_bs('a'):
        for x  in link:
            try:
                c = link["href"]
            except:
                pass
            if not "https://mbasic.facebook.com/groups" in c:
                pass
            else:
                with open("data_url.txt",'a') as w:
                    w.write(c+"\n")
                print(c)
    new_url = basee_url + next
    nex_1   = req.get(new_url,cookies=cookie).content
    nex_bs  = bs(nex_1, "html.parser")
    sec_nex = nex_bs
    for url_1 in sec_nex.find_all("a"):
        for z in url_1:
            try:
                nx_1 = url_1.get('href')
            except:
                pass
            try:
                if not "/graphsearch/str" in nx_1:
                    pass
                if not "keywords_groups?" in nx_1:
                    pass
                else:
                    next_2 = nx_1
            except:
                pass 
    for ex in nex_bs('a'):
        for x  in ex:
            try:
                dx = ex["href"]
            except:
                pass
            if not "https://mbasic.facebook.com/groups" in dx:
                pass
            else:
                with open("data_url.txt",'a') as w:
                    w.write(dx+"\n")
                print(dx)
    
    new_url_2 = next_2
    nex_2     = req.get(new_url_2,cookies=cookie).content
    nex_bs_2  = bs(nex_2, "html.parser")
    sec_nex   = nex_bs_2
    for ex_1 in nex_bs('a'):
        for x  in ex_1:
            try:
                dx_1 = ex_1["href"]
            except:
                pass
            if not "https://mbasic.facebook.com/groups" in dx_1:
                pass
            else:
                with open("data_url.txt",'a') as w:
                    w.write(dx_1+"\n")
                print(dx_1)
   
def scrap_all():
    req = requests.Session()
    cookie  = {"cookie":"datr=SltcYa6J5SHkCxp5bq9-rvHi;sb=WVtcYbQ8peUE6HVOT_1QeCAj;fr=0HCOjbefbnbVE6RbH.AWXdvtqIl-DEVukhC4Z2hHBpL1A.BhXFtR.c7.AAA.0.0.BhvE6R.AWW4AlOlZRA;c_user=100075772737215;xs=34%3ARPVWSJ8l_q0a7A%3A2%3A1639730841%3A-1%3A-1;m_pixel_ratio=1.59375;wd=452x864;x-referer=eyJyIjoiL3Byb2ZpbGUucGhwIiwiaCI6Ii9wcm9maWxlLnBocCIsInMiOiJtIn0%3D;"}
    base_url = "https://mbasic.facebook.com/groups/680672546105026?view=info"
    hx_gwt = req.get(base_url,cookies=cookie).content
    info   = bs(hx_gwt, "html.parser")
    for td in info.find_all('td'):
        print(td)   
   
   
def remove_dup_gc():
    input_file ="data_url.txt"
    output_file = "url.txt"
    seen_lines = set()
    outfile = open(str(output_file), "w")
    for line in open(str(input_file), "r"):
        if line not in seen_lines:
            outfile.write(line)
            seen_lines.add(line)

try:
    os.remove("data_url.txt")
    os.remove("url.txt")
except:
    pass

scrap_all()
#cari_gc()
#remove_dup_gc()