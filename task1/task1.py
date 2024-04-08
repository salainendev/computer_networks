import requests
import csv
import socket


domains = [
    "google.com",
    "amazon.com",
    "facebook.com",
    "pornhub.com",
    "twitter.com",
    "instagram.com",
    "linkedin.com",
    "reddit.com",
    "youtube.com",
    "microsoft.com"
]


def ping_domain(domain):
    try:
        response = requests.get("http://" + domain, timeout=5)  
        site_ip = socket.gethostbyname(domain)
        return ("Success",site_ip) if response.status_code == 200 else ("Failed",-1)
    except requests.exceptions.RequestException as e:
        return "Failed",-1


with open("ping_results.csv", "w", newline="") as csvfile:
    fieldnames = ["Domain", "Result","Ip"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for domain in domains:
        result, site_ip = ping_domain(domain)
        print(f"Соединение с http://{domain}...")
        writer.writerow({"Domain": domain, "Result": result ,"Ip":site_ip})

print("Результаты пинга сохранены в ping_results.csv")
