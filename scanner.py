#!/usr/bin/python
import sys
import os

ip_address = sys.argv[1]
file_name = sys.argv[2]

ip_file = open("ip_file", "w")
ip_file.write(ip_address)
ip_file.close()


def scan_name(name):
        file = open(file_name, "a")
        file.write("\n\n\n\n\n"+" "*40+"#"*40+" "*30+"\n")
        i = 0
        while i < 5 :
                if i == 2 :
                        file.write(" "*40+ "#"+ " "*14+name+ " "*14 +"#"+ " "*30+"\n")
                        i += 1
                        continue

                file.write(" "*40+ "#"+" "*38+"#"+" "*30+"\n")

                i += 1
        file.write(" "*40+"#"*40+" "*30+"\n")
        file.close()

scan_name("NMAP SCAN ")
nmap_scan = "nmap -sC -A -O -sV -n -v -v {} >> {} ".format(ip_address,file_name)
nikto_scan = "echo y | nikto -h {} >> {}".format(ip_address,file_name)
os.system(nmap_scan)
scan_name("NIKTO SCAN")
os.system(nikto_scan)
