# Intermediate Challenge 3: Spot ARP Spoofing

**Case File: The Rogue Router** 🕵️‍♂️  
Suspicious network behavior suggests ARP spoofing. Can you detect it in a PCAP?

## Objective
Analyze a PCAP to identify ARP spoofing by checking for duplicate MAC addresses.

## Prerequisites
- Wireshark.
- `arp` filter knowledge.

## Steps
1. Open [arp_spoof.pcap](../../../pcaps/arp_spoof.pcap) in Wireshark.
2. Filter: `arp`.
3. Look for multiple ARP replies for the same IP with different MACs.
4. Note the suspicious MAC address.
5. Save your findings as a screenshot.

## Challenges
- **Issue**: No ARP packets.
  - **Fix**: Ensure correct PCAP.
- **Issue**: Confusing replies.
  - **Fix**: Sort by IP in Packet List.

## Outcomes
- Detect ARP spoofing.
- Use `arp` filter.

## PCAP
[arp_spoof.pcap](../../../pcaps/arp_spoof.pcap).

## Bonus Task
- Use `Statistics > Endpoints` to list MACs.
- Share suspicious MACs in [Discussions](https://github.com/yourusername/PacketBlaze/discussions).

## Solution
See [solution](solutions/solution_3.md).

## Reward
Earn 🦈 **Inferno Champion** progress.

---

[Back to Challenges](../../../README.md#challenges)