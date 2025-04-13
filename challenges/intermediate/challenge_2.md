# Intermediate Challenge 2: Detect Slow HTTP Responses

**Case File: The Sluggish Site** 🕵️‍♂️  
Users complain a website’s slow. Is the server lagging? Analyze HTTP response times to diagnose the issue.

## Objective
Use Wireshark to measure HTTP response times and identify delays.

## Prerequisites
- Wireshark.
- Browser.
- `http` filter knowledge.

## Steps
1. Start Wireshark on your active interface.
2. Capture packets.
3. Visit `example.com` in a browser.
4. Filter: `http.response`.
5. Check `Time` column for delays (>1s is slow).
6. Save as `http_slow.pcap`.

## Challenges
- **Issue**: No HTTP responses.
  - **Fix**: Clear cache, revisit site.
- **Issue**: Mixed traffic.
  - **Fix**: Use `http.response and ip.addr == <server_ip>`.

## Outcomes
- Measure HTTP delays.
- Use `http.response` filter.

## PCAP
[http_slow.pcap](../../../pcaps/http_slow.pcap).

## Bonus Task
- Use `Statistics > HTTP > Requests` to list response codes.
- Share slow responses in [Discussions](https://github.com/yourusername/PacketBlaze/discussions).

## Solution
See [solution](solutions/solution_2.md).

## Reward
Earn 🔥 **Flame Master** progress.

---

[Back to Challenges](../../../README.md#challenges) | [Next Challenge](challenge_3.md)