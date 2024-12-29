DNS Enumeration is a technique used to RECONNAISSANCE


DNS enumeration is critical for cybersecurity, enabling identification of all DNS records associated with a domain to discover vulnerabilities, map a company’s internet-connected devices, and expose hidden services.

It returns important information about the target, such as DNS records, host names, IP addresses, etc. 


nmap -sSU -p 8080 --script dns-nsec-enum --script-args dns-nsec-enum.domains=brave.com <TARGET>





![image](https://github.com/user-attachments/assets/4813ef3e-15ee-4eaa-a966-afb5582521cb)



Ouput:
