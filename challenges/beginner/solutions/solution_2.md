# Solution: Beginner Challenge 2 - Filter ICMP Packets

**Case File: The Ping Mystery** 🕵️‍♂️  
This guide solves [Challenge 2](../challenge_2.md), showing you how to capture and filter ICMP packets to investigate a possible ping flood. Follow along with screenshots to crack the case!

## Objective
Filter ICMP packets in Wireshark to analyze ping traffic.

## Prerequisites
- Wireshark installed ([download](https://www.wireshark.org/download.html)).
- A terminal (e.g., \`cmd\` on Windows, \`Terminal\` on macOS/Linux).
- Network access.

## Step-by-Step Solution

### 1. Open Wireshark
Launch Wireshark to see the interface list.

![Wireshark Startup](../../../assets/beginner_ch2_wireshark_startup.png "Wireshark main window with interfaces")

### 2. Select Active Interface
Choose your active interface (e.g., Wi-Fi or eth0) showing packet activity. Double-click to select.

![Interface Selection](../../../assets/beginner_ch2_interface_selection.png "Selecting Wi-Fi interface with activity")

**Troubleshooting**:
- **Issue**: No interfaces listed.
- **Fix**: Install Npcap (Windows) or run \`sudo wireshark\` (Linux).

### 3. Start Capturing Packets
Click the blue shark fin (or \`Ctrl+E\`) to start capturing.

![Start Capture](../../../assets/beginner_ch2_start_capture.png "Wireshark capturing packets")

### 4. Generate ICMP Traffic
Open a terminal and run:
\`\`\`bash
ping example.com
\`\`\`
This sends ICMP Echo Requests to example.com, generating traffic.

![Ping Command](../../../assets/beginner_ch2_ping_command.png "Terminal running ping example.com")

**Troubleshooting**:
- **Issue**: Ping fails (e.g., “Request timed out”).
- **Fix**: Try \`ping 8.8.8.8\` (Google’s DNS) or check your network.

### 5. Apply ICMP Filter
In Wireshark’s filter bar, type \`icmp\` and press Enter. Only ICMP packets (e.g., Echo Request/Reply) will appear.

![ICMP Filter](../../../assets/beginner_ch2_icmp_filter.png "Wireshark with icmp filter applied")

**Troubleshooting**:
- **Issue**: No packets after filtering.
- **Fix**: Ensure ping is active and filter is \`icmp\` (lowercase).

### 6. Stop and Save Capture
After 10–15 seconds, click the red square (or \`Ctrl+E\`) to stop. Save via \`File > Save As\`, naming it \`icmp_traffic.pcap\` in \`pcaps/\`.

![Save PCAP](../../../assets/beginner_ch2_save_pcap.png "Saving capture as icmp_traffic.pcap")

## Sample PCAP
Download: [icmp_traffic.pcap](../../../pcaps/icmp_traffic.pcap).

## Analysis
- **Packet Types**: Look for \`Echo Request\` and \`Echo Reply\` in the Packet Details pane.
- **Details**: Check source (your IP) and destination (example.com’s IP).
- **Stats**: Use \`Statistics > Protocol Hierarchy\` to confirm ICMP traffic.

![Packet Details](../../../assets/beginner_ch2_packet_details.png "ICMP Echo Request details in Wireshark")

## Common Issues and Fixes
- **Issue**: Captured other protocols (e.g., DNS).
  - **Fix**: Reapply \`icmp\` filter or clear filter (\`Ctrl+/\`) to check capture.
- **Issue**: Ping blocked by firewall.
  - **Fix**: Try a different target (e.g., \`ping 1.1.1.1\`) or disable firewall temporarily.

## Bonus Task Solution
- Open \`Statistics > Packet Lengths\`.
- Filter for \`icmp.type == 8\` (Echo Request) and \`icmp.type == 0\` (Echo Reply) to count each.
- Example: “Found 10 Requests, 10 Replies.”
- Share in [Discussions](https://github.com/yourusername/Wireshark-Mastery/discussions) to earn 🦈 **Shark’s Approval**!

## Learning Outcomes
- **Filters**: Used \`icmp\` to isolate traffic.
- **ICMP Basics**: Identified Request/Reply packets.
- **Analysis**: Saved and reviewed a PCAP.

## Interactive Demo
Try our [Packet Analyzer](../../../scripts/interactive_analyzer.py) to count ICMP packets:
\`\`\`bash
python scripts/interactive_analyzer.py
\`\`\`

---

[Back to Challenge](../challenge_2.md) | [All Challenges](../../../README.md#challenges)

**Found a better way?** Submit a PR to improve this solution and earn a 🤝 **Community Star** badge!

