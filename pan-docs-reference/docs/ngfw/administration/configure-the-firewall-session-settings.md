<!-- Source: https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/configure-the-firewall-session-settings -->
<!-- Fetched: 2026-04-01T01:59:18.267315+00:00 -->
<!-- Project: scm -->
<!-- Tags: ngfw, onboarding, config -->

# Session Settings and Timeouts

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Next-Generation Firewall Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Getting Started
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Administration
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Networking
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Quick Start
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Reference
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Incidents & Alerts
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - PAN-OS 12.1
 
  - PAN-OS 11.2
 
  - PAN-OS 11.1
 
  - PAN-OS 11.0 (EoL)
 
  - PAN-OS 10.2
 
  - PAN-OS 10.1
 
  - PAN-OS 10.0 (EoL)
 
  - PAN-OS 9.1 (EoL)
 
  - PAN-OS 9.0 (EoL)
 
  - PAN-OS 8.1 (EoL)
 

 

 

 

 
 

 
 
- 
 
 
 
 
 

 Help
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - PAN-OS 12.1
 
  - PAN-OS 11.2
 
  - PAN-OS 11.1
 
  - PAN-OS 10.2
 
  - PAN-OS 10.1
 

 

 

 

 
 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Reference: BFD Details](/content/techdocs/en_US/ngfw/networking/bfd/reference-bfd-details.html)
 

 
 

**[Next
                                
                                    TCP](/content/techdocs/en_US/ngfw/networking/session-settings-and-timeouts/tcp.html)
 

 

---

 
 
 















 

# Session Settings and Timeouts



 



 Understand the session settings and timeouts that affect the Transport Layer. 



 






















 

- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by PAN-OS or Panorama) |  |


A network session is an exchange of messages that occurs between two or more
 communication devices, lasting for some period of time. A session is established and is
 torn down when the session ends. Different types of sessions occur at three layers of
 the OSI model: the Transport layer, the Session layer, and the Application layer. 

The Transport Layer operates at Layer 4 of the OSI model, providing reliable or
 unreliable, end-to-end delivery and flow control of data. Internet protocols that
 implement sessions at the Transport layer include the Transmission Control Protocol
 (TCP) and User Datagram Protocol (UDP). 

This section describes the global settings that affect TCP, UDP, and ICMPv6 sessions, in addition
 to IPv6, NAT64, NAT oversubscription, jumbo frame size, MTU, accelerated aging, and
 Captive Portal authentication. There is also a setting (Rematch Sessions) that enables
 you to apply newly configured security policy rules to sessions that are already in
 progress.