<!-- Source: https://docs.paloaltonetworks.com/ngfw/administration/high-availability -->
<!-- Fetched: 2026-04-01T01:59:24.898677+00:00 -->
<!-- Project: scm -->
<!-- Tags: ngfw, ha -->

# High Availability

 

 
 
 
 
 
 

 

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
                            
                                    Manage the HSM Deployment](/content/techdocs/en_US/ngfw/administration/certificate-management/secure-keys-with-hardware-security-module/manage-hsm-deployment.html)
 

 
 

**[Next
                                
                                    HA Modes](/content/techdocs/en_US/ngfw/administration/high-availability/ha-modes.html)
 

 

---

 
 
 















 

# High Availability



 



 Learn how high availability provides redundancy and synchronization between firewalls
 to prevent a single point of failure. 



 






















 

- 
- 

- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by Strata Cloud Manager)NGFW (Managed by PAN-OS or Panorama) | For Strata Cloud Manager managed NGFWs:
                            Strata Cloud Manager Pro |


High availability (HA) is a deployment in which two
firewalls are placed in a group or up to 16 firewalls are placed
in an HA cluster and their configuration is synchronized to prevent
a single point of failure on your network. A heartbeat connection
between the firewall peers ensures seamless failover in the event
that a peer goes down. Setting up HA provides redundancy and allows
you to ensure business continuity.

You can configure two Palo Alto Networks firewalls as an HA pair or configure up to 16
 firewalls as peer members of an HA cluster. The peers in the cluster can be HA pairs or
 standalone firewalls. HA allows you to minimize downtime by making sure that an
 alternate firewall is available in the event that a peer firewall fails. The firewalls
 in an HA pair or cluster use dedicated or in-band HA ports on the firewall to
 synchronize data—network, object, and policy configurations—and to maintain state
 information. Firewall-specific configuration such as management interface IP address or
 administrator profiles, HA specific configuration, log data, and the Application Command
 Center (ACC) information is not shared between peers.

For a consolidated application and log view across an HA pair, you must use Panorama, the
 Palo Alto Networks centralized management system. See [Context Switch—Firewall or Panorama](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/centralized-firewall-configuration-and-update-management/context-switchfirewall-or-panorama) in the [Panorama Administrator’s Guide](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin). Consult the [Set Up Active/Passive HA](/content/techdocs/en_US/ngfw/administration/high-availability/set-up-activepassive-ha.html) and
 [Set Up Active/Active HA](/content/techdocs/en_US/ngfw/administration/high-availability/set-up-activeactive-ha.html). It is highly recommended that you use Panorama to provision HA cluster members.
 Consult the [HA Clustering Best Practices and Provisioning](/content/techdocs/en_US/ngfw/administration/high-availability/ha-clustering-best-practices-and-provisioning.html#id53986e31-4241-4297-9343-0d574a0bdf52).

When a failure occurs on a firewall in an HA pair or HA cluster and a peer firewall takes
 over the task of securing traffic, the event is called a [Failover](/content/techdocs/en_US/ngfw/administration/high-availability/failover.html#id9e9b71b2-80f4-4ebb-8528-0bb3c47b8402). The conditions that
 trigger a failover are:

- One or more of the monitored interfaces fail. ([Link
                        Monitoring](/content/techdocs/en_US/ngfw/administration/high-availability/failover.html#id9e9b71b2-80f4-4ebb-8528-0bb3c47b8402_ida5d5e777-e43d-41a2-aa05-c6c6147a0a0f))

- One or more of the destinations specified on the firewall cannot be reached.
 ([Path
                        Monitoring](/content/techdocs/en_US/ngfw/administration/high-availability/failover.html#id9e9b71b2-80f4-4ebb-8528-0bb3c47b8402_idc6eda85f-7926-4957-bcad-4f2b57feac67))

- The firewall does not respond to heartbeat polls. ([Heartbeat Polling
                        and Hello messages](/content/techdocs/en_US/ngfw/administration/high-availability/failover.html#id9e9b71b2-80f4-4ebb-8528-0bb3c47b8402_id658ef543-082f-40a8-a866-b1ee5f1ffc1c))

- A critical chip or software component fails, known as packet path health
 monitoring.

Palo Alto Networks firewalls support stateful active/passive or active/active high
 availability with session and configuration synchronization with a few exceptions:

- The [VM-Series firewall on Azure](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-azure.html) and [VM-Series firewall on AWS](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws.html) support
 active/passive HA only. 

On AWS, when you deploy the firewall with the Amazon Elastic Load Balancing (ELB)
 service, it does not support HA (in this case, ELB service provides the failover
 capabilities).

- The VM-Series firewall on Google Cloud Platform does not support HA.