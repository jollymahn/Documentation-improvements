<!-- Source: https://docs.paloaltonetworks.com/ngfw/aiops/about-metrics/enable-telemetry -->
<!-- Fetched: 2026-03-31T18:30:16.349691+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: ngfw, telemetry -->

# Device Telemetry for AIOps

 

 
 
 
 
 
 

 

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
                            
                                    Troubleshoot NGFW Connectivity and Policy Enforcement Anomalies](/content/techdocs/en_US/strata-cloud-manager/aiops/about/troubleshooting.html)
 

 
 

**[Next
                                
                                    Domains Required for Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/aiops/about-metrics/fqdns.html)
 

 

---

 
 
 















 

# Device Telemetry for AIOps



 Learn about how Strata Cloud Manager uses PAN-OS device telemetry.



 






















 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)

- [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)
- [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by | One of these:
                                AIOps for NGFW Premium or |


AIOps for NGFW helps you monitor the health of your firewalls by
 analyzing data sent from your PAN-OS devices to the Strata Logging Service.

To start, you need to [enable device telemetry](https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-admin/device-telemetry/device-telemetry-configure/device-telemetry-enable.html) on your firewalls.
 Once enabled, they'll send raw telemetry data at [fixed intervals](https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-admin/device-telemetry/device-telemetry-collection.html). Strata Logging Service then processes this data, allowing AIOps for NGFW to provide you with device status, visualizations, and alerts. [Onboard your devices](https://docs.paloaltonetworks.com/content/techdocs/en_US/aiops/aiops-for-ngfw/get-started-with-aiops/enable-telemetry.html) to begin sending device
 telemetry to AIOps for NGFW

Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8, 10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview) configures
 telemetry to be enabled by default on your devices. Upon onboarding a new device
 (Panorama or firewall), telemetry is automatically enabled with settings centrally
 controlled through Strata Cloud Manager. This centralized approach ensures consistent
 telemetry settings across your entire environment. Metrics are automatically streamed to
 your data residency region, eliminating the need for manual configuration.

## Enable Telemetry on Devices

 Follow the steps below to use AIOps for NGFW with your PAN-OS devices. 

If your outbound traffic passes through a proxy, ensure that you have allowed the
 [Domains Required for Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/aiops/about-metrics/fqdns.html). 

 
 You need to onboard Panorama on AIOps for NGFW if you are onboarding
 Panorama-managed deployments.

1. Confirm the device is registered in the Customer Support Portal by logging in to
 [support.paloaltonetworks.com](https://support.paloaltonetworks.com), switch to your account
 (if necessary), and identify your device in AssetsDevices. 
2. [Install a device certificate](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/certificate-management/obtain-certificates/device-certificate.html) on the
 devices you want to onboard. 
3. [Enable telemetry sharing](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry/device-telemetry-configure/device-telemetry-enable.html) on the
 devices. 

 
 After you onboard the devices and enable telemetry, it takes around
 couple of hours for the first set of insights to be visible on the AIOps
 for NGFW dashboard. The process of generating and sending telemetry on
 the device's side is done in batches, with each metric being sampled and
 collected at a frequency optimized for the use-cases the metric is used
 for. This batch process can result in a delay between onboarding the
 firewall and the availability of insights. It might take several hours
 for all insights associated with a newly onboarded device to appear on
 the AIOps for NGFW dashboard.