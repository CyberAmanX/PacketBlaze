import pyshark
print("Welcome to Wireshark-Mastery Analyzer!")
pcap = input("Enter PCAP path (e.g., pcaps/http_traffic.pcap): ")
cap = pyshark.FileCapture(pcap)
print("Choose: 1) List HTTP requests 2) Count packets")
choice = input("Enter 1 or 2: ")
if choice == "1":
    for pkt in cap:
        if "HTTP" in pkt:
            print(f"Request: {pkt.http.request_method} {pkt.http.request_uri}")
else:
    print(f"Total packets: {len(list(cap))}")
