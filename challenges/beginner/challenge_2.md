# Beginner Challenge 2: Filter ICMP Packets

**Case File: The Ping Mystery** 🕵️‍♂️  
A server’s acting up, and the network admin suspects a *ping flood*. Your mission: Capture and filter ICMP packets to investigate!

## Objective
Learn to filter ICMP packets in Wireshark to identify ping traffic.

## Prerequisites
- Wireshark installed ([download](https://www.wireshark.org/download.html)).
- A terminal or command prompt (e.g., `cmd` on Windows, `Terminal` on macOS/Linux).
- Network access (Wi-Fi or Ethernet).

## Steps
1. Open Wireshark and select your active network interface (e.g., Wi-Fi or eth0).
2. Start capturing packets.
3. In a terminal, run `ping example.com` to generate ICMP traffic.
4. In Wireshark, apply the filter `icmp` to show only ICMP packets.
5. Stop the capture after 10–15 seconds.
6. Save your capture as `icmp_traffic.pcap` in the `pcaps/` folder.

## Common Challenges
- **Issue**: No ICMP packets appear after filtering.
  - **Fix**: Ensure `ping` is running and you’re using the correct interface.
- **Issue**: Filter shows errors (e.g., “invalid filter”).
  - **Fix**: Use lowercase `icmp` (not `ICMP` or `ping`).

## Learning Outcomes
- Apply the `icmp` filter to isolate ping traffic.
- Understand ICMP packet structure (e.g., Echo Request/Reply).
- Save and share PCAP files safely.

## PCAP
Use our sample: [icmp_traffic.pcap](../../../pcaps/icmp_traffic.pcap).  
*Note*: This PCAP is synthetic for educational use.

## Bonus Task
- Count how many Echo Requests vs. Replies in your capture using `Statistics > Packet Lengths`.
- Share your findings in our [Discussions](https://github.com/yourusername/Wireshark-Mastery/discussions) for a chance to earn the 🦈 **Shark’s Approval** badge!

## Solution
Stuck? Check the [detailed solution](solutions/solution_2.md) for a step-by-step guide with screenshots.

## Reward
Complete this challenge to progress toward the 🏅 **Packet Novice** badge! See [Badges](../../../docs/badges.md).

---

[Back to Challenges](../../../README.md#challenges) | [Next Challenge](challenge_3.md)
