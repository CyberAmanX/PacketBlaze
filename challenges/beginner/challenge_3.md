# Beginner Challenge 3: Filter UDP Traffic

**Case File: The DNS Dilemma** 🕵️‍♂️  
A website’s loading slowly, and the network admin suspects DNS issues. Your mission: Capture and filter UDP packets to uncover the truth!

## Objective
Learn to filter UDP packets in Wireshark to analyze lightweight network traffic, like DNS queries.

## Prerequisites
- Wireshark installed ([download](https://www.wireshark.org/download.html)).
- A terminal (e.g., `bash` on Linux, `cmd` on Windows).
- Internet access for DNS traffic.

## Steps
1. Open Wireshark and select your active network interface (e.g., Wi-Fi or eth0).
2. Start capturing packets.
3. In a terminal, run `nslookup example.com` to generate DNS traffic (UDP-based).
4. In Wireshark, apply the filter `udp` to show only UDP packets.
5. Stop the capture after 10 seconds.
6. Save your capture as `udp_traffic.pcap` in the `pcaps/` folder.

## Common Challenges
- **Issue**: No UDP packets appear.
  - **Fix**: Ensure `nslookup` ran and you’re on the correct interface.
- **Issue**: Filter errors (e.g., “invalid filter”).
  - **Fix**: Use lowercase `udp` (not `UDP`).

## Learning Outcomes
- Apply the `udp` filter to isolate UDP traffic.
- Recognize UDP packet structure (e.g., source/destination ports).
- Save PCAPs for analysis.

## PCAP
Use our sample: [udp_traffic.pcap](../../../pcaps/udp_traffic.pcap).  
*Note*: Synthetic for educational use.

## Bonus Task
- Filter DNS specifically with `udp.port == 53` and count queries.
- Share your count in [Discussions](https://github.com/yourusername/PacketBlaze/discussions) to earn the 🔥 **Flame Master** badge!

## Solution
Stuck? See the [detailed solution](solutions/solution_3.md) with screenshots.

## Reward
Complete this to unlock progress toward the 🧨 **Blaze Starter** badge! Check [Badges](../../../docs/badges.md).

---

[Back to Challenges](../../../README.md#challenges) | [Next Challenge](challenge_4.md)