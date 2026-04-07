<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics/fqdns -->
<!-- Fetched: 2026-03-31T18:59:34.101387+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, networking, fqdns -->

# Domains Required for Strata Cloud Manager

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Strata Cloud Manager Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Subscription & Tenant Management
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Getting Started
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 AIOps
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Device Telemetry for AIOps](/content/techdocs/en_US/strata-cloud-manager/aiops/about-metrics.html)
 

 
 

**[Next
                                
                                    Optimize Security Posture](/content/techdocs/en_US/strata-cloud-manager/aiops/security-posture.html)
 

 

---

 
 
 















 

# Domains Required for Strata Cloud Manager



 If using a proxy, allow these domains to use Strata Cloud Manager.



 






















 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)

- [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)
- [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by | One of these:
                                AIOps for NGFW Premium or |


If outbound traffic from your devices
passes through a proxy, ensure that you have allowed the following
FQDNs in order to successfully use Strata Cloud Manager.

## Domains to Access Strata Cloud Manager

Allow
these domains in order to access the Strata Cloud Manager application,
regardless of your geographic region.

- *.prod.di.paloaltonetworks.cloud

- *.paloaltonetworks.com
- *.prod.di.paloaltonetworks.com
- *.prod.reporting.paloaltonetworks.com
- *.receiver.telemetry.paloaltonetworks.com
- https://storage.googleapis.com

## App-IDs and Domains to Send Telemetry

See [TCP Ports and FQDNs Required
for](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/ports-and-fqdns) for the App-IDs and ports that you must
allow on your Palo Alto Networks firewalls to successfully send
telemetry data to Strata Cloud Manager.

On your proxy
server, in addition to allowing the required [ports and FQDNs](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/ports-and-fqdns), allow
the domain that corresponds to your geographic region so that your
devices can send telemetry data to Strata Cloud Manager.
























 

| Region | Domain |
| --- | --- |
| US | http://br-prd1.us.cdl.paloaltonetworks.com/ |
| Europe | http://br-prd1.nl.cdl.paloaltonetworks.com/ |
| UK | http://br-prd1.uk.cdl.paloaltonetworks.com/ |
| Canada | http://br-prd1.ca1.ne1.cdl.paloaltonetworks.com/ |
| Singapore | http://br-prd1.sg1.se1.cdl.paloaltonetworks.com/ |
| Japan | http://br-prd1.jp1.ne1.cdl.paloaltonetworks.com/ |
| Australia | http://br-prd1.au1.se1.cdl.paloaltonetworks.com/ |
| Germany | http://br-prd1.de1.ew3.cdl.paloaltonetworks.com/ |
| India | http://br-prd1.in1.as1.cdl.paloaltonetworks.com/ |