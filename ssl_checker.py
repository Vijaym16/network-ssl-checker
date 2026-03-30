import ssl
import socket
from datetime import datetime

def get_ssl_info(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            
    print(f"\n SSL Certificate Information for {hostname}\n")

    #issuer
    issuer = dict(x[0] for x in cert['issuer'])
    print("Issuer:", issuer.get('organizationName'))

    #Expiry Date
    expiry_date = cert['notAfter']
    print("Expiry Date:", expiry_date)

    #Convert expiry date to readable format
    expiry_dt = datetime.strptime(expiry_date, '%b %d %H:%M:%S %Y %Z')
    days_left = (expiry_dt - datetime.now()).days
    print("Days Left:", days_left)

    #Validity check
    if days_left > 0:
        print("Status: Valid")
    else:
        print("Status: Expired")

if __name__ == "__main__":
    target = input("Enter the hostname (e.g., www.example.com): ")
    get_ssl_info(target)    