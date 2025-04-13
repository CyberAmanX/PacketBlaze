# Intermediate Challenge 1: Analyze TCP Handshake

**Case File: The Connection Conundrum** 🕵️‍♂️  
A client can’t connect to a server. Is the TCP handshake failing? Investigate the three-way handshake to find out!

## Objective
Use Wireshark to capture and analyze a TCP three-way handshake (SYN, SYN-ACK, ACK).

## Prerequisites
- Wireshark installed.
- A browser and internet access.
- Basic filter knowledge (`tcp`).

## Steps
1. Open Wireshark and select your active interface.
2. Start capturing packets.
3. Open a browser and visit `example.com` to initiate a TCP connection.
4. In Wireshark, apply the filter `tcp.port == 80` to focus on HTTP traffic.
5. Identify the TCP handshake (SYN, SYN-ACK, ACK).
6. Save as `tcp_handshake.pcap` in `pcaps/`.

## Common Challenges
- **Issue**: Too many packets.
  - **Fix**: Use `tcp.port == 80 and ip.addr == <server_ip>` (find server IP from packets).
- **Issue**: No handshake found.
  - **Fix**: Clear browser cache or try `curl example.com`.

## Learning Outcomes
- Understand TCP handshake mechanics.
- Use port-based filters.
- Identify packet flags (SYN, ACK).

## PCAP
Sample: [tcp_handshake.pcap](../../../pcaps/tcp_handshake.pcap).

## Bonus Task
- Find the server’s IP in the handshake and check its Round-Trip Time (RTT) in `Statistics > TCP Stream Graphs`.
- Share in [Discussions](https://github.com/yourusername/PacketBlaze/discussions) for 🔥 **Flame Master**!

## Solution
See [solution](solutions/solution_1.md).

## Reward
Progress toward 🦈 **Inferno Champion**! See [Badges](../../../docs/badges.md).

---

[Back to Challenges](../../../README.md#challenges) | [Next Challenge](challenge_2.md)