import re

dosya=open("C:/Users/Mehmet Filiz/PycharmProjects/LogAnalizi/Log_Analizi_Yüklenicek.txt","r")

pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
pattern2= r"(\b[\w\-\.]*\.exe\b)"
pattern3= r'https?://\S+'

exe_lst=[]
ip_add_lst=[]
site_lst=[]
for log in dosya:
     ip_add = re.search(pattern, log)
     exe=re.search(pattern2,log)
     site=re.search(pattern3,log)
     if exe is not None:
           exe_lst.append(exe)
     if ip_add is not None:
           ip_add_lst.append(ip_add)
     if site is not None:
           site_lst.append(site)

print(exe_lst)
print(ip_add_lst)
print(site_lst)
