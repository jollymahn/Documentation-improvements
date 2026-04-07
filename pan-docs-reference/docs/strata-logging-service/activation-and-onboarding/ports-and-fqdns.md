<!-- Source: https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/planning/ports-and-fqdns -->
<!-- Fetched: 2026-03-31T18:05:09.789493+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags:  -->

# TCP Ports and FQDNs Required for Strata Logging Service

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Strata Logging Service Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Administration
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Log Reference
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Sizing for Strata Logging Service Storage](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/planning/sizing.html)
 

 
 

**[Next
                                
                                    Activate Strata Logging Service](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/activate.html)
 

 

---

 
 
 















 

# TCP Ports and FQDNs Required for Strata Logging Service



 List of FQDNs and ports that you must allow to ensure
connectivity to Strata Logging Service.



 






















 

- [Software NGFW
                                    Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 

- [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)
- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma Access | One of these:Strata Logging Service |


Depending on the platform you are using, you must allow
traffic from different sources to connect to Strata Logging Service successfully.

 
 If you're using a proxy, ensure that it allows connections to non-standard SSL ports
 3978 and 444.

- App-IDs for Palo Alto Networks Firewalls

- FQDNs for Panorama and PANW Firewalls

- Region FQDNs

## App-IDs
for Palo Alto Networks Firewalls

If you are using a Palo
Alto Networks firewall to secure traffic between Panorama, the firewalls,
and Strata Logging Service, use the following table to identify the App-IDs
and ports to which you must allow traffic to ensure that Panorama
and the firewalls can successfully connect to Strata Logging Service:
























 

- [device telemetry](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/device-telemetry/device-telemetry-overview.html)
- 
- [Content](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/software-and-content-updates/app-and-threat-content-updates)

- 

- 

| App-IDs | Ports |
| --- | --- |
| paloalto-logging-service (not
necessary if you are using only  and do
not have a Strata Logging Service license).paloalto-shared-services( version earlier
than 8290) panorama | TCP 444TCP 3978 |


For OCSP, you must also allow the firewalls
to access ocsp.paloaltonetworks.com on port 80.

On firewalls
running PAN-OS 9.1.7 or earlier, you also need a Security policy
rule that allows SSL over port 444 to lic.lc.prod.us.cs.paloaltonetworks.com.

(PAN-OS 10.0 or later) If you are sending [telemetry data](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/device-telemetry/device-telemetry-overview.html) to Strata Logging Service, then, in addition to the above App-IDs and ports
 (except paloalto-logging-service), you must allow the
 following:
























 

- 

- 

- 
- 
- 
- 

| App-IDs | Ports |
| --- | --- |
| paloalto-device-telemetrygoogle-base | TCP 443TCP 5222-5224TCP 5228TCP 5229 |



## FQDNs
for Panorama and PANW Firewalls

Panorama and Palo Alto
Networks firewalls need to access these FQDNs for the initial setup
and one-time password, ongoing certificate revocation checks, and
certificate renewals.
























 

- 

- 

- 

- 

- 

- 

- 

| Global FQDNs | Ports |
| --- | --- |
| http://ocsp.paloaltonetworks.comhttp://crl.paloaltonetworks.comhttp://ocsp.godaddy.com | TCP 80 |
| https://api.paloaltonetworks.comhttps://apitrusted.paloaltonetworks.comcertificatetrusted.paloaltonetworks.comcertificate.paloaltonetworks.com | TCP 443 |
| *.gpcloudservice.com | TCP 444 and TCP 443 |
| lic.lc.prod.us.cs.paloaltonetworks.com | TCP 444 |



## Region FQDNs

Additional region-specific FQDNs used by Panorama and Firewall to send logs to Strata Logging
 Service are available [here](https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-logging-service/administration/overview/supported-regions.html). If you have another vendor's
 firewall in between your Palo Alto Networks firewall and Strata Logging Service, allow traffic to the FQDNs and ports for your Strata Logging Service
 [region](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview/supported-regions).