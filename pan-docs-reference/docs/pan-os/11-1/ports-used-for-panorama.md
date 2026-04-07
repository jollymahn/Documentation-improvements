<!-- Source: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama -->
<!-- Fetched: 2026-04-01T01:59:31.625041+00:00 -->
<!-- Project: scm -->
<!-- Tags: panorama, ports -->

# Ports Used for Panorama

 

 
 
 
 
 
 

 

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
                            
                                    Ports Used for Clustering](/content/techdocs/en_US/ngfw/administration/firewall-administration/reference-port-number-usage/ports-used-for-clustering.html)
 

 
 

**[Next
                                
                                    Ports Used for GlobalProtect](/content/techdocs/en_US/ngfw/administration/firewall-administration/reference-port-number-usage/ports-used-for-globalprotect.html)
 

 

---

 
 
 















 

# Ports Used for Panorama



 



 Network ports and port numbers used by Panorama for firewall management, device
 communication, and administrative functions.



 Panorama uses the following ports.
























 

[Panorama](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin.html)

[Strata Logging Service](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/ports-and-fqdns)

- 

- 

- 

[failover](/content/techdocs/en_US/ngfw/administration/high-availability/failover.html)

| Destination Port | Protocol | Description |
| --- | --- | --- |
| 22 | TCP | Used for communication from a client system
to the  CLI interface. |
| 443 | TCP | Used for communication from a client system
to the Panorama web interface.
                            Used for outbound communications from Panorama to the Palo Alto
                                Networks Update Server. |
| 444 | TCP | Used for communication between Panorama and . |
| 3978 | TCP | Used for communication between Panorama
and managed firewalls or managed collectors, as well as for communication
among managed collectors in a Collector Group:For
communication between Panorama and firewalls. This connection is
initiated from the managed firewall to Panorama and facilitates
a bi-directional data exchange on which the firewalls forward logs
to Panorama and Panorama pushes configuration changes to the firewalls. Context
switching commands are sent over the same connection.Log Collectors use this destination port to forward logs
to Panorama.For communication with the default Log Collector on an M-Series
appliance in Panorama mode and with Dedicated Log Collectors. |
| 28443 | TCP | Used for managed devices (firewalls and
Log Collectors) to retrieve software and content updates from Panorama.
    
    Only
devices that run PAN-OS 8.x and later releases retrieve updates
from Panorama over this port. For devices running earlier releases,
Panorama pushes the update packages over port 3978. |
| 2876928260 | TCPTCP | Used for the HA connectivity and synchronization
between Panorama HA peers using clear text communication. Communication
can be initiated by either peer.
                            
    
    ICMP must be allowed on the network for successful Panorama HA
                                    peer connection and synchronization. Additionally, ICMP is
                                    required to monitor the  metrics used to
                                    detect whether an HA failover is required. |
| 28 | TCP | Used for the HA connectivity and synchronization
between Panorama HA peers using encrypted communication (SSH over
TCP). Communication can be initiated by either peer.Used
for communication between Log Collectors in a Collector Group for
log distribution. |
| 28270
                            9300 to 9302 (11.1 and later) | TCP | Used for communication among Log Collectors
in a Collector Group for log distribution. |
| 2049 | TCP | Used by the Panorama virtual appliance to
write logs to the NFS datastore. |
| 10443 | SSL | Port that Panorama uses to provide contextual
information about a threat or to seamlessly shift your threat investigation
to the Threat Vault and AutoFocus. |
| 23000 to 23999 | TCP, UDP, or SSL | Used for Syslog communication between Panorama
and the Traps ESM components. |