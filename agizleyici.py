import os
os.system("apt install figlet")
os.system("clear")
os.system("figlet Hoşgeldiniz.")
os.system("pip3 install requests")
os.system("clear")
os.system("figlet Hoşgeldiniz")
pirnt("""

Coded By Bl4P
Tüm Sorumluluğu Kabul Ettiniz

""")
import scapy.all as scapy
os.system("Figlet Ağ Tarayıcısı Başlatılıyor. ")
arp1 = scapy.ARP(pdst="10.0.2.1/24")
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
toplu = arp1/broadcast
(answered.list,unanswered.list) = scapy.srt(toplu,timeuot=1)
answered.list.summary()