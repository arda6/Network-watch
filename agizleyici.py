import os
os.system("apt install figlet")
os.system("clear")
os.system("figlet Hoşgeldiniz.")
os.system("pip3 install scapy.all")
os.system("clear")
os.system("figlet Hoşgeldiniz")
print("""

Coded By Bl4P
Tüm Sorumluluğu Kabul Ettiniz

""")
import scapy.all as scapy
os.system("figlet Ağ Tarayıcısı Başlatılıyor. ")
arp1 = scapy.ARP(pdst="10.0.2.1/24")
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
toplu = arp1/broadcast
(answered_list,unanswered_list) = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")(/scapy.srp(toplu,timeuot=1)
answered_list.summary()