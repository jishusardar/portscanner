import socket
import csv
from datetime import datetime
from tqdm import tqdm

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return "127.0.0.1" 
maxport=65535
def scans(ip_addr):
    flag=True
    for ports in tqdm(range(0, maxport+1), desc="Scanning Ports"):
        if open_ports(ipaddr,ports):
            print(f"\n [+] Port: {ports} is Opened\n")
            report(ip_addr,ports)
            if flag:
                flag=False
    
    if flag:
        print("No Ports are in Use")
        
def open_ports(ipaddr,port)->bool:
    try:
        s=socket.socket()
        s.settimeout(0.5)
        s.connect((ipaddr,port))
        s.close()
        return True
    except:
        return False
    
def report(ipaddrr,ports):
    with open("report.csv", 'a', newline='') as reportfile:
        writer=csv.writer(reportfile)
        current_datetime = datetime.now()
        writer.writerow([str(current_datetime),str(ipaddrr),str(ports)])

if __name__== "__main__":
    ipaddr=get_host_ip()
    print("Scanning for open Ports target: " + ipaddr)
    scans(ipaddr)
    print("You can Find The Report File In This: portscanner/report.csv")