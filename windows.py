import os
os.system("pip3 install scapy.all")
print("""

Coded By Bl4P
Tüm Sorumluluğu Kabul Ettiniz

""")
import scapy.all as scapy
os.system("figlet Ağ Tarayıcısı Başlatılıyor. ")
arp1 = scapy.ARP(pdst="10.0.2.1/24")
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
toplu = arp1/broadcast
(answered.list,unanswered.list) = scapy.all(toplu,timeuot=1)
answered.list.summary()